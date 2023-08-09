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
    text = input_field_1.get().replace("\n", "").split(".")
    text = "\n".join(text)
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
    someData0 = roditPadesh().replace("\t", "").replace("\r", "").split("\n")[0:-1]
    someData1 = zakl().replace("\t", "").replace("\r", "").split("\n")[0:-1]
    zipped_values = zip(someData0, someData1)
    zipped_list = list(zipped_values)
    someData = []
    for elem in zipped_list:
        temp = elem[1] + " " + elem[0]
        someData.append(temp)
    combined_string = " ".join(someData)
    pyperclip.copy(combined_string)
    input_field.delete(0, tk.END)
    input_field_1.delete(0, tk.END)


def writeReadDict2Txt(choice):
    import pprint
    if choice == 1:
        with open('data_0.txt', 'r') as file:
            haha_0 = eval(file.read())
        with open('data.txt', 'r') as file:
            haha = eval(file.read())
        temp = haha_0 | haha  # Python 3.9+: The merge operator | now works for dictionaries:
        haha_1 = dict(sorted(haha.items(), key=lambda item: item[1]))
        with open('data_0.txt', 'w') as file:
            pprint.pprint(haha_0, stream=file)
        # Запись словаря в текстовый файл в человекочитаемой форме
        with open('data.txt', 'w') as file:
            pprint.pprint(haha_1, stream=file)
        return temp
    elif choice == 0:
        # Прочитать словарь из текстового файла
        with open('data_0.txt', 'r') as file:
            haha_0 = eval(file.read())
        with open('data.txt', 'r') as file:
            haha = eval(file.read())
        haha1 = haha_0 | haha  # Python 3.9+: The merge operator | now works for dictionaries:
        return haha1


# Define a function to clear the content of the text widget
def click_input_field(event):
    input_field.delete(0, "end")
    input_field.unbind('<Button-1>', clicked_input_field)


def click_input_field_1(event):
    input_field_1.delete(0, "end")
    input_field_1.unbind('<Button-1>', clicked_input_field_1)


haha = writeReadDict2Txt(0)

HELP_CMD = ""
for i in haha.keys():
    HELP_CMD += f"{i} => {haha[i]}\n"

is_info = False

root = tk.Tk()
root.title("GAU_GMT_BOT")
root.attributes("-topmost", True)
root.geometry("200x315")

# Create input field label and entry
input_label = tk.Label(root, text="T9/Single (компонент)", height=1)
input_label.pack(fill=tk.X)
input_field = tk.Entry(root)
input_field.insert(0, "Ключ или неисправность")
# Bind the Entry widget with Mouse Button to clear the content
clicked_input_field = input_field.bind('<Button-1>', click_input_field)
input_field.pack(padx=10, pady=5, fill=tk.X)

# Create output field label and entry
input_label_1 = tk.Label(root, text="Complex (неисправность)")
input_label_1.pack(fill=tk.X)
input_field_1 = tk.Entry(root)
input_field_1.insert(0, "Неисправности")
# Bind the Entry widget with Mouse Button to clear the content
clicked_input_field_1 = input_field_1.bind('<Button-1>', click_input_field_1)
input_field_1.pack(padx=10, pady=5, fill=tk.X)

# Create command buttons
T9_button = tk.Button(root, text="T9", command=cmdT9)
T9_button.pack(padx=10, pady=5, fill=tk.X)
zakl_button = tk.Button(root, text="Итоговое заключение", command=complexZakl)
zakl_button.pack(padx=10, pady=5, fill=tk.X)
# noinspection PyTypeChecker
show_info_message = tk.Button(root, text="Info message", command=show_info_message)
show_info_message.pack(padx=10, pady=5, fill=tk.X)

paste_button = tk.Button(root, text="Из буфера в Single", command=paste_from_clipboard)
paste_button.pack(padx=10, pady=5, fill=tk.X)
paste_button = tk.Button(root, text="Из буфера в Complex", command=paste_1_from_clipboard)
paste_button.pack(padx=10, pady=5, fill=tk.X)

# Bind the update_suggested_phrase function to the "<KeyRelease>" event on input_field
input_field.bind("<KeyRelease>", update_suggested_phrase)

root.mainloop()

