from handlers.user.start import user_router
from handlers.user.UyJoyHandler import uyJoy_router


# hovli
from handlers.user.HovliSotish.AndijonHandler import andijon_router
from handlers.user.HovliSotish.BuxoroHandler import buxoro_router
from handlers.user.HovliSotish.FargonaHandler import fargona_router
from handlers.user.HovliSotish.JizzaxHandler import jizzax_router
from handlers.user.HovliSotish.NamanganHandler import namangan_router
from handlers.user.HovliSotish.NavoiyHandler import navoiy_router
from handlers.user.HovliSotish.QashqadaryoHandler import qashqa_router
from handlers.user.HovliSotish.QoraqalpoqHandler import qoraqaloq_router
from handlers.user.HovliSotish.SamarqandHandler import samarqand_router
from handlers.user.HovliSotish.SirdaryoHandler import sirdaryo_router
from handlers.user.HovliSotish.SurxondaryoHandler import surxon_router
from handlers.user.HovliSotish.ToshkentShHandler import toshsh_router
from handlers.user.HovliSotish.ToshkentVilHandler import toshvil_router
from handlers.user.HovliSotish.XorazmHandler import xorazm_router




# kvartira
from handlers.user.KvartiraSotish.AndijonHandler import andijon_kv_router
from handlers.user.KvartiraSotish.BuxoroHandler import buxoro_kv_router
from handlers.user.KvartiraSotish.FargonaHandler import fargona_kv_router
from handlers.user.KvartiraSotish.JizzaxHandler import jizzax_kv_router
from handlers.user.KvartiraSotish.NamanganHandler import namangan_kv_router
from handlers.user.KvartiraSotish.NavoiyHandler import navoiy_kv_router
from handlers.user.KvartiraSotish.QashqadaryoHandler import qashqa_kv_router
from handlers.user.KvartiraSotish.QoraqalpoqHandler import qoraqalpoq_kv_router
from handlers.user.KvartiraSotish.SamarqandHandler import samarqand_kv_router
from handlers.user.KvartiraSotish.SirdaryoHandler import sirdaryo_kv_router
from handlers.user.KvartiraSotish.SurxondaryoHandler import surxon_kv_router
from handlers.user.KvartiraSotish.ToshkentShHandler import toshsh_kv_router
from handlers.user.KvartiraSotish.ToshkentVilHandler import toshvil_kv_router
from handlers.user.KvartiraSotish.XorazmHandler import xorazm_kv_router


# yer
from handlers.user.YerSotish.AndijonHandler import andijon_yer_router
from handlers.user.YerSotish.BuxoroHandler import buxoro_yer_router
from handlers.user.YerSotish.FargonaHandler import fargona_yer_router
from handlers.user.YerSotish.JizzaxHandler import jizzax_yer_router
from handlers.user.YerSotish.NamanganHandler import namangan_yer_router
from handlers.user.YerSotish.NavoiyHandler import navoiy_yer_router
from handlers.user.YerSotish.QashqadaryoHandler import qashqa_yer_router
from handlers.user.YerSotish.QoraqalpoqHandler import qoraqalpoq_yer_router
from handlers.user.YerSotish.SamarqandHandler import samarqand_yer_router
from handlers.user.YerSotish.SirdaryoHandler import sirdaryo_yer_router
from handlers.user.YerSotish.SurxondaryoHandler import surxon_yer_router
from handlers.user.YerSotish.ToshkentShHandler import toshsh_yer_router
from handlers.user.YerSotish.ToshkentVilHandler import toshvil_yer_router
from handlers.user.YerSotish.XorazmHandler import xorazm_yer_router


from handlers.groups.sendMessage import group_router

from aiogram import Router
from typing import List

routers: List[Router] = [user_router, uyJoy_router, andijon_router, buxoro_router, \
    fargona_router, jizzax_router, namangan_router, navoiy_router, qashqa_router, \
    qoraqaloq_router, samarqand_router, sirdaryo_router, surxon_router, toshsh_router, \
    toshvil_router, xorazm_router, \
    andijon_kv_router, buxoro_kv_router, fargona_kv_router, jizzax_kv_router, namangan_kv_router, \
    navoiy_kv_router, qashqa_kv_router, qoraqalpoq_kv_router, samarqand_kv_router, sirdaryo_kv_router, \
    surxon_kv_router, toshsh_kv_router, toshvil_kv_router, xorazm_kv_router, \
    andijon_yer_router, buxoro_yer_router, fargona_yer_router, jizzax_yer_router, \
    namangan_yer_router, navoiy_yer_router, qashqa_yer_router, qoraqalpoq_yer_router, \
    samarqand_yer_router, sirdaryo_yer_router, surxon_yer_router, toshsh_yer_router, \
    toshvil_yer_router, xorazm_yer_router, \
    group_router]




def register_handlers(main_router: Router) -> None:
    for router in routers:
        main_router.include_router(router)
