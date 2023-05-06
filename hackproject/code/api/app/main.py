import os
import time
import traceback
import uuid

import telebot
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from googletrans import Translator
from langchain import OpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import LLMPredictor, LangchainEmbedding, ServiceContext
from starlette.requests import Request
from telebot import types

import sys

sys.path.extend([
    os.path.abspath(os.path.join('..')),
    os.path.abspath(os.path.join('..','..')),
    os.path.abspath(os.path.join('..','..', '..')),
    os.path.abspath(os.path.join('..','..','..','..'))
])

from hackproject.code.api.app.enums import Product
from hackproject.code.api.app.schemas.model_service.model_service_schemas import PromptResponse
from hackproject.code.api.app.schemas.tts_service.tts_schemas import TTS
from hackproject.code.api.app.schemas.prompt_service.prompt_service_schema import WebPrompt, ProcessedPrompt, \
    ChatInitialization
from hackproject.code.api.app.services.chat_service.chat_service import ChatServiceImpl, ChatService
from hackproject.code.api.app.services.prompt_service.prompt_service import PromptServiceImpl, PromptService
from hackproject.code.api.app.services.tts_service.tts import tts as parrot
from hackproject.code.api.app.services.axa.axa_service import get_questions, compute, products
from hackproject.code.api.app.schemas.axa_service.axa_schemas import Question, QuestionDetail, SubmissionResponse, State

# laod env's
load_dotenv()

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
BASE_URL = os.environ["BASE_URL"]

## models
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))
embed_model = LangchainEmbedding(HuggingFaceEmbeddings())
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, embed_model=embed_model)

# web
app = FastAPI()
router = APIRouter(prefix="/api/v1/chat")

# messaging
bot = telebot.TeleBot(TELEGRAM_API_KEY)

# dependencies
prompt_service: PromptService = PromptServiceImpl()
chat_service: ChatService = ChatServiceImpl()
translator = Translator()

from fastapi.responses import FileResponse
from starlette.background import BackgroundTask
from hackproject.code.api.app.utils import remove_file

@router.post("/tts/{message_id}")
async def tts(message_id:str, payload:TTS):
    path = parrot(payload.text, payload.language, message_id)
    return FileResponse(path, background=BackgroundTask(remove_file, path))

@router.get("/axa/products", response_model=list[Product])
async def get_products():
    return await products()

@router.get("/axa/{product}/questions", response_model=list[Question])
async def questions(product:str, language: str = 'en'):
    return await get_questions(product, language)

@router.get("/axa/{product}/questions/{question_id}", response_model=QuestionDetail)
async def get_question_by_id(product:str, question_id:str, language: str = 'en'):
    return await get_questions(product, language, question_id)

@router.post("/axa/{product}/compute", response_model=SubmissionResponse)
async def submit(product:str, payload:list[State], language: str = 'en'):
    return await compute(product, language, payload)

@router.get("/web")
async def web_prompt():
    chat_id = str(uuid.uuid4())
    initialization_details = ChatInitialization(chat_id=chat_id, product=Product.WEB)
    return chat_service.initialize(initialization_details)

@router.post("/web")
async def web_prompt(request: WebPrompt):
    processed_prompt: ProcessedPrompt = prompt_service.process_prompt(request)
    prompt_response: PromptResponse = chat_service.reply_prompt(processed_prompt)
    return prompt_response

@router.post("/messaging/" + bot.token)
async def mobile_prompt(request: Request):
    data = await request.json()
    data = telebot.types.Update.de_json(data)
    bot.process_new_updates([data])

@bot.message_handler(content_types=['document', 'text'])
def handle_document(message: types.Message):
    if message.text and message.text in ['/start', 'start']:
        initialization_details = ChatInitialization(product=Product.MESSAGING, chat_id=message.chat.id)
        chat_service.initialize(initialization_details)
        return {'ok': True}
    else:
        try:
            processed_prompt: ProcessedPrompt = prompt_service.process_prompt(message)
            chat_service.reply_prompt(processed_prompt)
        except:
            bot.reply_to(message, "An error occurred, please try again later.")
            traceback.print_exc()
        finally:
            return {'ok': True}

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'location', 'poll', 'contact'])
def echo_all(message):
    bot.send_chat_action(chat_id=message.chat.id, action='typing')
    time.sleep(1)
    bot.reply_to(message, "I can only help you with documents and texts")
    return {'ok': True}

app.include_router(router=router)

bot.remove_webhook()
bot.set_webhook(url=f'{BASE_URL}/api/v1/chat/messaging/' + bot.token)