'''
Гоша решил убрать из статистики дни, когда ничего
в «‎Черепашеньке» не заработал и не проиграл. Дан список заработанных
очков. Нужно удалить из него нули.
Дополнительную память больше O(1) использовать нельзя.
'''

n = int(input())
points = list(map(int, input().split(' ')))
points_without_zero = [points[i] for i in range(len(points)) if points[i]]
print(' '.join(repr(i) for i in points_without_zero))

# Time: 54ms, Memory: 3.94Mb
