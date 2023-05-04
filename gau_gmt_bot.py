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
from aiogram.utils import exceptions
import asyncio

import config
import pymorphy2


haha = {
        "бу": "Блок управления",
        "пу": "Панель управления",
        "кз": "Межвитковое замыкание обмоток трансформатора.",
        "в": "Выгорание электронных компонентов платы.",
        "ус": "Пробой элементов усилительного каскада.",
        "ак": "Аккумулятор",
        "акк": "Снижение емкостных характеристик, коррозия обмоток индукции.",
        "аку": "Повреждение акустической линзы.",
        "опт": "Оптическая система",
        "оптт": "Разгерметизация, вызывающая запотевание, помутнение элементов.",
        "вен": "Вентилятор",
        "венн": "Износ вала электродвигателя привода, пробой обмоток трансформатора.",
        "кнп": "Механическая выработка элементов, снижение активности кнопок.",
        "ш": "Выработка подвижных узлов и деталей.",
        "шш": "Штатив",
        "пр": "Выработка ресурса лентопротяжного механизма.",
        "прр": "Выработка ресурса лентопротяжного механизма, выгорание термоголовки.",
        "мп": "Механизм подъема",
        "мпп": "Разгерметизация гидравлической системы.",
        "мппп": "Механическая выработка узлов и деталей.",
        "ж": "Обрыв токонесущих жил кабелей.",
        "тчн": "Погрешность измерений выше класса точности, механическая выработка ресурса.",
        "изо": "Высыхание и нарушение изоляции токоведущих проводников.",
        "кп": "Растрескивание и разрывы внешнего покрытия до тканевой основы, разрушение крепёжных элементов.",
        "прб": "Пробозаборник",
        "ос": "Засорение химическими осадками тройного клапана.",
        "тн": "Выгорание нитей накала.",
        "ба": "Блок анализатора",
        "про": "Механический износ помп, выработка механизма пробозаборника.",
        "проо": "Выработан ресурс, дформация иглы.",
        "г": "Гидросистема",
        "гг": "Разгерметизация, утечка жидкости во внутреннее пространство аппарата.",
        "м": "Погрешность измерений выше класса точности, механическая выработка ресурса.",
        "мм": "Не прошёл метрологическую поверку, извещение о неисправности (неработоспособности) № КФТС-2-201/001-22Н от 22.06.22 г., максимальная величина выходной мощности не соответствует паспортному значению.",
}


HELP_CMD = ""
for i in haha.keys():
    HELP_CMD += f"*{i}* - _{haha[i]}_\n"

bot = Bot(config.TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        # one_time_keyboard=True
)
b1 = KeyboardButton("/c")
b2 = KeyboardButton("/z")
b3 = KeyboardButton("/h")
kb.insert(b1).insert(b2).add(b3)

async def on_startup(_):
    print("Я запустился")

# создаем состояние
class TestStateComp(StatesGroup):
    waiting_for_text = State()
# создаем состояние2
class TestStateItog(StatesGroup):
    waiting_for_text = State()
@dp.message_handler(commands=["h"])
async def helpCmd(mess: types.Message):
    await bot.send_message(
            chat_id=mess.from_user.id,
            text=HELP_CMD,
            parse_mode="MARKDOWN",
    )
    await mess.delete()

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
async def content(mess: types.Message):
    await mess.delete()
    if mess.text.lower() in haha.keys():
        # pyperclip.copy(haha[mess.text.lower()])
        await send_and_delete_message(mess.chat.id, haha[mess.text.lower()])

# функция для отправки сообщения с последующим удалением через 25 секунд
async def send_and_delete_message(chat_id, text):
    try:
        message = await bot.send_message(chat_id, text)
        await asyncio.sleep(5)  # ждем 25 секунд
        await bot.delete_message(chat_id, message.message_id)  # удаляем сообщение
    except exceptions.BotBlocked:
        print(f"Bot blocked by user with chat ID: {chat_id}")
    except exceptions.ChatNotFound:
        print(f"Chat not found for user with chat ID: {chat_id}")
    except exceptions.RetryAfter as e:
        print(f"RetryAfter {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_and_delete_message(chat_id, text)
    except exceptions.TelegramAPIError:
        print(f"Failed to send message to user with chat ID: {chat_id}")



def clearNN(message: str):
    text = message.replace("\n", "")
    itog = text.replace(".", ". ")
    pyperclip.copy(itog)
    return itog


if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
