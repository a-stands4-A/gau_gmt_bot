from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help', 'echo'])
async def echo(msg: types.Message):
    await msg.answer(text=msg.text + ", GIT GUT, MATE", reply_markup=types .ReplyKeyboardRemove())


# # practice 1.1
# @dp.message_handler()
# async def echo_upper(message: types.Message):
#     await message.answer(text=message.text.upper())

# practice 1.2
@dp.message_handler()
async def mes_count(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text)

if __name__ == '__main__':
   executor.start_polling(dp)
