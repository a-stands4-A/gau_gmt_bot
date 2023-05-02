import string
from aiogram import Bot, Dispatcher, executor, types
import random as rdm

from  config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

count = 1

@dp.message_handler(commands=["desctiption"])
async def desc_c(message: types.Message):
    await message.answer("бот что-то умеет")
    await message.delete()

@dp.message_handler(commands=["count"])
async def count_c(message: types.Message):
    global count
    await message.answer(f"{count=}")
    count += 1

@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        return await message.answer(text="YES")
    await message.answer(text="NO")

@dp.message_handler()
async def rdm_ASCII(message: types.Message):
    await message.reply(rdm.choice(string.ascii_letters))


if __name__ == "__main__":
    executor.start_polling(dp)
