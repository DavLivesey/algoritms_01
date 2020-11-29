'''
На клавиатуре старых мобильных телефонов каждой цифре
cоответствовало несколько букв. Примерно так:
2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'
Вам известно в каком порядке были нажаты клавиши телефона, без учета повторов.
Напечатайте все комбинации букв,
которые можно набрать такой последовательностью нажатий.
'''

import itertools

buttons = {2: 'abc',
           3: 'def',
           4: 'ghi',
           5: 'jkl',
           6: 'mno',
           7: 'pqrs',
           8: 'tuv',
           9: 'wxyz'}
action = list(map(int, input()))
list_letters = [buttons[i] for i in action]
answer = itertools.product(*list_letters)
for i in answer:
    print(''.join(i), end=' ')

# Time: 92ms, Memory: 4.16Mb
