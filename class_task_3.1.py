from random import randint

class Matrix:
    def __init__(self):
        z=int(input("\nЗадайте количество столбцов: "))
        x=int(input("Задайте количество строк: "))
        self.content=[[None for k in range(0,z)] for l in range(0, x)]

    def change(self,i,j,val):
        self.content[i][j]=val

    def add_colomn(self):
        for item in self.content:
            item.append(int(input(f'Введите {self.content.index(item)+1} число нового столбца: ')))
        
    def add_line(self):
        s=[]
        for i in range (0, len(self.content[0])):
            s.append(int(input(f'Введите {i+1} число новой строки: ')))
        self.content.append(s)

    def colomn_line_number(self):
        z=len(self.content)
        x=len(self.content[0])
        print(f'\nКоличество строк {z} \nКоличество  столбцов {x}\n')
  
    def __str__(self) -> str:
        y="\n"
        o=[]
        for itemz in self.content:
            for item in itemz:
                if item !=None:
                    o.append(len(str(item)))
        if len(o) >=1:
            h=max(o)
        else: h=2
        for itemz in self.content:
            for item in itemz:
                if item != None:
                    y=y+str(item)+' '*(h-len(str(item))+3)
                else: y=y+ "*"+' '*((h-1)+3)
            y+='\n'
        return y

    def full(self):
        z=len(self.content)
        x=len(self.content[0])
        print(f"Заполните матрицу {z}x{x}")
        for k in range(0,int(z)):
            for l in range(0,int(x)):
                self.content[k][l]=input(f'Введитете значение {k+1} строки {l+1} столбца:')
                if self.content[k][l]=="":
                    self.content[k][l]=None

    def auto_full(self):
        z=len(self.content)
        x=len(self.content[0])
        for k in range(0,int(z)):
            for l in range(0,int(x)):
                self.content[k][l]=randint(0,100)
                    

            


d=Matrix()
#d.full()
print (d)
d.change(0, 0,'45684122')
print (d)
d.auto_full()
print (d)
d.colomn_line_number()
d.add_line()
print (d)
d.add_colomn()
print (d)
d.colomn_line_number()