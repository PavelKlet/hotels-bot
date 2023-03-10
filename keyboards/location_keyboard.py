from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from site_api import location


async def location_keyboard(location_in):
    """

    :param location_in: user location
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    list_location = await location.request_location(location_in)

    for location_info in list_location:
        keyboard.add(InlineKeyboardButton(text=location_info[0], callback_data=location_info[1]))

    return keyboard
