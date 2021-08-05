# 7. Сложить цифры целого числа заданного пользователем
Val = str(input())
Sum = 0
for i in Val:
    Sum = Sum + int(i)

print(Sum)