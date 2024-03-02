def word_frequency(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1

        else:
            word_count[word] = 1
    return word_count

# def word_frequency(sentence):
#     # Преобразуем все слова в нижний регистр
#     sentence_lower = sentence.lower()
#     # Разбиваем предложение на слова
#     words = sentence_lower.split()
#     # Создаем словарь для подсчета частоты слов
#     word_count = {}
#     # Подсчитываем частоту каждого слова
#     for word in words:
#         # Если слово уже есть в словаре, увеличиваем его счетчик на 1
#         if word in word_count:
#             word_count[word] += 1
#         # Если слова еще нет в словаре, добавляем его и устанавливаем счетчик в 1
#         else:
#             word_count[word] = 1
#     return word_count

# Пример использования функции
sentence = "Hello world, hello Python world! Python is awesome."
print(word_frequency(sentence))