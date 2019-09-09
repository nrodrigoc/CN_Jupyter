import numpy as np
import matplotlib.pyplot as plt

# Metodo de Newton
# Pn(x) = d0 + d1(x-x0) + d2(x-x0)*(x-x2) + ...
# d0 = x0
# d1 = f[x0,x1] = (f[x1] - f[x0]) / x1 - x0
# d2 = f[x0, x1, x2] = (f[x1,x2] - f[x0,x1]) / x2 - x0

# Definição dos parâmetros
x = np.array([1991.0, 1996, 2000])
f = np.array([497600.0, 549363.0, 597934.0])

# Array com primeiro elemento d0 sendo x0
d = np.array([f[0]])

print('\n\n', '#'*5, 'Eixo das abscissas', '#'*5, end='\n\n     [ ')
for i in range(len(x)):
    print(f'{x[i]:.0f}', end=' ')
print(']\n\n', '#' * 29, '\n')

print('#'*5, 'Eixo das ordenadas', '#'*5, end='\n\n   [ ')
for i in range(len(x)):
    print(f'{f[i]:.0f}', end=' ')
print(']\n\n', '#' * 29, '\n')


class Interpolacao(object):

    def __init__(self, x, f, dAux):
        self.x = x
        self.f = f
        # O parâmetro dAux apenas recebe o array que está com o d0
        self.dAux = dAux
        # N de vezes que o método calcularDx procura cada os valores de cada ordem
        self.nDeIteracoes = 0

    def calcularDx(self):
        # Pega as variáveis definidas fora do escopo da classe
        global d
        global f
        # Array Auxiliar para o F[x]
        aux = np.array([])
        # Laço de repetição responsável por fazer os cálculos
        for l in range(0, len(f) - 1):
            f[l] = (f[l + 1] - f[l]) / (x[l + (self.nDeIteracoes + 1)] - x[l])
            aux = np.append(aux, f[l])

        self.dAux = np.append(self.dAux, aux[0])
        # Substitui o coeficientes da ordem pelos atuais
        d = self.dAux
        # Atribui os novos y correspondentes à sua ordem
        f = aux
        self.nDeIteracoes += 1
        self.termina()

    def termina(self):
        if self.nDeIteracoes < len(x) - 1:
            self.calcularDx()

    def calcularX(self, z):
        if (z > x[0]) and (z < x[len(x) - 1]):
            r = self.dAux[len(self.dAux) - 1]
            for i in range(len(self.dAux) - 2, -1, -1):
                r = r * (z - x[i]) + self.dAux[i]
            print(f'\nPn({z}) =', f'{r:.0f}')
        else:
            print('O valor nao esta contido no intervalo')


# x = np.array([-1, 0, 2])
# f = np.array([4, 1, -1])

var = Interpolacao(x, f, d)
var.calcularDx()

print('#'*8, 'Coeficientes', '#'*8, end='\n\n')
for i in range(len(d)):
    print(f'    d{i} = {d[i]:.0f}')
print('\n', '#' * 29, '\n')

print('Equacao geral: ')
print(f'Pn(x) = {d[0]:.0f} + {d[1]:.0f}*(X - {x[0]:.0f}) + {d[2]:.0f}*(X - {x[0]:.0f})*(X - {x[1]:.0f})\n')

var.calcularX(2005)
