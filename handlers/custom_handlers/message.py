from aiogram.types import Message
from aiogram.dispatcher import Dispatcher, FSMContext
from keyboards import location_keyboard
from state import ClientState


async def process_message(message: Message, state: FSMContext):

    """the function that accepts the location"""

    async with state.proxy() as data:
        data["user_id"] = message.from_user.id

    keyboard = await location_keyboard.location_keyboard(message.text)

    if keyboard.inline_keyboard:
        await message.answer(text="Выберите вариант", reply_markup=keyboard)
    else:
        await message.answer(text="Ничего не нашлось")
        await state.finish()


def register_handler_message(dp: Dispatcher):
    dp.register_message_handler(process_message, state=ClientState.request_location)


