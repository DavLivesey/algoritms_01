'''
Вася на уроке математики проходил степени.
Он хочет написать программу, которая определяет,
будет ли положительное целое число степенью четверки.
'''

from math import log

x = int(input())


def x_4(y):
    return y == 1 or (y == 4**log(y, 4) and log(y, 4) % int(log(y, 4)) == 0)


print(x_4(x))

# Time: 43ms, Memory: 4.17Mb
