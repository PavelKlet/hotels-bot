from datetime import datetime

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import Dispatcher, FSMContext
from state import ClientState
from site_api.list_hotels import payload, user_info


async def process_high(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data["command"] = "/high"
        data["datetime"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    await message.answer(text="Введите интересующий вас город", reply_markup=ReplyKeyboardRemove())
    payload["filters"] = {"price": {
        "max": 9000,
        "min": 250
    }}
    user_info["high"] = True
    await ClientState.request_location.set()


def register_handler_high(dp: Dispatcher):
    dp.register_message_handler(process_high, commands=["high"])
