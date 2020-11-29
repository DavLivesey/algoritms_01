'''
На IT-конференции присутствовали студенты из разных вузов со всей страны.
Список студентов представлен в таблице.
В колонке «‎Вуз» записаны числа — id учебного заведения.
Тимофей предложил Саше выяснить, из каких вузов на
конференцию пришло больше всего учащихся. Ребята решили выяснить,
из каких k вузов присутствует больше всего гостей.
'''

ids_univer = list(map(int, input().split(' ')))
count_rating = int(input())
rating = {}
num = 0
for i in range(len(ids_univer)):
    if ids_univer[i] not in rating:
        rating[ids_univer[i]] = 1
    rating[ids_univer[i]] += 1
list_rating = list(rating.items())
list_rating.sort(key=lambda i: i[1], reverse=True)
answer_list = []
for i in list_rating:
    if num < count_rating:
        answer_list.append(i[0])
        num += 1
print(' '.join(repr(e) for e in answer_list))

# Time: 44ms, Memory: 4.20Mb
