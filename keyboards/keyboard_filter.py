from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard_filter = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

button_low = KeyboardButton(text="/low")
button_high = KeyboardButton(text="/high")
button_bestdeal = KeyboardButton(text="/bestdeal")

keyboard_filter.add(button_low).add(button_high).add(button_bestdeal)

