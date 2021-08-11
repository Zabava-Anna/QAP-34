# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

def checknum(ent):
    for n in ent:
        if n in alph:
            return f'Введите только числа'
        elif n in sym:
            return f'Введите только числа'
        else:
            spisok.append(int(n))
    return spisok


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1,  middle + 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


spisok = []
alph = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
sym = "!@#$%^&*(\_-)+=:;|/?.,><[{]}`~§±"
ent = input("Введите числа через пробел \n").split()
print(checknum(ent))
number = int(input("Введите любое число \n"))
spisok.append(number)
spisok_sort = merge_sort(spisok)
print(spisok_sort)
print(binary_search(spisok_sort, number, 0, len(spisok_sort)))
