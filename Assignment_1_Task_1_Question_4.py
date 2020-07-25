import math

class Point:
    pass

first = Point()
second = Point()
first.x = float(input('Pls enter the x co-ordinate of the first point:'))
first.y = float(input('Pls enter the y co-ordinate of the first point:'))
second.x = float(input('Pls enter the x co-ordinate of the second point:'))
second.y = float(input('Pls enter the y co-ordinate of the second point:'))

def dist(original,final):
    dist = math.sqrt((original.x - final.x) * (original.x - final.x) + (original.y - final.y) * (original.y - final.y))
    return dist

dist = dist(first, second)
print(dist)