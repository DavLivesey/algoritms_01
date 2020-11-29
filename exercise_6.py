'''
Алла писала код, добавляющий запись в новую таблицу базы данных.
И вдруг получила ошибку duplicate foreign key constraint.
В тот же момент её отвлекла Рита. Алла случайно закрыла
окно терминала с информацией о том, какое именно значение
стало причиной ошибки.
Зато у неё сохранился список id, использованных при запросе.
Помогите ей выяснить,
какой id стал причиной ошибки.
Дан массив чисел, состоящий  из n целых чисел.
Одно число встречается более одного раза. Нужно определить это число.
'''


def count_points(points_list):
    answer_list = []
    for i in range(len(points_list)):
        if points_list[i] not in answer_list:
            answer_list.append(points_list[i])
        else:
            return points_list[i]


n = int(input())
points = (input().split(' '))
print(count_points(points))

# Time: 51ms, Memory: 4.16Mb
