import numpy
import random

n = int(input("Введіть граничну межу: "))
dots = []
for i in range(n):
    x = random.randint(-n, n)
    y = random.randint(- n, n )
    dots.append([i, x, y])

triangles = []

for i in range(len(dots)):
    for j in range(i+1, len(dots)):
        for k in range(j+1, len(dots)):
            triangles.append([
                dots[i],
                dots[j],
                dots[k]
            ])

triangles = numpy.array(triangles)

def calc_area(triangle):
    _, x1, y1 = triangle[0]
    _, x2, y2 = triangle[1]
    _, x3, y3 = triangle[2]
    return abs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))/2

calc_area_vectorized = numpy.vectorize(calc_area, signature='(m,n)->()')

Sq = calc_area_vectorized(triangles)

max_coor = max(Sq)
max_index = numpy.where(Sq == max_coor)[0][0]
print('Максимальне значення  S: ', max_coor)
print('Визначені точки: ')
for i, x, y in triangles[max_index]:
    print('Індекс:', i, f', значення: ({x},{y})')
