from aiogram.types import CallbackQuery
from aiogram import Dispatcher
from aiogram_calendar import DialogCalendar
from site_api.list_hotels import payload
from state import ClientState


async def process_callback_location(callback: CallbackQuery):

    """accepts the location selected by the user"""

    await callback.message.edit_text(text="Выберите дату въезда",
                                     reply_markup=await DialogCalendar().start_calendar())
    await ClientState.request_date_in.set()

    payload["destination"]["regionId"] = callback.data


def register_handler_callback_location(dp: Dispatcher):
    dp.register_callback_query_handler(process_callback_location, state=ClientState.request_location)