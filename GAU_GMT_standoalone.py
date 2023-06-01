import tkinter as tk
import pyperclip
import pymorphy2
from tkinter import messagebox
from tkinter import scrolledtext

def paste_from_clipboard():
    text = pyperclip.paste()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, text)

def paste_1_from_clipboard():
    text = pyperclip.paste()
    input_field_1.delete(0, tk.END)
    input_field_1.insert(tk.END, text)

def copy_to_clipboard():
    text = input_field.get()
    root.clipboard_clear()
    pyperclip.copy(text)
    # root.clipboard_append(text)
def copy_1_to_clipboard():
    text = input_field_1.get()
    root.clipboard_clear()
    pyperclip.copy(text)
    # root.clipboard_append(text)


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
    # pyperclip.copy(itog)
    return itog

def inflect_to_genitive(word):
    morph = pymorphy2.MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    genitive_word = parsed_word.inflect({'gent'})
    return genitive_word.word if genitive_word else word

def zakl():
    text = input_field_1.get().replace("\n", "")
    text = text.replace(".", ". ")
    text = text.split('. ')
    text = "\n".join(text)
    # pyperclip.copy(text)
    # input_field.delete(0, tk.END)
    return text

def cmdT9():
    text = input_field.get()
    if text.lower() in haha.keys():
        pyperclip.copy(haha[text.lower()])
    input_field.delete(0, tk.END)
    input_field_1.delete(0, tk.END)

def show_info_message():
    if not hasattr(root, 'info_window'):
        root.info_window = tk.Toplevel()
        root.info_window.title("Information")
        info_text = scrolledtext.ScrolledText(root.info_window, wrap=tk.WORD)
        info_text.insert(tk.END, HELP_CMD)
        info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    else:
        root.info_window.destroy()
        del root.info_window
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
    someData1 = zakl().split("\n")
    someData = []
    for ind, elem in enumerate(someData0):
        temp = someData1[ind].replace("\r", "") + " " + someData0[ind]
        someData.append(temp)
    someData[-1], someData[0] = someData[0], someData[-1]
    combined_string = " ".join(someData)
    pyperclip.copy(combined_string)
    input_field.delete(0, tk.END)
    input_field_1.delete(0, tk.END)

def writeReadDict2Txt(choice):
    import pprint
    if choice == 1:
        with open('data.txt', 'r') as file:
            haha = eval(file.read())
        haha = sorted(haha.values())
        # Запись словаря в текстовый файл в человекочитаемой форме
        with open('data.txt', 'w') as file:
            pprint.pprint(haha, stream=file)
    elif choice == 0:
        # Прочитать словарь из текстового файла
        with open('data.txt', 'r') as file:
            haha = eval(file.read())
        return haha

haha = writeReadDict2Txt(0)

HELP_CMD = ""
for i in haha.keys():
    HELP_CMD += f"{i} - {haha[i]}\n"

is_info = False

root = tk.Tk()
root.title("GAU_GMT_BOT")
root.attributes("-topmost", True)
root.geometry("200x315")

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
# noinspection PyTypeChecker
show_info_message = tk.Button(root, text="show_info_message", command=show_info_message)
show_info_message.pack()

paste_button = tk.Button(root, text="Вставить из буфера в Single", command=paste_from_clipboard)
paste_button.pack()
# copy_button = tk.Button(root, text="Скопировать в буфер Single", command=copy_to_clipboard)
# copy_button.pack()
paste_button = tk.Button(root, text="Вставить из буфера в Complex", command=paste_1_from_clipboard)
paste_button.pack()
# copy_button = tk.Button(root, text="Скопировать в буфер Complex", command=copy_1_to_clipboard)
# copy_button.pack()


# Bind the update_suggested_phrase function to the "<KeyRelease>" event on input_field
input_field.bind("<KeyRelease>", update_suggested_phrase)

root.mainloop()
