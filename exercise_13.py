'''
А теперь помогите Васе решить задачу по информатике.
Он снова томится дома в хорошую погоду.
На вход подается строка длиной от 1 до 10000 символов.
Нужно отсортировать её в порядке частот букв по встречаемости.
Заглавные и строчные буквы считаются разными. Если частота одинаковая,
нужно применить вторичную сортировку лексикографически.
'''

import collections
from operator import itemgetter

text = list(input())
count = list((collections.Counter(text)).items())
count = sorted(count, key=itemgetter(0))
count = sorted(count, key=itemgetter(1), reverse=True)
answer = []
for i in count:
    answer.append(i[0]*i[1])
print(''.join(answer))

# Time: 48ms, Memory: 4.16Mb
