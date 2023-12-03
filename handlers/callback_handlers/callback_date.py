from aiogram_calendar import DialogCalendar, dialog_cal_callback
from aiogram.types import CallbackQuery
from aiogram.dispatcher import Dispatcher, FSMContext
from state import ClientState
from site_api.list_hotels import payload
from keyboards import keyboard_10numbers


async def process_dialog_calendar(callback_query: CallbackQuery, callback_data, state: FSMContext):

    selected, date_in_res = await DialogCalendar().process_selection(callback_query, callback_data)

    if selected:
        async with state.proxy() as data:
            data["date_in"] = date_in_res
        date_in = date_in_res.strftime("%d/%m/%Y").split("/")
        payload["checkInDate"] = {
            "day": int(date_in[0]),
            "month": int(date_in[1]),
            "year": int(date_in[2])
        }
        await ClientState.request_date_out.set()
        await callback_query.message.edit_text(text="Выберите дату выезда",
                                               reply_markup=await DialogCalendar().start_calendar())


async def process_dialog_calendar_out(callback_query: CallbackQuery, callback_data, state: FSMContext):

    selected, date_out_res = await DialogCalendar().process_selection(callback_query, callback_data)

    if selected:
        async with state.proxy() as data:
            date_in = data["date_in"]
        date_out = date_out_res.strftime("%d/%m/%Y").split("/")

        if date_out_res > date_in:
            payload["checkOutDate"] = {
                "day": int(date_out[0]),
                "month": int(date_out[1]),
                "year": int(date_out[2])
            }
            await ClientState.quantity_hotels.set()
            await callback_query.message.edit_text(text="Количество отелей",
                                                   reply_markup=keyboard_10numbers.keyboard_numbers)
        else:
            await callback_query.message.edit_text(text="Дата выбрана неправильно, выберите дату выезда",
                                                   reply_markup=await DialogCalendar().start_calendar())


def register_handler_callback_date(dp: Dispatcher):
    dp.register_callback_query_handler(process_dialog_calendar,
                                       dialog_cal_callback.filter(),
                                       state=ClientState.request_date_in)

    dp.register_callback_query_handler(process_dialog_calendar_out,
                                       dialog_cal_callback.filter(),
                                       state=ClientState.request_date_out)
