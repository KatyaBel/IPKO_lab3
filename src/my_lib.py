#фибоначчи
def fibonacci(n):
    my_list = []
    f1 = f2 = 1
    print(f1, f2, end=' ')
    my_list.append(f1)
    my_list.append(f2)
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
        my_list.append(f2)
    return my_list


#пузырьковая сортировка
def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


#калькулятор
def calculator(a, b, sign):
    res = eval(f'{a} {sign} {b}')
    return res