import pyperclip
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


import config
import pymorphy2

bot = Bot(config.TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        # one_time_keyboard=True
)
b1 = KeyboardButton("/c")
b2 = KeyboardButton("/z")
kb.insert(b1).insert(b2)

async def on_startup(_):
    print("Я запустился")

# создаем состояние
class TestStateComp(StatesGroup):
    waiting_for_text = State()
# создаем состояние2
class TestStateItog(StatesGroup):
    waiting_for_text = State()

@dp.message_handler(commands=['start'])
async def process_comp_command(message: types.Message):
    await bot.send_message(
            chat_id=message.from_user.id,
            text="давай приступим!",
            reply_markup=kb
    )

@dp.message_handler(commands=["cL"])
async def startCmd(mess: types.Message):
    await bot.send_message(
            chat_id=mess.from_user.id,
            text="cleaning KeyBoards",
            reply_markup=ReplyKeyboardRemove()
    )
    await mess.delete()

# Определяем функцию, которая будет вызвана по команде /comp
@dp.message_handler(commands=['c'])
async def process_comp_command(message: types.Message):
    await bot.send_message(
            chat_id=message.from_user.id,
            text="Введите компоненты:",
    )
    # задаем состояние ожидания текста
    await TestStateComp.waiting_for_text.set()
    @dp.message_handler(state=TestStateComp.waiting_for_text)
    async def process_message(message: types.Message, state: FSMContext):
        # Выполняем функцию qwe и отправляем результат пользователю
        result = qwe(message.text)
        await message.answer(f"{result}")
        await state.finish()

@dp.message_handler(commands=['z'])
async def itogging(message: types.Message):
    await bot.send_message(
            chat_id=message.from_user.id,
            text="Введите предложения:",
    )
    # задаем состояние ожидания текста
    await TestStateItog.waiting_for_text.set()
    @dp.message_handler(state=TestStateItog.waiting_for_text)
    async def clearN(message: types.Message, state: FSMContext):
        # Выполняем функцию qwe и отправляем результат пользователю
        result = clearNN(message.text)
        await message.answer(f"{result}")
        await state.finish()

def qwe(message: str):
    result = []
    text = message
    # Разбиваем текст на фразы по символам переноса строки
    phrases = text.split('\n')
    for index, phrase in enumerate(phrases):
        dummyString = []
        for word in phrase.split():
            genitive_word = inflect_to_genitive(word)
            dummyString.append(genitive_word)
        genitive_phrase = " ".join(dummyString)
        genitive_phrase += '.'
        result.append(genitive_phrase)

    itog = "\n".join(result)
    pyperclip.copy(itog)
    return itog

def inflect_to_genitive(word):
    morph = pymorphy2.MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    genitive_word = parsed_word.inflect({'gent'})
    return genitive_word.word if genitive_word else word

@dp.message_handler()
async def del_message(message: types.Message):
    await message.delete()



def clearNN(message: str):
    text = message.replace("\n", "")
    itog = text.replace(".", ". ")
    pyperclip.copy(itog)
    return itog


if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
