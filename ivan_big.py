from statistics import mean
import numpy as np
import math
def kst(x, y):
    sum = 0
    for i in range(0, len(x)):
        sum += (x[i]-mean(x))*(y[i]-mean(y))
    return sum/len(x)


def S(arr):
    sum = 0
    for item in arr:
        sum += (item-mean(arr))**2
    return math.sqrt(sum/len(arr))


def r(x, y):
    return kst(x, y)/(S(x)*S(y))

filename = 'big_data.txt' 
arrays = []
with open(filename, 'r') as f:
    for line in f:
        arrays.append(
            np.array([float(val) for val in line.rstrip('\n').split(' ') if val != '']))
x = arrays[0]
y = arrays[1]
print(x)
print(y)
print("Статистичний кореляційний момент: ", kst(x, y))
print("Середнє квадратичне відхилення по х: ", S(x))
print("Середнє квадратичне відхилення по у: ", S(y))
print("Cтатистичний коефіцієнт кореляції: ", r(x, y))
print("Критерій Романовського: ", 3*((1-r(x, y)**2)/math.sqrt(len(x))))

romanov = 3*((1-r(x, y)**2)/math.sqrt(len(x)))
if(abs(r(x, y)) >= romanov):
    print(abs(r(x, y)), "≥", romanov, " - між величинами існує кореляційний зв`язок\n")
else:
    print(abs(r(x, y)), "<", romanov, " - між величинами не існує кореляційного зв'язку\n")
