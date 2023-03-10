from aiogram import types, Dispatcher
from config_data import config


async def process_help_command(message: types.Message):
    await message.answer(text=config.default_commands)


def register_handler_help(dp: Dispatcher):
    """information about bot commands"""
    dp.register_message_handler(process_help_command, commands=["help"])
