from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from keyboards.keyboard_filter import keyboard_filter


async def process_start_command(message: types.Message, state: FSMContext):

    """getting started"""
    await state.finish()
    await message.answer(text="Выберите вариант сортировки\n/help помощь по командам",
                         reply_markup=keyboard_filter)


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"], state="*")
