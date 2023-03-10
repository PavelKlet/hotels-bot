from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

switch = InlineKeyboardMarkup(row_width=2)

switch.add(InlineKeyboardButton(text="<<Предыдущая", callback_data="prev:0"),
           InlineKeyboardButton(text="Следующая>>", callback_data="next:0")).insert(
    InlineKeyboardButton(text="Выход", callback_data="exit")).add(
    InlineKeyboardButton(text="Фото", callback_data="Фото"))
