# Função constante 
# Reutilização, Clareza, Parametrização
# Autor: André Luiz Barbosa (Andrehlb)
# Data: 2025-04-13
# Descrição: Este script cria uma função constante e a plota usando matplotlib.
# -*- coding: utf-8 -*-
# Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Criando valores de x para o gráfico
def constante(valor, tamanho=100, intervalo=(-10, 10)):
    """
    Cria uma função constante com o valor especificado.
    
    Parâmetros:
    valor (float): O valor constante da função.
    tamanho (int): O número de pontos a serem gerados.
    intervalo (tuple): O intervalo para os valores de x.
    
    Retorna:
    numpy.ndarray: Um array de valores constantes.
    """
    x = np.linspace(intervalo[0], intervalo[1], tamanho)
    y= np.full_like(x, valor)
    return x,y

# Gerando x e y para f(x) = 20
x, y = constante(20)

# Plotando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(x,y, label='f(x) = 20', color='deepskyblue')
plt.fill_between(x, y, color='deepskyblue', alpha=0.3)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.title('Função constante: f(x) = 20')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()