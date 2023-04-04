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
