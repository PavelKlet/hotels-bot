from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_yes_no = InlineKeyboardMarkup(resize_keyboard=True, row_width=3)

keyboard_yes_no.add(InlineKeyboardButton("Да", callback_data="Да"))
keyboard_yes_no.add(InlineKeyboardButton("Нет", callback_data="Нет"))
