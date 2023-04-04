#x=float(input("Введите зарплату: "))
#e=float(input("Введите расходы: "))
#s=x
#for i in range(11):
    #x=x*1.05
    #s+=x
    #print(i,x,s)
#print(s-e*12)

#arr=[-3,2,4,0,5]
#k=-1
#result=[]
#for x in arr:
    #for y in arr:
        #if x+y==k:
            #result.append([x,y])
            #arr.remove(x)
            #arr.remove(y)
#print (result)

# НОРМАЛЬНЫЙ
# Бинарный поиск
def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    index = -1
    while (low <= high) and (index == -1):
        mid = (low+high) // 2
        if arr[mid] == x:
            index = mid
        else:
            if x < arr[mid]:
                high = mid -1
            else:
                low = mid +1
    return index

# Экспоненциальный поиск
def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= x:
        index = index * 2
    return binary_search( arr[:min(index, len(arr))], x)

print("\nEXPO")

# Тестовый массив
import random
arr = []
for i in range (10):
  arr.append(random.randint(1,50))
arr.sort()
print(arr)
x = int(input('Введи цифру: '))


 
# Вызов функции
print("Индекс искомого элемента: ",(exponential_search(arr,x)))


import math
from random import randint

def JumpSearh(arr,value):
  length = len(arr)
  jump = int(math.sqrt(length))
  left = 0
  rigth = 0
  while left < length and arr[left] <= value:
    rigth = min(length - 1, left + jump)
    if arr[left] <= value and arr[rigth] >= value:
      break
    left += jump
  if left >= length or arr[left] > value:
    return -1
  rigth = min(length-1, rigth)
  i = left
  while i < rigth and arr[i] <= value:
    if arr[i] == value:
      return i
    i +=1
  return -1

print("\nJUMP")
#Тестовый массив
testarr = []
for i in range (10):
  testarr.append(randint(1,50))
testarr.sort()
print(testarr)

value = int(input("Введи число: "))

# Вызов функции
if JumpSearh(testarr, value) != -1:
  print ("Элемент найден под индексом ", JumpSearh(testarr,value))
else:
  print ("Элемент отсутствует в списке")


def InterpolationSearch(arr, value):
  low = 0
  high = (len(arr)-1)
  while low <= high and value >= arr[low] and value <= arr[high]:
    index = low + int(((float(high-low) / (arr[high] - arr[low])) * (value - arr[low])))
    if arr[index] == value:
      return index
    if arr[index] < value:
      low = index + 1
    else:
      high = index - 1
  return -1

print("\nINTERPOL")
#Тестовый массив
for i in range (10):
  testarr.append(randint(1,50))
testarr.sort()
print(testarr)

value = int(input("Введи число: "))


# Вызов функции
if InterpolationSearch(testarr, value) != -1:
  print ("Элемент найден под индексом", InterpolationSearch(testarr,value),"\n")
else:
  print ("Элемент отсутствует в списке\n")

def factorial_iterative (k):
  factorial = 1
  if k<0:
    print("Нельзя вычислять факториал для отрицательных чисел")
  else:
    for i in range (1, k+1):
      factorial = factorial*i
    print(f"Факториал числа {k} это {factorial}\n")
factorial_iterative(3)

def factotial_rec(k):
  if k == 1:
    return k
  else:
    return k*factotial_rec(k-1)

print(factotial_rec(7))

## Тестовая папака
import os
def get_paths(path):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))
    
    yield abs_path
    
    if os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)

for i in get_paths("Тестовая папка"):
  print(i)

print("2 вариант")
import os
def get_paths(path='.'):
  for name in os.listdir(path):
    abs_path = os.path.abspath(os.path.join(path,name))
    if os.path.isfile(abs_path) is True:
      yield abs_path
    
    elif os.path.isdir(abs_path) is True:
      yield from get_paths(abs_path)

for i in get_paths("Тестовая папка"):
  print(i)

print("Привет\n", os.path.abspath(os.path.join("Тестовая папка", 'Тестовая папка 1')))
print("Привет\n", os.listdir("Тестовая папка"), os.path.join("Тестовая папка", 'Тестовая папка 1'))