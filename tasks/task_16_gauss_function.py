import math


def gauss_function(sigma, x, y):
    return math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2)) / (2 * math.pi * sigma ** 2)


#sigma, x, y = list(map(int, input().split()))
#print(gauss_function(sigma, x, y))
