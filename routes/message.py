from aiogram import Router, types
from aiogram.filters import Command

from chatgpt import ChatGPT

message_router = Router()


@message_router.message()
async def handle_message(message: types.Message):
    chatgpt = ChatGPT()
    answer = chatgpt.answer(message.text)
    await message.answer(answer)
