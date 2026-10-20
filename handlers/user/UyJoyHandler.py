from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from keyboards.inline.HomeButton import (
    allRegionsKvartira, toshkentShHome, toshkentVilHome,
    andijonHome, namanganHome, fargonaHome, samarqandHome, buxoroHome, sirdaryoHome, qashqadaryoHome,
    surxonHome, navoiyHome, jizzaxHome, xorazmHome, qoraqalpoqHome
)

from keyboards.inline.data import (
    AndijonData, BuxoroData, FargonaData, JizzaxData, NamanganData,
    NavoiyData, QashqadaryoData, QoraqalpoqData, SamarqandData, SirdaryoData, SurxondaryoData,
    toshkentshData, toshkentvilData, XorazmData
)

uyJoy_router = Router()

# =======================================1=======================================
@uyJoy_router.callback_query(AndijonData.filter(F.word == "andijon"))
async def andijon_tanlandi(call: CallbackQuery, callback_data: AndijonData):
    await call.answer("Andijon tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=andijonHome, parse_mode="HTML")

# =======================================2========================================
@uyJoy_router.callback_query(BuxoroData.filter(F.word == "buxoro"))
async def buxoro_tanlandi(call: CallbackQuery, callback_data: BuxoroData):
    await call.answer("Buxoro tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=buxoroHome, parse_mode="HTML")

# =======================================3========================================
@uyJoy_router.callback_query(FargonaData.filter(F.word == "fargona"))
async def fargona_tanlandi(call: CallbackQuery, callback_data: FargonaData):
    await call.answer("Farg'ona tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=fargonaHome, parse_mode="HTML")

# =======================================4========================================
@uyJoy_router.callback_query(JizzaxData.filter(F.word == "jizzax"))
async def jizzax_tanlandi(call: CallbackQuery, callback_data: JizzaxData):
    await call.answer("Jizzax tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=jizzaxHome, parse_mode="HTML")

# =======================================5========================================
@uyJoy_router.callback_query(NamanganData.filter(F.word == "namangan"))
async def namangan_tanlandi(call: CallbackQuery, callback_data: NamanganData):
    await call.answer("Namangan tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=namanganHome, parse_mode="HTML")

# =======================================6========================================
@uyJoy_router.callback_query(NavoiyData.filter(F.word == "navoiy"))
async def navoiy_tanlandi(call: CallbackQuery, callback_data: NavoiyData):
    await call.answer("Navoiy tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=navoiyHome, parse_mode="HTML")

# =======================================7========================================
@uyJoy_router.callback_query(QashqadaryoData.filter(F.word == "qashqa"))
async def qashqadaryo_tanlandi(call: CallbackQuery, callback_data: QashqadaryoData):
    await call.answer("Qashqadaryo tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=qashqadaryoHome, parse_mode="HTML")

# =======================================8========================================
@uyJoy_router.callback_query(QoraqalpoqData.filter(F.word == "qora"))
async def qoraqalpoq_tanlandi(call: CallbackQuery, callback_data: QoraqalpoqData):
    await call.answer("Qoraqalpog'iston tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=qoraqalpoqHome, parse_mode="HTML")

# =======================================9========================================
@uyJoy_router.callback_query(SamarqandData.filter(F.word == "samarqand"))
async def samarqand_tanlandi(call: CallbackQuery, callback_data: SamarqandData):
    await call.answer("Samarqand tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=samarqandHome, parse_mode="HTML")

# =======================================10========================================
@uyJoy_router.callback_query(SirdaryoData.filter(F.word == "sirdaryo"))
async def sirdaryo_tanlandi(call: CallbackQuery, callback_data: SirdaryoData):
    await call.answer("Sirdaryo tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=sirdaryoHome, parse_mode="HTML")

# =======================================11========================================
@uyJoy_router.callback_query(SurxondaryoData.filter(F.word == "surxon"))
async def surxondaryo_tanlandi(call: CallbackQuery, callback_data: SurxondaryoData):
    await call.answer("Surxondaryo tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=surxonHome, parse_mode="HTML")

# =======================================12========================================
@uyJoy_router.callback_query(toshkentshData.filter(F.word == "toshkent"))
async def toshkentsh_tanlandi(call: CallbackQuery, callback_data: toshkentshData):
    await call.answer("Toshkent Shahar tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=toshkentShHome, parse_mode="HTML")

# =======================================13========================================
@uyJoy_router.callback_query(toshkentvilData.filter(F.word == "toshkentvil"))
async def toshkentvil_tanlandi(call: CallbackQuery, callback_data: toshkentvilData):
    await call.answer("Toshkent Viloyati tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=toshkentVilHome, parse_mode="HTML")

# =======================================14========================================
@uyJoy_router.callback_query(XorazmData.filter(F.word == "xorazm"))
async def xorazm_tanlandi(call: CallbackQuery, callback_data: XorazmData):
    await call.answer("Xorazm tanlandi")
    if isinstance(call.message, Message):
        await call.message.answer("<b> Уй-жой турини танланг  </b>", reply_markup=xorazmHome, parse_mode="HTML")

# ===================================--finish--=====================================
