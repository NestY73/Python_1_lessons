# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, coordx1, coordy1, coordx2, coordy2, coordx3, coordy3):
        self.coordx1=coordx1
        self.coordx2=coordx2
        self.coordx3=coordx3
        self.coordy1=coordy1
        self.coordy2=coordy2
        self.coordy3=coordy3

    #методы
    #вычисление длины стороны
    def storona_len(self):
        pass
    #вычисление периметра
    def perimetr(self):
        AB=math.sqrt((self.coordx1-self.coordx2)**2+(self.coordy1-self.coordy2)**2)
        BC=math.sqrt((self.coordx2-self.coordx3)**2+(self.coordy2-self.coordy3)**2)
        AC=math.sqrt((self.coordx1-self.coordx3)**2+(self.coordy1-self.coordy3)**2)
        return (AB+BC+AC)
    #вычисление площади
    def square(self):
        AB=math.sqrt((self.coordx1-self.coordx2)**2+(self.coordy1-self.coordy2)**2)
        BC=math.sqrt((self.coordx2-self.coordx3)**2+(self.coordy2-self.coordy3)**2)
        AC=math.sqrt((self.coordx1-self.coordx3)**2+(self.coordy1-self.coordy3)**2)
        P=(AB+BC+AC)/2
        return(math.sqrt((P-AB)*(P-AC)*(P-BC)*P))


Tri=Triangle(1,1,-2,4,-2,-2)
print('Периметр треугольника равен: {:.2f}'.format(Tri.perimetr()))
print('Площадь треугольника равна: {:.2f}'.format(Tri.square()))



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, coordx1, coordy1, coordx2, coordy2, coordx3, coordy3, coordx4, coordy4):
        self.coordx1=coordx1
        self.coordx2=coordx2
        self.coordx3=coordx3
        self.coordx4=coordx4
        self.coordy1=coordy1
        self.coordy2=coordy2
        self.coordy3=coordy3
        self.coordy4=coordy4

    #методы
    #проверка трапеции на равнобокость-равенство диагоналей AC и BD
    def equal_side(self):
        AC=math.sqrt((self.coordx1-self.coordx3)**2+(self.coordy1-self.coordy3)**2)
        BD=math.sqrt((self.coordx2-self.coordx4)**2+(self.coordy2-self.coordy4)**2)
        if AC!=BD:
            return ('Трапеция не равнобокая')
        else:
            return ('Трапеция равнобокая')
    #вычисление периметра
    def perimetr(self):
        AB=math.sqrt((self.coordx1-self.coordx2)**2+(self.coordy1-self.coordy2)**2)
        BC=math.sqrt((self.coordx2-self.coordx3)**2+(self.coordy2-self.coordy3)**2)
        CD=math.sqrt((self.coordx3-self.coordx4)**2+(self.coordy3-self.coordy4)**2)
        AD=math.sqrt((self.coordx1-self.coordx4)**2+(self.coordy1-self.coordy4)**2)
        return (AB+BC+CD+AD)
    #вычисление площади
    def square(self):
        AB=math.sqrt((self.coordx1-self.coordx2)**2+(self.coordy1-self.coordy2)**2)
        BC=math.sqrt((self.coordx2-self.coordx3)**2+(self.coordy2-self.coordy3)**2)
        CD=math.sqrt((self.coordx3-self.coordx4)**2+(self.coordy3-self.coordy4)**2)
        AD=math.sqrt((self.coordx1-self.coordx4)**2+(self.coordy1-self.coordy4)**2)
        res1=(AD-BC)**2+AB**2-CD**2
        res2=2*(AD-BC)
        res3=(res1/res2)**2
        res4=math.sqrt(AB**2-res3)
        S=((BC+AD)/2)*res4
        return S
Trp=Trapezium(1,1,-2,4,-2,-2,2,2)
print('Периметр трапеции равен: {:.2f}'.format(Trp.perimetr()))
print('Площадь трапеции равна: {:.2f}'.format(Trp.square()))
