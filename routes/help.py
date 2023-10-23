from aiogram import Router, types
from aiogram.filters import Command

help_router = Router()


@help_router.message(Command(commands=['help']))
async def help(message: types.Message):
    await message.answer("Что бы воспользоваться ботом, тебе нужно просто написать ему любое сообщение без команды.")
