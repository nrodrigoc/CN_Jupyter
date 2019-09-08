import numpy as np
#Metodo de Newton
#Pn(x) = d0 + d1(x-x0) + d2(x-x0)*(x-x2) + ...
#d0 = x0
#d1 = f[x0,x1] = (f[x1] - f[x0]) / x1 - x0
#d2 = f[x0, x1, x2] = (f[x1,x2] - f[x0,x1]) / x2 - x0
#d3 = f[x


x = np.array([[2, 0, 1, 2, 4, 5]])
f = np.array([[5, 1, 3, -1, -1, 0]])
ordens = np.array([5])
d = np.append(x, x, axis=0)
print(d)
# [[1 2]
#  [3 4]]
#z = []
#ordens[0] = np.append(ordens[0], z)
y = [4, 1, -1]



class Interpolacao(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

        #N de iteracoes
        self.nDeIteracoes = 0

    def calcularDx(self):
        for c in range(1, len(x) - 1):
            for l in range(0, c):
                w = 0

