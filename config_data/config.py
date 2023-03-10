from dotenv import find_dotenv, load_dotenv
import os

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_TOKEN = os.getenv("RAPID_API_TOKEN")

default_commands = """
/start - начать работу бота
/help - список команд
/low - топ самых недорогих отелей
/high - топ самых дорогих отелей
/bestdeal - собственный диапазон цен и расстояние до центра города
/history - история запросов
"""

ip = os.getenv("ip")
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"