import numpy as np
from math import sqrt, log, exp
from scipy.stats import laplace
from pynverse import inversefunc
from scipy.special import erf

def average(lst):
    return sum(lst) / len(lst)

def avgSquaredDeviation(array = []):
    deviation = 0
    for x in array:
        deviation += pow((x - average(array)), 2)
    deviation /= len(array)
    return sqrt(deviation)

def covariance(xarray, yarray):
    xavg = average(xarray)
    yavg = average(yarray)
    covar = 0
    for i in range(0, len(xarray)):
        covar += (xarray[i] - xavg)*(yarray[i] - yavg)
    return covar / len(xarray)
    
def StatCorelCoef(xar, yar):
    return covariance(xar, yar) / (avgSquaredDeviation(xar)*avgSquaredDeviation(yar))

def LaplaceDistribution(alpha):
    erf(1)
    Phi = lambda x: erf(x/2**0.5)/2
    invLap=inversefunc(Phi)
    return invLap((1-alpha)/2)

def empiricZzero(xar, yar):
    return 0.5 * log((1 + StatCorelCoef(xar, yar))/(1-StatCorelCoef(xar, yar)))


def main():
    filename = 'small_data.txt' 
    arrays = []
    with open(filename, 'r') as f:
        for line in f:
            arrays.append(
                np.array([float(val) for val in line.rstrip('\n').split(' ') if val != '']))
    print(f"X: {arrays[0]}")
    print(f"Y: {arrays[1]}")
    xlist = arrays[0]
    ylist = arrays[1]
    alpha = float(input("Рівень значущості: "))
    print(f"Коваріація: {covariance(xlist, ylist)}")
    print(f"Середнє статистичне відхилення по Х: {avgSquaredDeviation(xlist)}")
    print(f"Середнє статистичне відхилення по Y: {avgSquaredDeviation(ylist)}")
    print(f"Статистичний коефіцієнт кореляції: {StatCorelCoef(xlist, ylist)}")
    print(f"Емпіричне значення функції Фішера: {empiricZzero(xlist, ylist)}")

    z1 = empiricZzero(xlist, ylist) - (LaplaceDistribution(alpha) / (sqrt(len(xlist)-3)))
    z2 = empiricZzero(xlist, ylist) + (LaplaceDistribution(alpha) /( sqrt(len(xlist)-3)))

    rxy1 = (exp(2 * z1)-1) / (exp(2 * z1) + 1)
    rxy2 = (exp(2 * z2)-1) / (exp(2 * z2) + 1)

    print(f"Інтервальна оцінка функції Фішера: {z1} ≤ Z ≤ {z2}")
    print(f"Інтервальна оцінка Коефіцієнта кореляції: {rxy1} ≤ Rxy ≤ {rxy2}")

    l = rxy2 - rxy1

    if(l > StatCorelCoef(xlist, ylist)):
        print(f"{l} > {StatCorelCoef(xlist, ylist)}, зв'язку між X та Y не існує")
    else:
        print(f"{l} < {StatCorelCoef(xlist, ylist)}, зв'язок між X та Y існує")


if __name__ == '__main__':
    main()