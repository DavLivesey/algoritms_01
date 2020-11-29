'''
Васе очень понравилась задача про анаграммы и он придумал к ней модификацию.
Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы
в случайную позицию. Нужно найти добавленную букву.
'''

import collections

text_1 = collections.Counter(input())
text_2 = collections.Counter(input())
if len(text_1) > len(text_2):
    for i in text_1:
        if text_1[i] != text_2[i]:
            print(i)
else:
    for i in text_2:
        if text_1[i] != text_2[i]:
            print(i)

# Time: 47ms, Memory: 4.20Mb
