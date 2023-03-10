from aiogram.types import Message
from aiogram.dispatcher import Dispatcher


async def process_message_no_state(message: Message):

    """sends clarifying information when sending messages without state"""

    await message.answer(text="Введите /start для поиска отелей\n/help информация по командам бота")


def register_handler_no_state_message(dp: Dispatcher):
    dp.register_message_handler(process_message_no_state)

