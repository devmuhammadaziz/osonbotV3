from aiogram import Router, F
from aiogram.types import Message, ContentType
from aiogram.filters import CommandStart

from keyboards.inline.HomeButton import start_button, allRegionsKvartira

from aiogram.fsm.context import FSMContext

from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.state import any_state

from loader import bot, dp, db

from keyboards.inline.data import StartData, GoBackData

from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from keyboards.default.JobButton import send_contact
from aiogram.client.session.middlewares.request_logging import logger

user_router = Router()


@user_router.message(CommandStart())
async def bot_start(message: Message):
    telegram_id = str(message.chat.id)
    user = await db.get_one_user(chat_id=telegram_id)
    
    if user:
        await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")  
    else:
        await message.answer("Телефон рақамингизни тасдиқланг", parse_mode=ParseMode.MARKDOWN_V2, reply_markup=send_contact) 

@user_router.message(F.content_type == ContentType.CONTACT)
async def check_contact(message: Message):
    if not message.contact:
        logger.info("No contact information found in the message.")
        return

    contact = message.contact.phone_number
    telegram_id = str(message.chat.id)
    full_name = message.from_user.full_name if message.from_user else "User"
    username = message.from_user.username if (message.from_user and message.from_user.username) else "null"

    logger.info(f"Attempting to add user: {full_name}, {username}, {telegram_id}, {contact}")
    
    try:
        user = await db.add_user(name=full_name, username=username, chat_id=telegram_id, phone=contact)
        if user:
            await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")
        else:
            await message.answer("Телефон рақамингизни тасдиқланг", parse_mode=ParseMode.MARKDOWN_V2, reply_markup=send_contact) 
    except Exception as error:
        await bot.send_message(chat_id=message.chat.id, text='Телефон рақамингизни тасдиқланг') 


@user_router.callback_query(StartData.filter(F.word=="start"), any_state)
async def starter_bot(call: CallbackQuery, state: FSMContext, callback_data: StartData):
    await call.answer("Bot ishga tushdi")
    await state.clear()
    await call.message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="START", any_state)
async def first(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("START", reply_markup=ReplyKeyboardRemove())
    await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="start", any_state)
async def first(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("start", reply_markup=ReplyKeyboardRemove())
    await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="/start", any_state)
async def first(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("START", reply_markup=ReplyKeyboardRemove())
    await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")


@user_router.message(F.text=="/stop", any_state)
async def stop(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("START", reply_markup=ReplyKeyboardRemove())
    await message.answer("Bot is stopping", reply_markup=allRegionsKvartira, parse_mode="HTML")

@user_router.message(F.text=="/restart", any_state)
async def restart(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("START", reply_markup=ReplyKeyboardRemove())
    await message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")

@user_router.message(F.text=="⬅️ Ортга")
async def ortga(message: Message):
    await message.answer("<b> Ҳудудни танланг </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")

@user_router.callback_query(GoBackData.filter(F.word=="ortga"))
async def kvartirasotish(call: CallbackQuery):
    await call.answer("Категорияни танланг")
    await call.message.answer("START", reply_markup=ReplyKeyboardRemove())
    await call.message.answer("<b> Ҳудудни танланг  </b>", reply_markup=allRegionsKvartira, parse_mode="HTML")
