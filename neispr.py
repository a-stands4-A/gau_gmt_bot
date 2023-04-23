import pymorphy2

# Создаем экземпляр класса MorphAnalyzer
morph = pymorphy2.MorphAnalyzer()

neisprStr = "Разгерметизация, следы залива внутреннего пространства.\nОбрыв нити накала, нарушение целостности " \
            "электрической цепи"
neisprStr = neisprStr.replace(".", "")
neisprList = neisprStr.split("\n")

initialStr = "блок питания\nультразвуковой конвексный датчик"
wordsList = initialStr.split("\n")
result = [[]]*20
print(result)

for index, words in enumerate(wordsList):
    result[index] = [neisprList[index]]
    for word in words.split(" "):
        p = morph.parse(word)[0]
        result[index].append(p.inflect({'gent'}).word)
    result[index] = ' '.join(result[index])
    result[index] += '.'



print(result)
