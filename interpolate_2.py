#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def main():
    global x
    global y
    load()
    x = f[0, :]
    y = f[1, :]
    interpolate1()
    plot()


def load():
    global f
    f = np.loadtxt('Grafik.txt')


def interpolate1():
    global x1
    global func1
    x1 = np.arange(x[0], x[-1], (x[1] - x[0]) / 10)
    func1 = interp1d(f[0, :], f[1, :], kind='cubic')


def plot():
    plt.plot(f[0, :], f[1, :], 'o', x1, func1(x1), '-', linewidth=2,  markersize=5)
    plt.legend(['data', 'cubic'], loc='best')
    plt.show()


main()
