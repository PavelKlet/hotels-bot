from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMedia
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.inline_switch import switch
from state import ClientState

# inline keyboard for switching hotel photos


async def process_photo_hotels(callback_query: CallbackQuery, state: FSMContext):

    async with state.proxy() as data:
        photo = data["photo"]

    switch_photo = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton("<<Предыдущая", callback_data=f"prev_p:0"),
        InlineKeyboardButton("Следующая>>", callback_data=f"next_p:0"),
        (InlineKeyboardButton("Назад", callback_data="назад")),
    ).insert(InlineKeyboardButton("Выход", callback_data="exit"))

    await callback_query.message.edit_media(InputMedia(media=photo[0], type="photo",
                                                       caption="Фото отеля"),
                                            reply_markup=switch_photo
                                            )


async def process_next_photo(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    try:
        async with state.proxy() as data:
            photo = data["photo"]

            new_data = int(callback_query.data.split(":")[1]) + 1

            switch_photo = InlineKeyboardMarkup(row_width=2).add(
                InlineKeyboardButton("<<Предыдущая", callback_data=f"prev_p:{new_data}"),
                InlineKeyboardButton("Следующая>>", callback_data=f"next_p:{new_data}"),
                InlineKeyboardButton("Назад", callback_data="назад"),
            ).insert(InlineKeyboardButton("Выход", callback_data="exit"))

            await callback_query.message.edit_media(InputMedia(media=photo[new_data], type="photo",
                                                               caption="Фото отеля"),
                                                    reply_markup=switch_photo
                                                    )
    except IndexError:
        pass


async def process_prev_photo(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()

    try:
        async with state.proxy() as data:
            photo = data["photo"]

            new_data = int(callback_query.data.split(":")[1]) - 1

            switch_photo = InlineKeyboardMarkup(row_width=2).add(
                InlineKeyboardButton("<<Предыдущая", callback_data=f"prev_p:{new_data}"),
                InlineKeyboardButton("Следующая>>", callback_data=f"next_p:{new_data}"),
                InlineKeyboardButton("Назад", callback_data="назад"),
            ).insert(InlineKeyboardButton("Выход", callback_data="exit"))

            await callback_query.message.edit_media(InputMedia(media=photo[new_data], type="photo",
                                                               caption="Фото отеля"),
                                                    reply_markup=switch_photo
                                                    )
    except IndexError:
        pass


async def process_back(callback_query: CallbackQuery, state: FSMContext):

    async with state.proxy() as data:
        result = data["result"]
        data["photo"] = result[0][5][1]

    await callback_query.message.edit_media(InputMedia(media=result[0][4], type="photo",
                                                       caption=f"Цена за ночь: {result[0][0]}\n"
                                                               f"Цена за весь период: {result[0][1]}\n"
                                                               f"Название отеля: {result[0][2]}\n"
                                                               f"Ссылка на отель: {result[0][3]}\n"
                                                               f"Адрес: {result[0][5][0]}\n"
                                                               f"Расстояние до центра: {result[0][6]}"),
                                            reply_markup=switch)


def register_handler_switch_photos(dp: Dispatcher):
    dp.register_callback_query_handler(process_photo_hotels, Text('Фото'), state=ClientState.answer)
    dp.register_callback_query_handler(process_next_photo, Text(startswith="next_p"), state=ClientState.answer)
    dp.register_callback_query_handler(process_prev_photo, Text(startswith="prev_p"), state=ClientState.answer)
    dp.register_callback_query_handler(process_back, Text("назад"), state=ClientState.answer)