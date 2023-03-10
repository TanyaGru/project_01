# Задача 1.2.

print ('\nПункт A.') 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
A=random.randint(0, 8)
B=random.randint(0, 8)
C=random.randint(0, 8)
while B==A:
    B=random.randint(0, 8)
while C==B or C==A:
    C=random.randint(0, 8)
x=round(my_favorite_songs[A][1]+my_favorite_songs[B][1]+my_favorite_songs[C][1], 2)
#print(A,B,C)
print(f'Три песни звучат {x} минут')

print ('\nПункт B.') 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
values=list(my_favorite_songs_dict.values())
A=random.randint(0, 8)
B=random.randint(0, 8)
C=random.randint(0, 8)
while B==A:
    B=random.randint(0, 8)
while C==B or C==A:
    C=random.randint(0, 8)
x=round(values[A]+values[B]+values[C], 2)
print(f'Три песни звучат {x} минут')
# Дополнительно для пунктов A и B
print ('\nПункт C.')
# Сгенерируйте случайные песни с помощью модуля random
# import random
print(f'Случайная песня из списка: {my_favorite_songs[random.randint(0, 8)][0]}')

g=my_favorite_songs_dict.keys()
print('Случайная песня из словаря:', list(g)[random.randint(0, 8)])

# Дополнительно 
print('\nПункт D.!!!!!!!!!!!!!!\n')
# Переведите минуты и секунды в формат времени. Используйте модуль 
import datetime 
sec=int(round((my_favorite_songs[0][1]-int(my_favorite_songs[0][1]))*100))
timeobj=datetime.time(0,int(my_favorite_songs[0][1]),sec)
print(timeobj)


