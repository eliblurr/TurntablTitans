import requests, os
from hackproject.code.api.app.schemas.axa_service.axa_schemas import Product,Question, Answer, QuestionDetail, State, SubmissionResponse, Coverage
from dotenv import load_dotenv
from fastapi import HTTPException


load_dotenv()

COMPUTATION_URL=os.environ["AXA_COMPUTATION_URL"]
SPECIFICATION_URL=os.environ["AXA_SPECIFICATION_URL"]
HEADERS = {
    "x-api-key":os.environ["AXA_API_KEY"]
}
base_payload={
    "policy": {
        "endorsements": []
    },
    "match": [],
    "claim": {
        "lines": [
            {
                "state": [],
                "line_ref": "string"
            }
        ]
    }
}


async def products():
    return Product(
        id="162306",
        name="motor"
    )

async def get_questions(product_id:str, language:str, question_id:str=None, base=base_payload):
    HEADERS["accept-language"]=language
    if question_id!=None:
        base.update({
            "productId": product_id,
            "questionId": question_id,
            "questionLineRef": "root",
            "ignoreTriggers": False,
            "onlyNext": False
        })
        res = requests.post(SPECIFICATION_URL, headers=HEADERS, json=base)

        if res.status_code!=200:
            raise HTTPException(status_code=res.status_code, detail=res.json())

        return QuestionDetail(
            id=res.json().get("id", ""),
            order=res.json().get("order", 0),
            question=res.json()["metadata"][0]["value"],
            possible_answers=[Answer(
                id=answer.get("id", None),
                answer=answer.get("displayName", None),
                priority=answer.get("priority", None),
                extra=answer.get("columns", {})
            ) for answer in res.json().get("answers", []) if answer["id"] in res.json().get("possibleAnswers", []) ]
        )
    
    base["productId"]=product_id
    res = requests.post(COMPUTATION_URL, headers=HEADERS, json=base)
    if res.status_code!=200:
        raise HTTPException(status_code=res.status_code, detail=res.json())
    return [
        Question(
            id=question.get("id", None), 
            order=question.get("order", 0),
            question=question["metadata"][0]["value"] 
        ) 
        for question in res.json()["questions"] 
        if "metadata" in question.keys() and len(question.get("metadata", [])) >= 1
    ]

async def compute(product_id:str, language:str, payload: list[State]=[], base=base_payload):
    HEADERS["accept-language"]=language
    base.update({"productId": product_id})
    base["claim"]["lines"][0]["state"]=[state.dict() for state in payload]
    res = requests.post(COMPUTATION_URL, headers=HEADERS, json=base)
    if res.status_code!=200:
        raise HTTPException(status_code=res.status_code, detail=res.json())
    
    data = res.json()
    return SubmissionResponse(
        next_question=Question(
            id=data["nextQuestion"]["id"],
            order=data["nextQuestion"]["order"],
            question=data["nextQuestion"]["metadata"][0]["value"]
        ) if "nextQuestion" in data.keys() and "metadata" in data["nextQuestion"] and len(data["nextQuestion"]["metadata"]) >= 1 else None,
        coverage=[Coverage(
           priority=coverage["priority"], 
           status=coverage["result"]["global"]["status"]
        ) for coverage in data["coverageResponses"] ] if "coverageResponses" in data.keys() and len(data["coverageResponses"])>=1 else [],
        progress=data["stats"]["progressPercentage"] if "stats" in data.keys() and "progressPercentage" in data["stats"].keys() else None,
        states=payload
    )
