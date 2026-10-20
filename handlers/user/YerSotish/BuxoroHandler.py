from utils.collage import build_collage_or_photo, elon_inline_button
import ast
from typing import List
from aiogram import Bot, types, F, Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types.callback_query import CallbackQuery

from keyboards.default.JobButton import checkbtn, start
from keyboards.default.JobButton import otkazishButton
from keyboards.inline.HomeButton import remontButton, documentButton, valyutaButton, borYoq
from keyboards.inline.HomeButton import buxoro_group

from loader import bot, db
from states.YerSotish.BuxoroState import BuxoroYerSotish

from transliterate import to_cyrillic

from utils.QuestionYer.yerqs import hovlitanlandi, rasmlar, umumiyMaydonyoz, faqatRaqamyoz, gazyoz, \
    jihozlaryoz, kanalizatsiyayoz, manzilyoz, moljalyoz, narxiyoz, nechaQavatyoz,oshxonayoz, \
    qoshimchaMalumotyoz, remontyoz, suvyoz, svetyoz, telraqam1yoz, telraqam2yoz, valyutayoz, \
    xammomyoz, xonalaryoz, buxoro_id, check_text, buxororegion, data2, data32, data33, \
    data34, data35, success_text, hujjatlaribormiyoz, group_id, success_message, fail_message


from keyboards.inline.data import BuxoroYerData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import DocumentHaveData, DocumentNotData
from keyboards.inline.data import USDData, SUMData
from keyboards.inline.data import TasdiqlashBuxoro, BekorQilishBuxoro

mode = "Markdown"

from aiogram_media_group import media_group_handler
from utils.media_group import MediaGroupBuilder


from filters.group_chat import IsGroup, IsGroupCall


buxoro_yer_router = Router()

@buxoro_yer_router.callback_query(BuxoroYerData.filter(F.word=="buxoroyer"))
async def first(callback_query: CallbackQuery, state: FSMContext, callback_data: BuxoroYerData):
    # await callback_query.answer(hovlitanlandi)
    await callback_query.message.answer(rasmlar, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.images)


@buxoro_yer_router.message(BuxoroYerSotish.images, F.photo, ~F.media_group_id)
async def single_photo_handler(message: Message, state: FSMContext):
    if not message.photo:
        return
    file_id = message.photo[-1].file_id
    await state.update_data({"images": [file_id]})
    await message.answer(umumiyMaydonyoz, parse_mode="HTML")
    await state.set_state(BuxoroYerSotish.umumiyMaydon)


@buxoro_yer_router.message(BuxoroYerSotish.images, F.media_group_id, F.content_type.in_({'photo'}))
@media_group_handler
async def album_handler(messages: List[types.Message], state: FSMContext):
    file_ids = []
    for msg in messages:
        if msg.photo:
            file_ids.append(msg.photo[-1].file_id)

    await state.update_data({
        "images": file_ids
    })

    await messages[-1].answer(umumiyMaydonyoz, parse_mode="HTML")
    await state.set_state(BuxoroYerSotish.umumiyMaydon)


@buxoro_yer_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    BuxoroYerSotish.umumiyMaydon)
async def check_umumiy(message: Message):
    await message.reply(faqatRaqamyoz)


@buxoro_yer_router.message(BuxoroYerSotish.umumiyMaydon)
async def umumiymaydon(message: Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "umumiyMaydon": text
    })

    await bot.send_message(chat_id=message.chat.id, text=gazyoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.gaz)


# ================================================================

@buxoro_yer_router.callback_query(BorData.filter(F.word=="bor"), BuxoroYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = "Газ ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(BuxoroYerSotish.svet)


@buxoro_yer_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroYerSotish.gaz)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "gaz": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=svetyoz, reply_markup=borYoq)
    await state.set_state(BuxoroYerSotish.svet)

# ========================================================================
    
@buxoro_yer_router.callback_query(BorData.filter(F.word=="bor"), BuxoroYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Свет ✔️"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(BuxoroYerSotish.suv)


@buxoro_yer_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroYerSotish.svet)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Танланди")

    await state.update_data({
        "svet": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=suvyoz, reply_markup=borYoq)
    await state.set_state(BuxoroYerSotish.suv)

# ============================================================================

@buxoro_yer_router.callback_query(BorData.filter(F.word=="bor"), BuxoroYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Сув ✔️"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.kanal)


@buxoro_yer_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroYerSotish.suv)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "suv": text
    })

    await callback_query.message.answer(text=kanalizatsiyayoz, reply_markup=borYoq, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.kanal)

# ============================================================================

@buxoro_yer_router.callback_query(BorData.filter(F.word=="bor"), BuxoroYerSotish.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: BorData):
    text = " Канализация ✔️"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton, parse_mode="HTML")

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(BuxoroYerSotish.qoshimchaMalumot)
    else:
        await state.set_state(BuxoroYerSotish.qoshimchaMalumot)


@buxoro_yer_router.callback_query(YoqData.filter(F.word=="yoq"), BuxoroYerSotish.kanal)
async def xonalar(callback_query: types.CallbackQuery, state: FSMContext, callback_data: YoqData):
    text = "doesnotexist"
    # await callback_query.answer("Tanlandi")

    await state.update_data({
        "kanal": text
    })

    await callback_query.message.answer(text=qoshimchaMalumotyoz, reply_markup=otkazishButton, parse_mode="HTML")

    if callback_query.message.text == "⏭️ Кейингиси":
        await state.update_data({
            "qoshimchaMalumot": ""
        })
        await state.set_state(BuxoroYerSotish.qoshimchaMalumot)
    else:
        await state.set_state(BuxoroYerSotish.qoshimchaMalumot)

# ==============================================================

@buxoro_yer_router.message(BuxoroYerSotish.qoshimchaMalumot)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "qoshimchaMalumot": text
    })
    await message.answer(text=hujjatlaribormiyoz, reply_markup=documentButton, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.hujjatlar)


# =================================================================
    
@buxoro_yer_router.callback_query(DocumentHaveData.filter(F.word=="dokumentbor"), BuxoroYerSotish.hujjatlar)
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Бор,  қонуний"
    # await callback_query.answer("Dokument bor")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=valyutayoz,
                           reply_markup=valyutaButton, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.valyuta)


@buxoro_yer_router.callback_query(DocumentNotData.filter(F.word=="dokumentyoq"), BuxoroYerSotish.hujjatlar)
async def dokumentlar(callback_query: types.CallbackQuery, state: FSMContext):
    text = "Тайёр эмас"
    # await callback_query.answer("Dokument Yo'q")

    await state.update_data({
        "hujjatlar": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=valyutayoz,
                           reply_markup=valyutaButton, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.valyuta)    

# =================================================================
    

@buxoro_yer_router.callback_query(USDData.filter(F.word=="usd"), BuxoroYerSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: USDData):
    text = " $"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.narxi)


@buxoro_yer_router.callback_query(SUMData.filter(F.word=="sum"), BuxoroYerSotish.valyuta)
async def kvartira(callback_query: types.CallbackQuery, state: FSMContext, callback_data: SUMData):
    text = " сўм"
    # await callback_query.answer("Pressed")

    await state.update_data({
        "valyuta": text
    })

    await bot.send_message(chat_id=callback_query.message.chat.id, text=narxiyoz,
                                reply_markup=types.ReplyKeyboardRemove(), parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.narxi)


# ===============================================================

@buxoro_yer_router.message(lambda message: message.text and not message.text.replace('.', '').replace(',', '').isdigit(),
                    BuxoroYerSotish.narxi)
async def check_narxi(message: types.Message):
    await message.reply(faqatRaqamyoz)


@buxoro_yer_router.message(BuxoroYerSotish.narxi)
async def kvartira_narxi(message: types.Message, state: FSMContext):
    msg = int(message.text)

    number = "{:,}".format(msg).replace(",", ".")

    await state.update_data({
        "narxi": number
    })

    await message.answer(text=manzilyoz, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.manzil)


@buxoro_yer_router.message(BuxoroYerSotish.manzil)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "manzil": text
    })
    await message.answer(text=moljalyoz, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.moljal)


@buxoro_yer_router.message(BuxoroYerSotish.moljal)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "moljal": text
    })
    await message.answer(text=telraqam1yoz, parse_mode="HTML")

    await state.set_state(BuxoroYerSotish.telNumberOne)


@buxoro_yer_router.message(BuxoroYerSotish.telNumberOne)
async def umumiyMaydon(message: types.Message, state: FSMContext):
    telNumber = message.text

    await state.update_data({
        "telNumberOne": telNumber
    })

    await message.answer(text=telraqam2yoz, reply_markup=otkazishButton, parse_mode="HTML")
    if message.text == "⏭️ Кейингиси":
        await state.update_data({
            "telNumberTwo": ""
        })
        await state.set_state(BuxoroYerSotish.telNumberTwo)
    else:
        await state.set_state(BuxoroYerSotish.telNumberTwo)


@buxoro_yer_router.message(BuxoroYerSotish.telNumberTwo)
async def telNumbertwo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        "telNumberTwo": text
    })

    chat_id = message.chat.id
    media_group = MediaGroupBuilder()

    data = await state.get_data()

    photos = data['images']

    if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        photo_obj = await build_collage_or_photo(bot, photos)
        sent = await bot.send_photo(chat_id=chat_id, photo=photo_obj, caption=cyrillic_text, parse_mode="HTML")
        if sent.photo:
            await state.update_data({"collage_file_id": sent.photo[-1].file_id})
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroYerSotish.check)
    elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        photo_obj = await build_collage_or_photo(bot, photos)
        sent = await bot.send_photo(chat_id=chat_id, photo=photo_obj, caption=cyrillic_text, parse_mode="HTML")
        if sent.photo:
            await state.update_data({"collage_file_id": sent.photo[-1].file_id})
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroYerSotish.check)

    elif data['telNumberTwo'] == "⏭️ Кейингиси":
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

        result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data11, data12, data13, data14, data15]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        photo_obj = await build_collage_or_photo(bot, photos)
        sent = await bot.send_photo(chat_id=chat_id, photo=photo_obj, caption=cyrillic_text, parse_mode="HTML")
        if sent.photo:
            await state.update_data({"collage_file_id": sent.photo[-1].file_id})
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroYerSotish.check)

    else:
        data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
        data9 = "♦️ "
        gaz = data['gaz']
        svet = data['svet']
        suv = data['suv']
        kanal = data['kanal']
        data10 = " бор\n"
        document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
        data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
        data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
        data13 = "📌 Манзил: " + data['manzil'] + "\n"
        data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
        data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
        data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

        result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                  data11, data12, data13, data14, data15, data16]

        array = []

        for item in result:
            if item == "doesnotexist":
                continue

            array.append(item)

        stringify = "".join(array)
        cyrillic_text = to_cyrillic(stringify)

        photo_obj = await build_collage_or_photo(bot, photos)
        sent = await bot.send_photo(chat_id=chat_id, photo=photo_obj, caption=cyrillic_text, parse_mode="HTML")
        if sent.photo:
            await state.update_data({"collage_file_id": sent.photo[-1].file_id})
        await bot.send_message(chat_id=chat_id, text=check_text, reply_markup=checkbtn, parse_mode="HTML")
        await state.set_state(BuxoroYerSotish.check)


@buxoro_yer_router.message(BuxoroYerSotish.check)
async def check(message: types.Message, state: FSMContext, bot: Bot):
    mycheck = message.text
    chat_id = message.chat.id

    media_group = MediaGroupBuilder()

    if mycheck == "✅ Эълонни жойлаш":
        data = await state.get_data()
        photos = data['images']

        if data['qoshimchaMalumot'] == "⏭️ Кейингиси" and data['telNumberTwo'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            collage_id = data.get("collage_file_id") or photos[0]
            printer = await bot.send_photo(chat_id=group_id, photo=collage_id, caption=cyrillic_text, parse_mode="HTML")

            message_id = str(printer.message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str([collage_id]), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 

        elif data['qoshimchaMalumot'] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            collage_id = data.get("collage_file_id") or photos[0]
            printer = await bot.send_photo(chat_id=group_id, photo=collage_id, caption=cyrillic_text, parse_mode="HTML")

            message_id = str(printer.message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str([collage_id]), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 
        elif data["telNumberTwo"] == "⏭️ Кейингиси":
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n\n"

            result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data11, data12, data13, data14, data15]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            collage_id = data.get("collage_file_id") or photos[0]
            printer = await bot.send_photo(chat_id=group_id, photo=collage_id, caption=cyrillic_text, parse_mode="HTML")

            message_id = str(printer.message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str([collage_id]), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 
        else:
            data3 = "♦️ Умумий майдон: " + data['umumiyMaydon'] + "-сотих" + "\n"
            data9 = "♦️ "
            gaz = data['gaz']
            svet = data['svet']
            suv = data['suv']
            kanal = data['kanal']
            data10 = " бор\n"
            document = "♦️ Ҳужжатлари: " + data['hujjatlar'] + "\n"
            data11 = "♦️ Қўшимча маълумот: " + data['qoshimchaMalumot'] + "\n\n"
            data12 = "💲 Нархи: " + data['narxi'] + data['valyuta'] + "\n\n"
            data13 = "📌 Манзил: " + data['manzil'] + "\n"
            data14 = "📌 Мўлжал: " + data['moljal'] + "\n\n"
            data15 = "☎️ Тел: " + data['telNumberOne'] + "\n"
            data16 = "☎️ Тел: " + data['telNumberTwo'] + "\n\n"

            result = [buxororegion, data2, data3, data9, gaz, svet, suv, kanal, data10, document,
                      data11, data12, data13, data14, data15, data16]

            array = []

            for item in result:
                if item == "doesnotexist":
                    continue

                array.append(item)

            stringify = "".join(array)
            cyrillic_text = to_cyrillic(stringify)+data32+data33+data34+data35

            collage_id = data.get("collage_file_id") or photos[0]
            printer = await bot.send_photo(chat_id=group_id, photo=collage_id, caption=cyrillic_text, parse_mode="HTML")

            message_id = str(printer.message_id)
            userId = str(message.chat.id)
            await db.add_yer_data(user_id=userId, photos=str([collage_id]), captions=cyrillic_text, message_id=message_id)

            await bot.send_message(chat_id=group_id, text="Буйруқ Беринг", reply_markup=buxoro_group)
            await bot.send_message(chat_id=chat_id, text=success_text, reply_markup=start, parse_mode="HTML")
            await state.clear() 
    if mycheck == "❌ Эълонни қайтадан ёзиш":
        await bot.send_message(chat_id=chat_id, text="<b>❌ Эълон қабул қилинмади</b>", parse_mode="HTML")
        await bot.send_message(chat_id=chat_id, text="<b>Еълон бериш учун қайтадан уриниб кўринг</b>", reply_markup=start, parse_mode="HTML")
        await state.clear()


@buxoro_yer_router.callback_query(IsGroupCall(), TasdiqlashBuxoro.filter(F.word == "buxorotasdiqlash"))
async def dokumentlar(call: types.CallbackQuery, state: FSMContext):
    chat_id = str(call.message.message_id - 1)

    media_group = MediaGroupBuilder()

    data = await db.yer_get_one_user_data(message_id=chat_id)
    if not data:
        if call.message:
            await bot.send_message(chat_id=call.message.chat.id, text="Xatolik mavjud.")
        return

    photos_string = data['photos']
    try:
        photos_list = ast.literal_eval(photos_string) if photos_string.startswith('[') else [photos_string]
        photo_id = photos_list[0]
    except (ValueError, SyntaxError):
        photo_id = photos_string

    await bot.send_photo(chat_id=buxoro_id, photo=photo_id, caption=data['captions'], reply_markup=elon_inline_button, parse_mode="HTML")
    await bot.send_message(chat_id=int(data['user_id']), text=success_message)
    await bot.send_message(chat_id=call.message.chat.id, text=success_message)
    


@buxoro_yer_router.callback_query(IsGroupCall(), BekorQilishBuxoro.filter(F.word=="buxorobekor"))
async def dokumentlar(call: types.CallbackQuery, state: FSMContext):

    chat_id = str(call.message.message_id - 1)


    data = await db.yer_get_one_user_data(message_id=chat_id)

    await bot.send_message(chat_id=int(data['user_id']), text=fail_message)
    await bot.send_message(chat_id=call.message.chat.id, text=fail_message)