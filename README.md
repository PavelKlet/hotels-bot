Бот-парсер API с сайта https://rapidapi.com/apidojo/api/hotels4/

Для использования скрипта необходимо зарегистрироваться на сайте rapidapi и оформить подписку на отправку запросов (базовая бесплатна, 500 запросов)

Создать бота у BotFather

Создать файл .env, где прописать данные из env.template


В качестве БД для получения истории запросов используется PostgreSQL, gino; для взаимодействия с API сайта aiohttp; функционал бота aiogram

Бот по команде /low производит поиск самых недорогих отелей в локации прописанной пользователем,
/high - самые дорогие, /bestdeal - поиск по введённым пользователем диапазоном цен и расстояние до центра города (до 10 отелей)

/history - последние запросы пользователя с информацией о введенной команде, датой и временем введенной команды и найденными отелями