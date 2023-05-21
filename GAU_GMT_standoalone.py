import tkinter as tk
import pyperclip
import pymorphy2
from tkinter import messagebox

def roditPadesh():
    result = []
    text = input_field.get()
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
    # input_field.delete(0, tk.END)
    # input_field_1.delete(0, tk.END)
    return itog

def inflect_to_genitive(word):
    morph = pymorphy2.MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    genitive_word = parsed_word.inflect({'gent'})
    return genitive_word.word if genitive_word else word

def zakl():
    text = input_field_1.get().replace("\n", "")
    text = text.replace(".", ". ")
    pyperclip.copy(text)

    # input_field.delete(0, tk.END)
    return text

def cmdT9():
    text = input_field.get()
    if text.lower() in haha.keys():
        pyperclip.copy(haha[text.lower()])
    input_field.delete(0, tk.END)
    input_field_1.delete(0, tk.END)

def show_info_message():
    messagebox.showinfo("Информация", HELP_CMD)

def update_suggested_phrase(event):
    text = input_field.get().lower()
    if text in haha:
        suggested_phrase = haha[text]
        input_field_1.delete(0, tk.END)
        input_field_1.insert(tk.END, suggested_phrase)
    else:
        input_field_1.delete(0, tk.END)

def complexZakl():
    someData0 = roditPadesh().split("\n")
    someData1 = zakl().split(". ")
    someData = []
    for ind, elem in enumerate(someData0):
        temp = someData1[ind] + " " + someData0[ind]
        someData.append(temp)
    combined_string = "".join(someData)
    pyperclip.copy(combined_string)
    input_field.delete(0, tk.END)
    input_field_1.delete(0, tk.END)

haha = {
        "1"   : "Царапины и потёртости изделия и его элементов обусловлены интенсивной и длительной эксплуатацией.",
        "2"   : "Рентгеновская трубка.",
        "д1"  : "Деформация конструкции, коррозия сварных швов.",
        "ск"  : "Сколы лако-красочного покрытия, глубокая коррозия рабочих поверхностей.",
        "э"   : "Электроды",
        "д"   : "Оборудование демонтировано силами ЛПУ.",
        "бу"  : "Блок управления",
        "бп"  : "Блок питания",
        "вы"  : "Выгорание электронных компонентов.",
        "вы1" : "Выгорание электронных компонентов платы управления.",
        "пу"  : "Панель управления",
        "пуу" : "Механическая выработка элементов, снижение активности кнопок.",
        "ок"  : "Окисление электронных компонентов и токопроводящих дорожек материнской платы.",
        "кз"  : "Межвитковое замыкание обмоток трансформатора.",
        "ус"  : "Пробой элементов усилительного каскада.",
        "ак"  : "Аккумулятор",
        "акк" : "Снижение емкостных характеристик, коррозия обмоток индукции.",
        "аку" : "Повреждение акустической линзы.",
        "опт" : "Оптическая система",
        "оптт": "Разгерметизация, вызывающая запотевание, помутнение элементов.",
        "вен" : "Вентилятор",
        "венн": "Износ вала электродвигателя привода, пробой обмоток трансформатора.",
        "кнп" : "Механическая выработка элементов, снижение активности кнопок.",
        "ш"   : "Выработка подвижных узлов и деталей.",
        "шш"  : "Штатив",
        "пр"  : "Выработка ресурса лентопротяжного механизма.",
        "прр" : "Выработка ресурса лентопротяжного механизма, выгорание термоголовки.",
        "мп"  : "Механизм подъема",
        "мпп" : "Разгерметизация гидравлической системы.",
        "мппп": "Механическая выработка узлов и деталей.",
        "ж"   : "Обрыв токонесущих жил кабелей.",
        "тчн" : "Погрешность измерений выше класса точности, механическая выработка ресурса.",
        "изо" : "Высыхание и нарушение изоляции токоведущих проводников.",
        "кп"  : "Растрескивание и разрывы внешнего покрытия до тканевой основы, разрушение крепёжных элементов.",
        "прб" : "Пробозаборник",
        "ос"  : "Засорение химическими осадками тройного клапана.",
        "тн"  : "Выгорание нитей накала.",
        "ба"  : "Блок анализатора",
        "про" : "Механический износ помп, выработка механизма пробозаборника.",
        "проо": "Выработан ресурс, деформация иглы.",
        "г"   : "Гидросистема",
        "гг"  : "Разгерметизация, утечка жидкости во внутреннее пространство аппарата.",
        "м"   : "Погрешность измерений выше класса точности, механическая выработка ресурса.",
        "мм"  : "Не прошёл метрологическую поверку, извещение о неисправности (неработоспособности) № КФТС-2-201/001-22Н от 22.06.22 г., максимальная величина выходной мощности не соответствует паспортному значению.",
}


HELP_CMD = ""
for i in haha.keys():
    HELP_CMD += f"{i} - {haha[i]}\n"

root = tk.Tk()
root.title("GAU_GMT_BOT")
root.geometry("300x215")

# Create input field label and entry
input_label = tk.Label(root, text="Single (компонент):")
input_label.pack()
input_field = tk.Entry(root)
input_field.pack()

# Create output field label and entry
input_label_1 = tk.Label(root, text="Complex (неисправность):")
input_label_1.pack()
input_field_1 = tk.Entry(root)
input_field_1.pack()

# Create command buttons
helpCMD_button = tk.Button(root, text="Т9", command=cmdT9)
helpCMD_button.pack()
# component_button = tk.Button(root, text="Родительный падеж", command=roditPadesh)
# component_button.pack()
zakl_button = tk.Button(root, text="Итоговое заключение", command=complexZakl)
zakl_button.pack()
show_info_message = tk.Button(root, text="show_info_message", command=show_info_message)
show_info_message.pack()

# Bind the update_suggested_phrase function to the "<KeyRelease>" event on input_field
input_field.bind("<KeyRelease>", update_suggested_phrase)

root.mainloop()
