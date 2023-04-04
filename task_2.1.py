# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

a=[4,6,2,1,9,63,-134,566]
b=[-52, 56, 30, 29, -54, 0, -110]
c=[42, 54, 65, 87, 0]
d=[5]

def minimum(arr):
    min=arr[0]
    for item in arr:
        if min>item:
            min=item
    return(min)

def maximum(arr):
    max=arr[0]
    for item in arr:
        if max<item:
            max=item
    return(max)

print(f'\nВ списке {a}: min={minimum(a)}, max={maximum(a)}')
print(f'\nВ списке {b}: min={minimum(b)}, max={maximum(b)}')
print(f'\nВ списке {c}: min={minimum(c)}, max={maximum(c)}')
print(f'\nВ списке {d}: min={minimum(d)}, max={maximum(d)}\n')

# Супер) можно также воспользоваться быстрой сортировкой
def quicksort(arr):
    if len(arr) < 2:
        # базовый случай, массив с 0 или 1 элементом уже отсортирован
        return arr
    else:
        # рекурсивный случай. выберем опорный элемент pivot
        pivot = arr[0]
        # подмассив всех элементов, меньших, чем опорный элемент pivot
        less = [i for i in arr[1:] if i <= pivot]
        # подмассив всех элементов, превышающих опорный элемент pivot
        greater = [i for i in arr[1:] if i > pivot]
        # обединяем в порядке "сортировка для меньшего подмассива – опорный элемент – сортировка для большего подмассив"
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]
print('\nБыстрая сортировка')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
