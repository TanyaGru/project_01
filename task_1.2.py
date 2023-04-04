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
sml=random.sample(range(0,8),3)
sum=round(my_favorite_songs[sml[0]][1]+my_favorite_songs[sml[1]][1]+my_favorite_songs[sml[2]][1], 2)
print(f'Три песни звучат {sum} минут')

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
sml=random.sample(range(0,8),3)
sum=round(values[sml[0]]+values[sml[1]]+values[sml[2]], 2)
print(f'Три песни звучат {sum} минут')
# Дополнительно для пунктов A и B
print ('\nПункт C.')
# Сгенерируйте случайные песни с помощью модуля random
# import random
print(f'Случайная песня из списка: {my_favorite_songs[random.randint(0, 8)][0]}')

g=my_favorite_songs_dict.keys()
print('Случайная песня из словаря:', list(g)[random.randint(0, 8)])

# Дополнительно 
print('\nПункт D.')
# Переведите минуты и секунды в формат времени. Используйте модуль 
import datetime 
i=random.randint(0, 8)
sec=int(round((my_favorite_songs[i][1]-int(my_favorite_songs[i][1]))*100))
timeobj=datetime.time(0,int(my_favorite_songs[i][1]),sec).strftime("%M:%S")
print(timeobj,'\n')


#Если после запятой сотые доли минуты
#import time
#n=my_favorite_songs[i][1]*60
#time_format=time.strftime("%M:%S", time.gmtime(n))
#print(time_format,'\n')

# К сожалению, есть вероятность, что будет ошибка(
# Вот вариант мой
from datetime import timedelta
from math import modf
from random import sample


total_time = timedelta()

for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Три песни звучат {total_time} минут')
