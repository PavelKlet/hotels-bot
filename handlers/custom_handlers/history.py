from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from database.quick_commands import select_user


async def process_history(message: Message):

    user_info = await select_user(int(message.from_user.id))

    if user_info:

        info_result = [f"Отели: {info.hotels}\nКоманда: {info.command}\n"
                       f"Дата и время отправки: "
                       f"{info.date}\n"
                       for info in user_info
                       ][::-1][:10]

        for info in info_result:
            i_index = info_result.index(info)
            info_result[i_index] = f"{i_index + 1}. " + info

        await message.answer(text="\n".join(info_result))
    else:
        await message.answer(text="Данных нет")


def register_handler_history(dp: Dispatcher):
    dp.register_message_handler(process_history, commands=["history"])
