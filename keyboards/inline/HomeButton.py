from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.data import StartData, AndijonData, BuxoroData, FargonaData, JizzaxData, \
    NamanganData, NavoiyData, QashqadaryoData, QoraqalpoqData, SamarqandData, SirdaryoData, \
    SurxondaryoData, toshkentshData, toshkentvilData, XorazmData

from keyboards.inline.data import AndijonHovliData, BuxoroHovliData, FargonaHovliData, JizzaxHovliData, \
    NamanganHovliData, NavoiyHovliData, QashqaHovliData, QoraqalpoqHovliData, SamarqandHovliData, \
    SirdaryoHovliData, SurxonHovliData, ToshketnShHovliData, ToshkentVilHovliData, XorazmHovliData

from keyboards.inline.data import AndijonKvartiraData, BuxoroKvartiraData, FargonaKvartiraData, \
    JizzaxKvartiraData, NamanganKvartiraData, NavoiyKvartiraData, QashqaKvartiraData, \
    QoraqalpoqKvartiraData, SamarqandKvartiraData, SirdaryoKvartiraData, SurxonKvartiraData, \
    ToshketnShKvartiraData, ToshkentVilKvartiraData, XorazmKvartiraData

from keyboards.inline.data import AndijonYerData, BuxoroYerData, FargonaYerData, \
    JizzaxYerData, NamanganYerData, NavoiyYerData, QashqaYerData, \
    QoraqalpoqYerData, SamarqandYerData, SirdaryoYerData, SurxonYerData, \
    ToshketnShYerData, ToshkentVilYerData, XorazmYerData

from keyboards.inline.data import YoqData, BorData
from keyboards.inline.data import YevroremontData, TamirlangantData, OrtachaData, TamirsizData
from keyboards.inline.data import MavjudData, JihozlarsizData
from keyboards.inline.data import USDData, SUMData
from keyboards.inline.data import DocumentHaveData, DocumentNotData
from keyboards.inline.data import GoBackData

from keyboards.inline.data import TasdiqlashAndijon, TasdiqlashBuxoro, TasdiqlashFargona, TasdiqlashJizzax, \
      TasdiqlashNamangan, TasdiqlashNavoiy, TasdiqlashQashqa, TasdiqlashQoraqalpoq, TasdiqlashSamarqand, \
      TasdiqlashSirdaryo, TasdiqlashSurxon, TasdiqlashToshsh, TasdiqlashToshvil, TasdiqlashXorazm
from keyboards.inline.data import BekorQilishAndijon, BekorQilishBuxoro, BekorQilishFargona, \
      BekorQilishJizzax, BekorQilishNamangan, BekorQilishNavoiy, BekorQilishQashqa, BekorQilishQoraqalpoq, \
      BekorQilishSamarqand, BekorQilishSirdaryo, BekorQilishSurxon, BekorQilishToshsh, BekorQilishToshvil, \
      BekorQilishXorazm

from keyboards.inline.data import AdminXabarYuborish

allRegionsKvartira = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                          inline_keyboard=[
                                              [InlineKeyboardButton(text="Тошкент шаҳар", callback_data=toshkentshData(word="toshkent").pack()),
                                               InlineKeyboardButton(text="Тошкент вилояти",
                                                                    callback_data=toshkentvilData(word="toshkentvil").pack())],
                                              [InlineKeyboardButton(text="Андижон", callback_data=AndijonData(word="andijon").pack()),
                                               InlineKeyboardButton(text="Наманган", callback_data=NamanganData(word="namangan").pack())],
                                              [InlineKeyboardButton(text="Фарғона", callback_data=FargonaData(word="fargona").pack()),
                                               InlineKeyboardButton(text="Самарқанд", callback_data=SamarqandData(word="samarqand").pack())],
                                              [InlineKeyboardButton(text="Бухоро", callback_data=BuxoroData(word="buxoro").pack()),
                                               InlineKeyboardButton(text="Сирдарё", callback_data=SirdaryoData(word="sirdaryo").pack())],
                                              [InlineKeyboardButton(text="Қашқадарё", callback_data=QashqadaryoData(word="qashqa").pack()),
                                               InlineKeyboardButton(text="Сурхoндарё", callback_data=SurxondaryoData(word="surxon").pack())],
                                              [InlineKeyboardButton(text="Навоий", callback_data=NavoiyData(word="navoiy").pack()),
                                               InlineKeyboardButton(text="Жиззах", callback_data=JizzaxData(word="jizzax").pack())],
                                              [InlineKeyboardButton(text="Хоразм", callback_data=XorazmData(word="xorazm").pack()),
                                               InlineKeyboardButton(text="Қорақалпоғистон",
                                                                    callback_data=QoraqalpoqData(word="qora").pack())],
                                          ])


toshkentShHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Квартира", callback_data=ToshketnShKvartiraData(word="toshshkv").pack()),
                                           InlineKeyboardButton(text="Ховли Участка", callback_data=ToshketnShHovliData(word="toshshhovli").pack())],
                                          [InlineKeyboardButton(text="Қуруқ Ер", callback_data=ToshketnShYerData(word="toshshyer").pack())]
                                      ])

toshkentVilHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text="Квартира", callback_data=ToshkentVilKvartiraData(word="toshvilkv").pack()),
                                            InlineKeyboardButton(text="Ховли Участка", callback_data=ToshkentVilHovliData(word="toshvilhovli").pack())],
                                           [InlineKeyboardButton(text="Қуруқ Ер", callback_data=ToshkentVilYerData(word="toshvilyer").pack())]
                                       ])

andijonHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="Квартира", callback_data=AndijonKvartiraData(word="andijonkv").pack()),
                                        InlineKeyboardButton(text="Ховли Участка", callback_data=AndijonHovliData(word="andijonhovli").pack())],
                                       [InlineKeyboardButton(text="Қуруқ Ер", callback_data=AndijonYerData(word="andijonyer").pack())]
                                   ])

namanganHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Квартира", callback_data=NamanganKvartiraData(word="namangankv").pack()),
                                         InlineKeyboardButton(text="Ховли Участка", callback_data=NamanganHovliData(word="namanganhovli").pack())],
                                        [InlineKeyboardButton(text="Қуруқ Ер", callback_data=NamanganYerData(word="namanganyer").pack())]
                                    ])

fargonaHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="Квартира", callback_data=FargonaKvartiraData(word="fargonakv").pack()),
                                        InlineKeyboardButton(text="Ховли Участка", callback_data=FargonaHovliData(word="fargonahovli").pack())],
                                       [InlineKeyboardButton(text="Қуруқ Ер", callback_data=FargonaYerData(word="fargonayer").pack())]
                                   ])

samarqandHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text="Квартира", callback_data=SamarqandKvartiraData(word="samarqandkv").pack()),
                                          InlineKeyboardButton(text="Ховли Участка", callback_data=SamarqandHovliData(word="samarqandhovli").pack())],
                                         [InlineKeyboardButton(text="Қуруқ Ер", callback_data=SamarqandYerData(word="samarqandyer").pack())]
                                     ])

buxoroHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=BuxoroKvartiraData(word="buxorokv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=BuxoroHovliData(word="buxorohovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=BuxoroYerData(word="buxoroyer").pack())]
                                  ])

sirdaryoHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Квартира", callback_data=SirdaryoKvartiraData(word="sirdaryokv").pack()),
                                         InlineKeyboardButton(text="Ховли Участка", callback_data=SirdaryoHovliData(word="sirdaryohovli").pack())],
                                        [InlineKeyboardButton(text="Қуруқ Ер", callback_data=SirdaryoYerData(word="sirdaryoyer").pack())]
                                    ])

qashqadaryoHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                       inline_keyboard=[
                                           [InlineKeyboardButton(text="Квартира", callback_data=QashqaKvartiraData(word="qashqakv").pack()),
                                            InlineKeyboardButton(text="Ховли Участка", callback_data=QashqaHovliData(word="qashqadaryohovli").pack())],
                                           [InlineKeyboardButton(text="Қуруқ Ер", callback_data=QashqaYerData(word="qashqayer").pack())]
                                       ])

surxonHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=SurxonKvartiraData(word="surxonkv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=SurxonHovliData(word="surxonhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=SurxonYerData(word="surxonyer").pack())]
                                  ])

navoiyHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=NavoiyKvartiraData(word="navoiykv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=NavoiyHovliData(word="navoiyhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=NavoiyYerData(word="navoiyyer").pack())]
                                  ])

jizzaxHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=JizzaxKvartiraData(word="jizzaxkv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=JizzaxHovliData(word="jizzaxhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=JizzaxYerData(word="jizzaxyer").pack())]
                                  ])

xorazmHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Квартира", callback_data=XorazmKvartiraData(word="xorazmkv").pack()),
                                       InlineKeyboardButton(text="Ховли Участка", callback_data=XorazmHovliData(word="xorazmhovli").pack())],
                                      [InlineKeyboardButton(text="Қуруқ Ер", callback_data=XorazmYerData(word="xorazmyer").pack())]
                                  ])

qoraqalpoqHome = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Квартира", callback_data=QoraqalpoqKvartiraData(word="qoraqalpoqkv").pack()),
                                           InlineKeyboardButton(text="Ховли Участка", callback_data=QoraqalpoqHovliData(word="qoraqalpoqhovli").pack())],
                                          [InlineKeyboardButton(text="Қуруқ Ер", callback_data=QoraqalpoqYerData(word="qoraqalpoqyer").pack())],
                                      ])

# =========================================================================================

borYoq = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text="✅ Бор", callback_data=BorData(word="bor").pack()),
                                   InlineKeyboardButton(text="❌ Йўқ", callback_data=YoqData(word="yoq").pack())]
                              ])

remontButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="Евроремонт", callback_data=YevroremontData(word="yevroremont").pack())],
                                        [InlineKeyboardButton(text="Таъмирланган", callback_data=TamirlangantData(word="tamirlangan").pack())],
                                        [InlineKeyboardButton(text="Ўртача", callback_data=OrtachaData(word="ortacha").pack())],
                                        [InlineKeyboardButton(text=" Таъмирсиз", callback_data=TamirsizData(word="tamirsiz").pack())]
                                    ])

jihozlarButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Бор", callback_data=MavjudData(word="mavjud").pack())],
                                          [InlineKeyboardButton(text="Йўқ", callback_data=JihozlarsizData(word="jihozlarsiz").pack())]
                                      ])

valyutaButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                     inline_keyboard=[
                                         [InlineKeyboardButton(text="$", callback_data=USDData(word="usd").pack())],
                                         [InlineKeyboardButton(text="сўм", callback_data=SUMData(word="sum").pack())]
                                     ])

documentButton = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Бор,  қонуний", callback_data=DocumentHaveData(word="dokumentbor").pack())],
                                          [InlineKeyboardButton(text="Тайёр эмас", callback_data=DocumentNotData(word="dokumentyoq").pack())]
                                      ])

import config

link_button = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                   inline_keyboard=[
                                       [InlineKeyboardButton(text="✍️ ЭЪЛОН БЕРИШ", url=f"https://t.me/{getattr(config, 'BOT_USERNAME', 'demo_bot_2022Bot')}")]
                                   ])

elon_inline_button = InlineKeyboardMarkup(resize_keyboard=True, row_width=1,
                                          inline_keyboard=[
                                              [InlineKeyboardButton(text="✍️ ЭЪЛОН БЕРИШ", url=f"https://t.me/{getattr(config, 'BOT_USERNAME', 'demo_bot_2022Bot')}")]
                                          ])

start_button = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    inline_keyboard=[
                                        [InlineKeyboardButton(text="бошидан ёзиш",
                                                              callback_data=StartData(word="start").pack())]
                                    ])

admin = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                             inline_keyboard=[
                                  [InlineKeyboardButton(text="Barcha kanallarga xabar yuborish", callback_data=AdminXabarYuborish(word="AdminXabar").pack())]
                             ]) 

# ==============================================================================

andijon_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashAndijon(word=f"andijontasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishAndijon(word=f"andijonbekor").pack())]])

buxoro_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashBuxoro(word=f"buxorotasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishBuxoro(word=f"buxorobekor").pack())]])
fargona_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashFargona(word=f"fargonatasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishFargona(word=f"fargonabekor").pack())]])
jizzax_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashJizzax(word=f"jizzaxtasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishJizzax(word=f"jizzaxbekor").pack())]])
namangan_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashNamangan(word=f"namangantasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishNamangan(word=f"namanganbekor").pack())]])
navoiy_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashNavoiy(word=f"navoiytasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishNavoiy(word=f"navoiybekor").pack())]])

qashqa_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashQashqa(word=f"qashqatasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishQashqa(word=f"qashqabekor").pack())]])

qoraqalpoq_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashQoraqalpoq(word=f"qoraqalpoqtasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishQoraqalpoq(word=f"qoraqalpoqbekor").pack())]])

samarqand_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashSamarqand(word=f"samarqandtasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishSamarqand(word=f"samarqandbekor").pack())]])

sirdaryo_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashSirdaryo(word=f"sirdaryotasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishSirdaryo(word=f"sirdaryobekor").pack())]])

surxon_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashSurxon(word=f"surxontasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishSurxon(word=f"surxonbekor").pack())]])

toshsh_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashToshsh(word=f"toshshtasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishToshsh(word=f"toshshbekor").pack())]])

toshvil_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashToshvil(word=f"toshviltasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishToshvil(word=f"toshvilbekor").pack())]])

xorazm_group = InlineKeyboardMarkup(resize_keyboard=True, row_width=2,
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text="Тасдиқлаш", callback_data=TasdiqlashXorazm(word=f"xorazmtasdiqlash").pack()), 
                                           InlineKeyboardButton(text="Бекор Қилиш", callback_data=BekorQilishXorazm(word=f"xorazmbekor").pack())]])