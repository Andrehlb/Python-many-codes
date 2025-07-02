# Função TRigonometria
# Criador: André Luiz Barbosa (Andrehlb)
# Data: 2025-04-14
# Descrição: Este script cria uma função trigonométrica e a plota usando matplotlib.
# -*- coding: utf-8 -*-
# Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Criando valores de x para o gráfico
x = np.linspace(0,4 * np.pi, 500)
y = np.sin(x)

plt.plot(x,y)
plt.title("Fução seno: f(x) = sin(x)")
plt.xlabel("x (rad)")
plt.ylabel("f(x)")
plt.grid(True)
plt.axvline(x=2 * np.pi, color='red', linestyle='--', label='Período = 2π')
plt.legend()
plt.show()