# 1. Соберем первого бота. Импортируем сущность бота, диспетчера, «executor», типы
from aiogram import Bot, Dispatcher, executor, types
# 2. Из блока работы с памятью (находится в aiogram.contrib) нужен "fsm_storage".
# Нужно импортировать оттуда «MemoryStorage».
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# 3. Далее асинхронность, ее нужно доставить
import asyncio

# 4. Дальше понадобится api ключ, который мы получили в «BotFather». Так же переменная бота,
# она будет хранить объект бота, «token» будет равен вписанному ключу
api = ""
bot = Bot(token=api)
# 5. Понадобится «Dispatcher», который будет объектом «Dispatcher», у него будет наш бот в
# качестве аргументов. В качестве «Storage» будет «MemoryStorage»
dp = Dispatcher(bot, storage=MemoryStorage())

# # 7. Создание асинхронного обработчика сообщений

# декоратор Хэндлера перехватывающий избранные сообщения 'Urban', 'dd', 'ff'
@dp.message_handler(text = ['Urban', 'dd', 'ff'])
async def urban_massage(message):
    print('Urban message')

# декоратор-хэндлер общего типа прописывается ниже тех, которые
# обрабатывают избранные сообщения и команды (данный перехватывает все сообщения)
@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение')

# 6. Запускаем «executor», у которого есть функция «start_polling». Объясняем,
# через кого ему запускаться
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
