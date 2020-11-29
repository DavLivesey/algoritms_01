'''
А теперь помогите Васе понять, будет ли фраза палиндромом‎.
Учитываются только буквы и цифры,
заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N - длина строки на входе.
'''

slovo = str(input())
slovo.lower()
length = len(slovo)
left = 0
right = length - 1
brk = 0
while right - left >= left:
    if slovo[right].isalpha():
        if slovo[left].isalpha():
            if slovo[right].lower() == slovo[left].lower():
                left += 1
                right -= 1
            else:
                brk = 1
                break
        else:
            left += 1
    else:
        right -= 1
if brk == 1:
    print("False")
else:
    print("True")

# Time: 44ms, Memory: 4.21Mb
