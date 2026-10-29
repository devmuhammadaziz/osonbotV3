from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

send_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                   keyboard=[
                                        [KeyboardButton(text='☎️ Телефон рақамни тасдиқлаш', request_contact=True)]
                                   ])

button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                             keyboard=[
                                 [KeyboardButton(text="УЙ-ЖОЙ БОЗОРИ")],
                             ])

start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True, is_persistent=True,
                             keyboard=[
                                 [KeyboardButton(text="START")],
                             ])


checkbtn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,one_time_keyboard=True, is_persistent=True,
                               keyboard=[
                                   [KeyboardButton(text="✅ Эълонни жойлаш"),
                                    KeyboardButton(text="❌ Эълонни қайтадан ёзиш")],
                               ])

newbutton = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [KeyboardButton(text="🛑 Bekor qilish")]
                                ])

otkazishButton = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                     keyboard=[
                                         [KeyboardButton(text="⏭️ Кейингиси")],
                                     ])

homeTypes = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                                keyboard=[
                                    [KeyboardButton(text="Квартира"), KeyboardButton(text="Ҳовли Участка")],
                                    [KeyboardButton(text="Қуруқ Ер"), KeyboardButton(text="Дача")],
                                    [KeyboardButton(text="⬅️ Ортга")],
                                ])

homeTypesRent = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                                    keyboard=[
                                        [KeyboardButton(text="Квартира"), KeyboardButton(text="Ҳовли уй")],
                                        [KeyboardButton(text="⬅️ Ортга")],
                                    ])


homeTypeAllRegions = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3,
                                         keyboard=[
                                             [KeyboardButton(text="Regions"), KeyboardButton(text="Regions")]
                                         ])

