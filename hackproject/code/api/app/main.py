import os
import time
import traceback
import uuid

import telebot
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from langchain import OpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index import LLMPredictor, LangchainEmbedding, ServiceContext
from starlette.requests import Request
from telebot import types

from hackproject.code.api.app.enums import Product
from hackproject.code.api.app.schemas.model_service.model_service_schemas import PromptResponse
from hackproject.code.api.app.schemas.prompt_service.prompt_service_schema import WebPrompt, ProcessedPrompt, \
    ChatInitialization
from hackproject.code.api.app.services.chat_service.chat_service import ChatServiceImpl, ChatService
from hackproject.code.api.app.services.prompt_service.prompt_service import PromptServiceImpl, PromptService

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