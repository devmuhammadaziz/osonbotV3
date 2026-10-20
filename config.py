from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = [int(admin) for admin in env.list('ADMINS')]

assert BOT_TOKEN is not None, "BOT_TOKEN is not set in environment variables."
assert ADMINS is not None

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
BOT_USERNAME = env.str("BOT_USERNAME", "demo_bot_2022Bot")