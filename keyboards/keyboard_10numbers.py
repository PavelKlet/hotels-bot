from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard_numbers = InlineKeyboardMarkup(resize_keyboard=True, row_width=3)

for button in range(1, 11):
    keyboard_numbers.insert(InlineKeyboardButton(text=str(button), callback_data=str(button)))
