from asyncio import run
from pathlib import Path
from loguru import logger

from handlers import register_handlers
from loader import bot, dp, db
from utils.set_bot_commands import set_default_commands


async def database_connected():
    # Ma'lumotlar bazasiga ulanamiz:
    await db.create()


async def main() -> None:
    base_dir = Path(__file__).resolve().parent
    logger.add(base_dir / 'logs.log', level="INFO")

    register_handlers(dp)

    logger.info('Bot started')
    await set_default_commands(bot)

    await database_connected()
    logger.info("Database connected")

    await dp.start_polling(bot)
    logger.info('Bot stopped')


if __name__ == '__main__':
    run(main())
