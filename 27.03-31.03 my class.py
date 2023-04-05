#Создание класса

class Cell:
    # атрибуты(переменные внутри класса)
    content = 1
    content_type = type(content)
    
    # метод - функция внутри класса
    def set_value(self, val):
        self.content = val
        self.content_type = type(val)


# Создание экземпляра класса (его дубликат)
a1=Cell()
b2=Cell()

print(a1.content_type)
a1.set_value("Hello")
print(a1.content)

# TypeError: set_value() takes 1 positional argument but 2 were give
# потому что надо добавить self в метод

# Специальные методы в Python
# Магия Python  - встроенные методы внутри  класса!

class Cell2:
    # конструктор - магический метод __init__
    def __init__(self, val: int) -> None:  # присвоение переменных
        self.content = val
        self.content_type = type(val)
    
    # метод - функция внутри класса
    def set_value(self, val:any) -> None:
        self.content = val
        self.content_type = type(val)

c3= Cell2(100)
c3.set_value("Привет")
print(c3.content)

# Наследование

class Plane:
    pass

class WarPlane(Plane):
    pass


class Bucket:
    '''Хранилище объектов длястатического сайта'''

    def __init__(self, tutorial=None):
        '''Инициализация бакета без описания по-умолчанию'''
        self.content = []
        if tutorial is not None: # проверка на пустоту
            self.content.append(tutorial)
    
    def __bool__(self):
        return self.content!= []

    def __str__(self) -> str:
        return 'Содержание: ' + ", ".join(self.content)

    def add(self, obj):
        '''Поместить объект в бакет'''
        print('Добавлен', obj)
        self.content.append(obj)

    def inspect(self):
        '''Проверить содержимое'''
        print('Текущее содержимое бакета')
        for item in self.content:
            print(' ', item)

#website = Bucket(tutorial = 'README.md')

#print=help(Bucket)
website=Bucket()
#website.inspect()
website.add('index.html')
website.add('main.css')
#website.inspect()
#print(website)
empty_bucket=Bucket()
print(bool(empty_bucket))
print(bool(website))


class Truck:
    '''Самосвал загружает в ковш и выгружает из него в другом месте.'''
    
    def __init__(self, *args):
        print('Загружено в ковш:')
        [print(i) for i in args]
    
    def __del__(self):
        print('Содержимое выгружено из ковша!')

Truck('песок', 'щебень', 'земля', 'блоки', 'идругое.')

class User:
    '''Модель пользователя'''
    #gid = 1000
    active = True
    
    def __init__(self, name=None):
        self.name = name
        self.gid = 1000
        self.get_permissions('700')

    def get_permissions(self, args):
        self.u, self.g, self.o = args
        return self.u, self.g, self.o

    # инкапсуляция 
    __token="very secret key" # поменять извне не получится
    def inspect(self):
        print(f'id({self.gid})')
        print('Active' if self.active else 'Dead')

class Root(User):
    '''Суперпользователь'''
    #gid = 0
    #active = False
    def __init__(self, token):
        super().__init__(name=None)
        self.gid = 0
        self.token = token
        self.get_permissions('777')
    
    def check_permissions(self):
        print('Права:', 'Чтение', 'Редактирование', 'Запись')

class Guest(User):
    '''Гость'''

    def check_permissions(self):
        print('Права:','Чтение')

    def get_token(self):
        print(self.__token)

#acc0=Root()
#acc0.inspect()
#acc0.get__token


#print('Радж')
#acc1=Guest()
#acc1.inspect() # Метод базового клвссв
#acc1.check_permissions() # Метод текущего класаа
#print(acc1.__class__ is User) # False, потому что это по факту класс  Guest , хоть он и наследует методы User 

acc1=Guest("Радж")
acc1.inspect() 
acc1.check_permissions() 

acc0=Root('very secret token')
acc0.inspect()


o=[]
if len(o) >=1:
    print ('true')
else: print ('False')