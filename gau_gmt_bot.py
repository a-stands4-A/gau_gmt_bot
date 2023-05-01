from aiogram import Bot, Dispatcher, executor, types
import config

import pymorphy2

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


# Определяем функцию, которая будет вызвана по команде /comp
@dp.message_handler(commands=['c'])
async def process_comp_command(message: types.Message):
    # Отправляем пользователю сообщение с запросом ввода
    await bot.send_message(message.chat.id, "Введите компоненты:")

    @dp.message_handler()
    async def process_message(message: types.Message):
        # Выполняем функцию qwe и отправляем результат пользователю
        result = qwe(message.text)
        await message.answer(text=result)

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


if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)
