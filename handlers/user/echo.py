from aiogram import Router, F
from aiogram.types import Message

echo_router = Router()


@echo_router.message(F.text)
async def bot_echo(message: Message):
    if message.text:
        await message.answer(message.text)