import numpy as np
import matplotlib.pyplot as plt

# Metodo de Newton
# Pn(x) = d0 + d1(x-x0) + d2(x-x0)*(x-x2) + ...
# d0 = x0
# d1 = f[x0,x1] = (f[x1] - f[x0]) / x1 - x0
# d2 = f[x0, x1, x2] = (f[x1,x2] - f[x0,x1]) / x2 - x0

# Definição dos parâmetros
x = np.array([-1, 1, 2, 3, 5])
f = np.array([-4, 0, 3, 5, 3])
# Vetor auxiliar f1
f1 = np.array([-4, 0, 3, 5, 3])
# Array com primeiro elemento d0 sendo x0
ordens = np.array([f1[0]])


class Interpolacao(object):

    def __init__(self, x, f, ordensAux):
        self.x = x
        self.f = f
        self.ordensAux = ordensAux

        # N de vezes que o método calcularDx procura cada os valores de cada ordem
        self.nDeIteracoes = 0

    def calcularDx(self):
        # Pega as variaveis definidas fora do escopo do objeto
        global ordens
        global f
        # Array Auxiliar para o F[x]
        aux = np.array([])
        # Laco de repeticao responsavel por fazer os calculos
        for l in range(0, len(f) - 1):
            f[l] = (f[l + 1] - f[l]) / (x[l + (self.nDeIteracoes + 1)] - x[l])
            aux = np.append(aux, f[l])

        self.ordensAux = np.append(self.ordensAux, aux[0])
        # Substitui o coeficientes da ordem pelos atuais
        ordens = self.ordensAux
        # Atribui os novos y correspondentes à sua ordem
        f = aux
        self.nDeIteracoes += 1
        self.termina()

    def iniciarInterpolacao(self):
        self.calcularDx()

    def termina(self):
        if self.nDeIteracoes < len(x) - 1:
            self.calcularDx()

    def calcularX(self, z):
        r = self.ordensAux[len(self.ordensAux) - 1]
        for i in range(len(self.ordensAux) - 2, -1, -1):
            r = r * (z - x[i]) + self.ordensAux[i]
        return r


# x = np.array([-1, 0, 2])
# f = np.array([4, 1, -1])

var = Interpolacao(x, f, ordens)
var.iniciarInterpolacao()
print('#' * 20)
print(f)
print('[', end='')
for l in range(0, len(ordens)):
    print(f'{ordens[l]:^8.4f}', end='')
print(']')
print("=#" * 20, '\n')

print(var.calcularX(0))
