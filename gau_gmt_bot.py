from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help', 'echo'])
async def echo(msg: types.Message):
    await msg.answer(text=msg.text + ", GIT GUT, MATE", reply_markup=types .ReplyKeyboardRemove())

if __name__ == '__main__':
   executor.start_polling(dp)
