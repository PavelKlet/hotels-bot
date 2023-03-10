from datetime import datetime

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import Dispatcher, FSMContext
from state import ClientState
from site_api.list_hotels import payload, user_info


async def process_bestdeal(message: Message, state: FSMContext):

    async with state.proxy() as data:
        data["command"] = "/bestdeal"
        data["datetime"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    await message.answer(text="Введите минимальную цену состоящую из цифр.", reply_markup=ReplyKeyboardRemove())

    await ClientState.request_min_price.set()


async def min_price(message: Message):
    try:
        payload["filters"]["price"]["min"] = int(message.text)
        await message.answer(text="Введите максимальную цену состоящую из цифр.")

        await ClientState.request_max_price.set()

    except ValueError:
        await message.answer("Некорректный ввод, попробуйте ещё раз.")


async def max_price(message: Message):
    try:
        payload["filters"]["price"]["max"] = int(message.text)
        await message.answer("Введите расстояние до центра города в км, пример: 1.70")

        await ClientState.request_distance.set()

    except ValueError:
        await message.answer("Некорректный ввод, попробуйте ещё раз.")


async def distance(message: Message):

    try:
        user_info["distance"] = float(message.text)
        await message.answer(text="Введите интересующий вас город")
        await ClientState.request_location.set()

    except ValueError:
        await message.answer("Некорректный ввод, попробуйте ещё раз.")


def register_handler_bestdeal(dp: Dispatcher):
    dp.register_message_handler(process_bestdeal, commands=["bestdeal"])
    dp.register_message_handler(min_price, state=ClientState.request_min_price)
    dp.register_message_handler(max_price, state=ClientState.request_max_price)
    dp.register_message_handler(distance, state=ClientState.request_distance)
