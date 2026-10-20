from aiogram import Router, F, Bot
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.parse_mode import ParseMode

from filters.group_chat import IsGroup, IsGroupCall
from loader import bot
from keyboards.inline.HomeButton import admin
from keyboards.inline.data import AdminXabarYuborish

# Define the FSM states
class SendPoster(StatesGroup):
    waiting_for_text = State()

import config

# Initialize the router
group_router = Router()

CHANNEL_IDS = config.ALL_CHANNEL_IDS

@group_router.message(IsGroup(), Command('show'))
async def sendmessage(message: Message):
    await message.answer("Admin Panel", reply_markup=admin)


@group_router.callback_query(IsGroupCall(), AdminXabarYuborish.filter(F.word == "AdminXabar"))
async def ask_for_text(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Xabaringizni yozing:", parse_mode=ParseMode.HTML)
    await state.set_state(SendPoster.waiting_for_text)

# Message handler to receive the text and forward it to channels
@group_router.message(IsGroup(), F.content_type == ContentType.TEXT)
async def receive_text(message: Message, state: FSMContext):
    # Check if the state is waiting for text
    current_state = await state.get_state()
    if current_state == SendPoster.waiting_for_text:
        # Forward the text to all channels
        for channel_id in CHANNEL_IDS:
            await bot.send_message(chat_id=channel_id, text=message.text, parse_mode=ParseMode.HTML)


        await message.answer("Xabar barcha kanallarga yuborildi!", parse_mode=ParseMode.HTML)
        # Finish the state
        await state.clear()

# Handler for other messages if they are not text
@group_router.message(IsGroup(), ~F.content_type == ContentType.TEXT)
async def not_text_message(message: Message, state: FSMContext):
    # Check if the state is waiting for text
    current_state = await state.get_state()
    if current_state == SendPoster.waiting_for_text:
        await message.answer("To\'gri xabar yuboring", parse_mode=ParseMode.HTML)
