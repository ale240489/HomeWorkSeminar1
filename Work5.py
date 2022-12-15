#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
import math

pointAX = int(input('Введите координату X первой точки: '))
pointAY = int(input('Введите координату Y первой точки: '))

pointBX = int(input('Введите координату X второй точки: '))
pointBY = int(input('Введите координату Y второй точки: '))

distanceOfPoints = round(math.sqrt((pointBX-pointAX)**2+(pointBY-pointAY)**2),3)
print(distanceOfPoints)