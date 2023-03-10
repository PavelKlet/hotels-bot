from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext, Dispatcher

from database import quick_commands
from state import ClientState
from keyboards import keyboard_10numbers, yes_no, inline_switch
from site_api.list_hotels import request_hotels, payload, user_info


async def process_quantity(callback_query: CallbackQuery):
    user_info["quantity"] = int(callback_query.data)

    await callback_query.message.edit_text(text="Нужны фото?",
                                           reply_markup=yes_no.keyboard_yes_no)

    await ClientState.need_photo.set()


async def process_answer(callback_query: CallbackQuery, state: FSMContext):

    """final answer if photos are not needed"""

    if callback_query.data == "Нет":

        await callback_query.message.edit_text(text="Поиск...")

        result = await request_hotels(quantity_hotels=user_info["quantity"],
                                      payload_info=payload)
        if result:

            async with state.proxy() as data:
                data["result"] = result
                data["hotels"] = "; ".join([hotel[2] for hotel in result])

                await quick_commands.add_user_info(int(data["user_id"]), data["hotels"], data["command"],
                                                   data["datetime"])

            switch = InlineKeyboardMarkup(row_width=2)

            switch.add(InlineKeyboardButton(text="<<Предыдущая", callback_data="prev:0"),
                       InlineKeyboardButton(text="Следующая>>", callback_data="next:0")).insert(
                InlineKeyboardButton(text="Выход", callback_data="exit"))

            await callback_query.bot.send_photo(chat_id=callback_query.message.chat.id,
                                                photo=result[0][4],
                                                caption=f"Цена за ночь: {result[0][0]}\n"
                                                        f"Цена за весь период: {result[0][1]}\n"
                                                        f"Название отеля: {result[0][2]}\n"
                                                        f"Ссылка на отель: {result[0][3]}\n"
                                                        f"Адрес: {result[0][5][0]}\n"
                                                        f"Расстояние до центра: {result[0][6]}",
                                                reply_markup=switch)
            await callback_query.message.delete()
            await ClientState.answer.set()

        else:
            await callback_query.message.answer(text="Ничего не нашлось")
            await state.finish()

    else:
        await callback_query.message.edit_text(text="Количество фотографий",
                                               reply_markup=keyboard_10numbers.keyboard_numbers)
        await ClientState.quantity_photo.set()


async def process_quantity_photo(callback_query: CallbackQuery, state: FSMContext):

    """the response process if photos are needed"""

    await callback_query.message.edit_text(text="Поиск...")

    result = await request_hotels(quantity_hotels=user_info["quantity"],
                                  quantity_photo=int(callback_query.data), payload_info=payload)

    if result:

        async with state.proxy() as data:
            data["result"] = result
            data["photo"] = result[0][5][1]
            data["hotels"] = "; ".join([hotel[2] for hotel in result])
            await quick_commands.add_user_info(int(data["user_id"]), data["hotels"], data["command"],
                                               data["datetime"])

        await callback_query.bot.send_photo(chat_id=callback_query.message.chat.id,
                                            photo=result[0][4],
                                            caption=f"Цена за ночь: {result[0][0]}\n"
                                                    f"Цена за весь период: {result[0][1]}\n"
                                                    f"Название отеля: {result[0][2]}\n"
                                                    f"Ссылка на отель: {result[0][3]}\n"
                                                    f"Адрес: {result[0][5][0]}\n"
                                                    f"Расстояние до центра: {result[0][6]}",
                                            reply_markup=inline_switch.switch)
        await callback_query.message.delete()
        await ClientState.answer.set()

    else:
        await callback_query.message.answer(text="Ничего не нашлось")
        await state.finish()


def register_handler_callback_quantity(dp: Dispatcher):
    dp.register_callback_query_handler(process_quantity,
                                       state=ClientState.quantity_hotels)

    dp.register_callback_query_handler(process_quantity_photo,
                                       state=ClientState.quantity_photo)

    dp.register_callback_query_handler(process_answer,
                                       state=ClientState.need_photo)