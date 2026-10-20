import socket
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from utils.db.postgres import Database

import config

storage = MemoryStorage()

dp = Dispatcher(storage=storage)

db = Database()

# Force IPv4 to avoid timeout hangs on VPS with unrouted IPv6
session = AiohttpSession()
session._connector_init["family"] = socket.AF_INET

bot = Bot(
    token=config.BOT_TOKEN,
    session=session,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

