from aiogram import Bot, Dispatcher, executor, types
import config


bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

HELP_CMD = """
/help - list of commands
/start - start work via bot
"""

@dp.message_handler(commands=["help"])
async def hellp_cmd(message: types.Message):
    await message.reply(text=HELP_CMD)


@dp.message_handler(commands=["start"])
async def hellp_cmd(message: types.Message):
    await message.answer(text="welcome on board")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp)
