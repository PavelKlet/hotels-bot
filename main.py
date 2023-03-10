from aiogram.utils import executor

from loader import dp, POSTGRES_URI

from handlers import (help, start, message, callback_location,
                      callback_date, low, callback_hotels_and_photo, switch_hotels, high, photo_hotels, bestdeal,
                      no_state_message, history)
from database.db_gino import db


async def start_up(_):
    print("Установка связи с postgresql")
    await db.set_bind(POSTGRES_URI)


if __name__ == '__main__':

    start.register_handler_start(dp)
    help.register_handler_help(dp)
    low.register_handler_low(dp)
    high.register_handler_high(dp)
    bestdeal.register_handler_bestdeal(dp)
    history.register_handler_history(dp)
    no_state_message.register_handler_no_state_message(dp)
    message.register_handler_message(dp)
    callback_location.register_handler_callback_location(dp)
    callback_date.register_handler_callback_date(dp)
    callback_hotels_and_photo.register_handler_callback_quantity(dp)
    switch_hotels.register_handler_switch(dp)
    photo_hotels.register_handler_switch_photos(dp)

    executor.start_polling(dp, on_startup=start_up)
