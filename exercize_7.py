'''
Вася вернулся домой под вечер и вспомнил,
что ещё не сделал домашнее задание по русскому языку.
Чтобы понять разницу между анаграммой и палиндромом,
Вася снова обратился к Алле. Она объяснила брату, что два слова — анаграммы,
если одно можно получить из другого перестановкой букв.
А палиндром — это слово или фраза, которая читается одинаково,
если читать слева направо и справа налево. Теперь Васе интересно:
как закодить функцию, определяющую, анаграммы слова или нет. Помогите ему.
'''

import collections

l1 = input()
l2 = input()
if collections.Counter(l1) == collections.Counter(l2):
    print('True')
else:
    print('False')

# Time: 47ms, Memory: 4.17Mb
