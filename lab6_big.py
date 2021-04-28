import numpy as np
from math import sqrt, log

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

def testSmallData(xar, yar):
    covar = covariance(xar, yar)
    rigtarg = 3 * ((1 - pow(covar, 2))/sqrt(len(xar)))
    print("Критерій Романовського", rigtarg)
    if covar >= rigtarg:
        print(f'{covar} >= {rigtarg}, кореляційний зв\'язок між Х та У існує')
    else: 
        print(f'{covar} < {rigtarg}, кореляційного зв\'язку між Х та У не існує')


def main():
    filename = 'big_data.txt' 
    arrays = []
    with open(filename, 'r') as f:
        for line in f:
            arrays.append(
                np.array([float(val) for val in line.rstrip('\n').split(' ') if val != '']))
    print("X:", arrays[0])
    print("Y:", arrays[1])
    xlist = arrays[0]
    ylist = arrays[1]

    print(f"Коваріація: {covariance(xlist, ylist)}")
    print(f"Середнє статистичне відхилення по Х: {avgSquaredDeviation(xlist)}")
    print(f"Середнє статистичне відхилення по Y: {avgSquaredDeviation(ylist)}")
    print(f"Статистичний коефіцієнт кореляції: {StatCorelCoef(xlist, ylist)}")

    testSmallData(xlist, ylist)



if __name__ == '__main__':
    main()
