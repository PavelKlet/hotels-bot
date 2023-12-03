from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMedia
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text

from state import ClientState


async def process_next_hotel(callback_query: CallbackQuery, state: FSMContext):

    await callback_query.answer()

    try:
        async with state.proxy() as data:
            result = data["result"]
            new_data = int(callback_query.data.split(":")[1]) + 1
            switch = InlineKeyboardMarkup(row_width=2).add(
                InlineKeyboardButton("<<Предыдущая", callback_data=f"prev:{new_data}"),
                InlineKeyboardButton("Следующая>>", callback_data=f"next:{new_data}"),
            ).insert(InlineKeyboardButton("Выход", callback_data="exit"))
            data["photo"] = result[new_data][5][1]

            if data["photo"]:
                switch.add(InlineKeyboardButton(text="Фото", callback_data="Фото"))

            await callback_query.message.edit_media(InputMedia(media=result[new_data][4], type="photo",
                                                               caption=f"Цена за ночь: {result[new_data][0]}\n"
                                                                       f"Цена за весь период: {result[new_data][1]}\n"
                                                                       f"Название отеля: {result[new_data][2]}\n"
                                                                       f"Ссылка на отель: {result[new_data][3]}\n"
                                                                       f"Адрес: {result[new_data][5][0]}\n"
                                                                       f"Расстояние до центра: {result[new_data][6]}"),
                                                    reply_markup=switch
                                                    )
    except IndexError:
        pass


async def process_prev_hotel(callback_query: CallbackQuery, state: FSMContext):

    await callback_query.answer()

    try:
        async with state.proxy() as data:
            result = data["result"]
            new_data = int(callback_query.data.split(":")[1]) - 1
            switch = InlineKeyboardMarkup(row_width=2).add(
                InlineKeyboardButton("<<Предыдущая", callback_data=f"prev:{new_data}"),
                InlineKeyboardButton("Следующая>>", callback_data=f"next:{new_data}"),
            ).insert(InlineKeyboardButton("Выход", callback_data="exit"))
            data["photo"] = result[new_data][5][1]

            if data["photo"]:
                switch.add(InlineKeyboardButton(text="Фото", callback_data="Фото"))

            await callback_query.message.edit_media(InputMedia(media=result[new_data][4], type="photo",
                                                               caption=f"Цена за ночь: {result[new_data][0]}\n"
                                                                       f"Цена за весь период: {result[new_data][1]}\n"
                                                                       f"Название отеля: {result[new_data][2]}\n"
                                                                       f"Ссылка на отель: {result[new_data][3]}\n"
                                                                       f"Адрес: {result[new_data][5][0]}\n"
                                                                       f"Расстояние до центра: {result[new_data][6]}"),
                                                    reply_markup=switch
                                                    )
    except IndexError:
        pass


async def process_callback_exit(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите /start для поиска отелей\n/help информация по командам бота")
    await state.finish()


def register_handler_switch(dp: Dispatcher):
    dp.register_callback_query_handler(process_next_hotel, Text(startswith="next:"), state=ClientState.answer)
    dp.register_callback_query_handler(process_prev_hotel, Text(startswith="prev:"), state=ClientState.answer)
    dp.register_callback_query_handler(process_callback_exit, Text("exit"), state=ClientState.answer)
