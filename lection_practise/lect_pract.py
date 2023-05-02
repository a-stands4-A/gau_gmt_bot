import string
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random as rdm
import pyperclip  # для записи текста в clipboard
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        # one_time_keyboard=True
)  #TODO
b1 = KeyboardButton("/h")
b2 = KeyboardButton("/d")
b3 = KeyboardButton("/f")
bCl = KeyboardButton("/c")
kb.add(b1).insert(b2).insert(b3).insert(bCl)


# # lect
HELP_CMD = """
*/help* -_показывает список команд_
*/g* - _мимишный кот_
*/s* - _привет_
*/d* - _возможности_
"""

async def on_startup(_):
    print("Я запустился")

@dp.message_handler(commands=["h"])
async def helpCmd(mess: types.Message):
    await bot.send_message(
            chat_id=mess.from_user.id,
            text=HELP_CMD,
            parse_mode="MARKDOWN",
    )
    await mess.delete()

@dp.message_handler(commands=["s"])
async def startCmd(mess: types.Message):
    await bot.send_message(
            chat_id=mess.from_user.id,
            text="*welcome* on _board_ *!*",
            parse_mode="MARKDOWN",
            reply_markup=kb
    )
    await mess.delete()

@dp.message_handler(commands=["d"])
async def descCmd(mess: types.Message):
    await bot.send_message(
            chat_id=mess.from_user.id,
            text="Умелец наш *бот*!",
            parse_mode="MARKDOWN"
    )
    await mess.delete()

@dp.message_handler(commands=["f"])
async def fotoCmd(mess: types.Message):
    await bot.send_photo(
            mess.from_user.id,
            photo="https://www.fantasianew.ru/wa-data/public/shop/products/49/86/18649/images/99324/99324.970.jpg"
    )
    await mess.delete()

@dp.message_handler(commands=["c"])
async def startCmd(mess: types.Message):
    await bot.send_message(
            chat_id=mess.from_user.id,
            text="cleaning KeyBoards",
            reply_markup=types.ReplyKeyboardRemove()
    )
    await mess.delete()


###pract


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
