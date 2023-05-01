import aiogram.utils.markdown as md
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

# создаем состояние
class TestState(StatesGroup):
    waiting_for_text = State()


# Определяем функцию, которая будет вызвана по команде /comp
@dp.message_handler(commands=['c'])
async def process_comp_command(message: types.Message):
    await message.answer("Введите текст:")
    # задаем состояние ожидания текста
    await TestState.waiting_for_text.set()

@dp.message_handler(state=TestState.waiting_for_text)
async def process_message(message: types.Message, state: FSMContext):
    # Выполняем функцию qwe и отправляем результат пользователю
    result = qwe(message.text)
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
    return itog

def inflect_to_genitive(word):
    morph = pymorphy2.MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    genitive_word = parsed_word.inflect({'gent'})
    return genitive_word.word if genitive_word else word

@dp.message_handler()
async def process_message(message: types.Message):
    await message.delete()

if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp)
