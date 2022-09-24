from tasks.task_16_gauss_function import gauss_function
import numpy as np


def gauss_kernel(sigma):
    k = round(sigma * 3 * 2 + 1)
    kernel = np.zeros((k, k))
    x_s = list(range(round(- sigma * 3), round(sigma * 3) + 1))
    y_s = list(x_s)
    for i, x in enumerate(x_s):
        kernel[i, :] = np.vectorize(gauss_function)(sigma=sigma, x=x, y=y_s)
    # normalizaion
    s = np.sum(kernel)
    kernel /= s
    return kernel


# sigma = float(input())
# kernel = gauss_kernel(sigma)
# print(*[' '.join([str(round(x, 5)) for x in x_i]) for x_i in kernel], sep='\n')
