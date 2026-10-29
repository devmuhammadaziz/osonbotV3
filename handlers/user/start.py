from aiogram import Router, F
from aiogram.types import Message, ContentType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.state import any_state
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from loguru import logger

from keyboards.inline.HomeButton import allRegionsKvartira
from keyboards.inline.data import StartData, GoBackData
from keyboards.default.JobButton import send_contact
from loader import bot, dp, db

user_router = Router()


@user_router.message(CommandStart())
async def bot_start(message: Message, state: FSMContext):
    await state.clear()
    telegram_id = str(message.chat.id)
    user = await db.get_one_user(chat_id=telegram_id)
    
    if user:
        await message.answer("Ассалому алайкум!", reply_markup=ReplyKeyboardRemove())
        await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")  
    else:
        await message.answer("Телефон рақамингизни тасдиқланг", reply_markup=send_contact) 


@user_router.message(F.content_type == ContentType.CONTACT)
async def check_contact(message: Message, state: FSMContext):
    await state.clear()
    if not message.contact:
        logger.info("No contact information found in the message.")
        return

    contact = message.contact.phone_number
    telegram_id = str(message.chat.id)
    full_name = message.from_user.full_name if message.from_user else "User"
    username = message.from_user.username if (message.from_user and message.from_user.username) else "null"

    logger.info(f"Attempting to add user: {full_name}, {username}, {telegram_id}, {contact}")
    
    try:
        user = await db.get_one_user(chat_id=telegram_id)
        if not user:
            await db.add_user(name=full_name, username=username, chat_id=telegram_id, phone=contact)
        
        await message.answer("Рақамингиз муваффақиятли қабул қилинди! ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")
    except Exception as error:
        logger.error(f"Error saving user contact: {error}")
        await message.answer("Рақамингиз қабул қилинди ✅", reply_markup=ReplyKeyboardRemove())
        await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.callback_query(StartData.filter(F.word=="start"), any_state)
async def starter_bot(call: CallbackQuery, state: FSMContext, callback_data: StartData):
    await call.answer("Bot ishga tushdi")
    await state.clear()
    if isinstance(call.message, Message):
        await call.message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text.casefold() == "start", any_state)
async def restart_cmd(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Ассалому алайкум!", reply_markup=ReplyKeyboardRemove())
    await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text == "/stop", any_state)
async def stop(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Bot тўхтатилди", reply_markup=ReplyKeyboardRemove())


@user_router.message(F.text == "/restart", any_state)
async def restart(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Ассалому алайкум!", reply_markup=ReplyKeyboardRemove())
    await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text == "⬅️ Ортга")
async def ortga(message: Message):
    await message.answer("<b> Ҳудудни танланг </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.callback_query(GoBackData.filter(F.word == "ortga"))
async def kvartirasotish(call: CallbackQuery):
    await call.answer("Категорияни танланг")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")
