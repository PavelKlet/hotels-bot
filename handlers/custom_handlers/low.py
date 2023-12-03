from datetime import datetime

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import Dispatcher, FSMContext
from state import ClientState
from site_api.list_hotels import payload


async def process_low(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data["command"] = "/low"
        data["datetime"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    await message.answer(text="Введите интересующий вас город", reply_markup=ReplyKeyboardRemove())
    payload["filters"] = {"price": {
        "max": 250,
        "min": 1
    }}
    await ClientState.request_location.set()


def register_handler_low(dp: Dispatcher):
    dp.register_message_handler(process_low, commands=["low"])
