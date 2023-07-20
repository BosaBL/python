#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import sympy as sym
import numpy as np


def formatter(y, pos, list):
    for element in list:
        if y == element[0]:
            return element[1]
    return y


fig, ax = plt.subplots()
# (comienzo, fin, datos)
t = np.linspace(0, 30, 50000)
# Función
v = ((80*9.8)/(10))*(1-np.exp((-10/80)*t))  # Función
# Definiendo la variable x (para utilizar sympy)
x = sym.Symbol('x')
# Redefiniendo la función para evaluar con sympy
v_2 = ((80*9.8)/(10))*(1-sym.exp((-10/80)*x))
lim_infty = sym.limit(v_2, x, sym.oo).n()
# Evaluando $\lim_{t\to\infty}$
plt.axhline(y=lim_infty, color='b', linestyle='dashed')
# Velocidad Terminal
plt.gca().yaxis.set_major_formatter(
    mpl.ticker.FuncFormatter(lambda x, y: formatter(x, y, list=[[lim_infty.n(), 'asd']])))
plt.plot(t, v)
# Graficar
plt.show()
# Mostrar gráfica
