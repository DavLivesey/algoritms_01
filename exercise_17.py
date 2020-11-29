'''
В метро Гоша обычно играет в мобильную игру «‎Черепашенька».
Он долго собирал данные о том, сколько очков зарабатывает
и проигрывает в день. Гоша собирает необычную статистику.
Нужно определить максимальное произведение заработанных очков
среди троек дней, в которые сумма очков равна нулю,
и произведение является положительным числом.
'''

n = int(input())
array = list(map(int, input().split(' ')))
array.sort()
max_arr = -1
for i in range(len(array)):
    left = i+1
    right = len(array) - 1
    while right > left:
        if array[i] + array[left] + array[right] > 0:
            right -= 1
        elif array[i] + array[left] + array[right] < 0:
            left += 1
        else:
            count = array[i] * array[left] * array[right]
            if count > max_arr:
                max_arr = count
            else:
                right -= 1
                left += 1
print(max_arr)

# Time: 1.468s, Memory: 3.95Mb
