import string
from aiogram import Bot, Dispatcher, executor, types
import random as rdm
import pyperclip  # для записи текста в clipboard
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# # lect
# @dp.message_handler(commands=["s"])
# async def start_CMD(message: types.Message):
#     # text = "*HI!* lets _kick_ *zayavki*"
#     await message.answer(text=text, parse_mode="MARKDOWN")
#     # pyperclip.copy(text)
#
#
# @dp.message_handler(commands=["g"])
# async def sticker_cmd(message: types.Message):
#     await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEI1AZkUU9Qa2Q3mpLEbcAn0681FKJkbQACpRAAArRFoEpqI1qAWc6jRy8E")
#     await message.delete()
#
# @dp.message_handler()
# async def emooo(message: types.Message):
#     await message.reply(message.text + "🛹")

###pract
HELP_CMD = """
*/help* -_показывает список команд_
*/g* - _мимишный кот_
"""

async def on_start_up(_):
    print("Я запустился")

@dp.message_handler(content_types=["sticker"])
async def sticker_id(mess: types.Message):
    await mess.answer(mess.sticker.file_id)


@dp.message_handler(commands=['h'])
async def helpCmd(mess: types.Message):
    await mess.reply(text=HELP_CMD, parse_mode="MARKDOWN")

@dp.message_handler(commands=["g"])
async def s_st(message: types.Message):
    await message.answer("Смотри на котяру:")
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgUAAxkBAAEI1ApkUVE6B_OoQ5R43oa2ijrdGFFoaQAC1gEAAt8fchn5W4LVs8ZxXy8E")


@dp.message_handler()
async def heart(message: types.Message):
    if message.text == "❤️":
        await message.answer(text="❤️‍🔥")


@dp.message_handler()
async def galy(message: types.Message):
    await message.answer(text=str(message.text.count("✅")))


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_up)
