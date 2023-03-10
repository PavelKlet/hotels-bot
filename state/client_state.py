from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()


class ClientState(StatesGroup):
    request_min_price = State()
    request_max_price = State()
    request_distance = State()
    request_location = State()
    request_date_in = State()
    request_date_out = State()
    quantity_hotels = State()
    need_photo = State()
    quantity_photo = State()
    answer = State()



