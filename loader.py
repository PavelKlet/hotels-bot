from aiogram import Dispatcher, Bot

from state import storage

from config_data.config import BOT_TOKEN, RAPID_API_TOKEN, POSTGRES_URI

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

