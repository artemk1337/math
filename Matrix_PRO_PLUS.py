#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import *
import numpy as np
from scipy import linalg
from tkinter import *
try:
    from Tkinter import *
except ImportError:
    pass


"""Начальные данные"""


n_nv = 6
vxv = 10
N1_matr_size = 3


"""Преобразование матриц"""


# Степень
def power():
    ma1tr_input()
    n = int(input('Введите стпепень: '))
    K = np.linalg.matrix_power(aaa_matr, n)
    ma1r_pr1nt(K)


# Собсвенные ветора и значения
def eiq():
    ma1tr_input()
    (V, K) = linalg.eig(aaa_matr)
    round1(V)
    round2(K)
    ma1r_pr1nt(V)
    ma1r_pr1nt1(K)


# Обратная матрица
def inv():
    ma1tr_input()
    K = linalg.inv(aaa_matr)
    round2(K)
    ma1r_pr1nt(K)


# Округление для строки
def round1(C):
    ma1tr_input()
    for k in range(len(C[:])):
        C[k] = round(C[k], 2)


# Округления для матрицы
def round2(C):
    ma1tr_input()
    for i in range(len(C[:, 0])):
        for k in range(len(C[i, :])):
            C[i, k] = round(C[i, k], 2)


# Определитель
def det():
    ma1tr_input()
    K = linalg.det(aaa_matr)
    K = round(K, 2)
    ma1r_pr1nt(K)


# Ранг матрицы
def rank():
    ma1tr_input()
    K = np.linalg.matrix_rank(aaa_matr)
    ma1r_pr1nt(K)


# PLU разложение
def PLU():
    ma1tr_input()
    (P, L, U) = linalg.lu(aaa_matr)
    round2(P)
    round2(L)
    round2(U)
    ma1r_pr1nt(P)
    ma1r_pr1nt1(L)
    ma1r_pr1nt2(U)


# QR разложение
def QR():
    ma1tr_input()
    (Q, R) = linalg.qr(aaa_matr)
    ma1r_pr1nt(Q)
    ma1r_pr1nt1(R)


# Холецкого разложение
def chol():
    ma1tr_input()
    K = linalg.cholesky(aaa_matr)
    ma1r_pr1nt(K)


# Слау
def slau():
    matr2.destroy()
    ma1tr_input()
    P = np.linalg.solve(aaa_matr, bbb_matr)
    ma1r_pr1nt(P)


"""Изменение размера матрицы"""


def matr_size():
    global matrsss
    matrsss = Toplevel(root)
    matrsss.title("Размер матрицы")
    matrsss.geometry("320x200+500+350")
    matrsss.resizable(width=False, height=False)
    Label(matrsss, text=f'Текущий размер матрицы {N1_matr_size}x{N1_matr_size}', width=32, font='Arial 13 bold') \
        .grid(row=0, sticky=W + S + E + N, column=0)
    btn_matrsss1 = Button(matrsss, text='+', font='Arial 18 bold', bg='lightgrey', width=8, command=matr_size_more) \
        .place(x=35, y=40, height=60, width=110)
    btn_matrsss2 = Button(matrsss, text='-', font='Arial 18 bold', bg='lightgrey', width=8, command=matr_size_less) \
        .place(x=180, y=40, height=60, width=110)
    btn_matrsss3 = Button(matrsss, text='Продолжить', font='Arial 16 bold', bg='lightgreen', width=8, command=ma1tr_window) \
        .place(x=35, y=120, height=60, width=255)


def matr_size_more():
    global N1_matr_size
    if N1_matr_size < 9:
        N1_matr_size += 1
    Label(matrsss, text=f'Текущий размер матрицы {N1_matr_size}x{N1_matr_size}', width=32, font='Arial 13 bold') \
        .grid(row=0, sticky=W + S + E + N, column=0)


def matr_size_less():
    global N1_matr_size
    if N1_matr_size > 2:
        N1_matr_size -= 1
    Label(matrsss, text=f'Текущий размер матрицы {N1_matr_size}x{N1_matr_size}', width=32, font='Arial 13 bold') \
        .grid(row=0, sticky=W + S + E + N, column=0)


"""MAIN"""


# Главное окно
def ma1tr_window():
    global matr
    global N1_matr_size
    N1 = N1_matr_size * 64
    N2 = N1_matr_size * 28 + 50
    matr = Toplevel(matrsss)
    matr.title("Квадратное уравнение")
    matr.geometry(f"{N1}x{N2}+400+350")
    matr.resizable(width=False, height=False)
    global Entry_matr_00
    global Entry_matr_01
    global Entry_matr_02
    global Entry_matr_03
    global Entry_matr_04
    global Entry_matr_05
    global Entry_matr_06
    global Entry_matr_07
    global Entry_matr_08
    global Entry_matr_10
    global Entry_matr_11
    global Entry_matr_12
    global Entry_matr_13
    global Entry_matr_14
    global Entry_matr_15
    global Entry_matr_16
    global Entry_matr_17
    global Entry_matr_18
    global Entry_matr_20
    global Entry_matr_21
    global Entry_matr_22
    global Entry_matr_23
    global Entry_matr_24
    global Entry_matr_25
    global Entry_matr_26
    global Entry_matr_27
    global Entry_matr_28
    global Entry_matr_30
    global Entry_matr_31
    global Entry_matr_32
    global Entry_matr_33
    global Entry_matr_34
    global Entry_matr_35
    global Entry_matr_36
    global Entry_matr_37
    global Entry_matr_38
    global Entry_matr_40
    global Entry_matr_41
    global Entry_matr_42
    global Entry_matr_43
    global Entry_matr_44
    global Entry_matr_45
    global Entry_matr_46
    global Entry_matr_47
    global Entry_matr_48
    global Entry_matr_50
    global Entry_matr_51
    global Entry_matr_52
    global Entry_matr_53
    global Entry_matr_54
    global Entry_matr_55
    global Entry_matr_56
    global Entry_matr_57
    global Entry_matr_58
    global Entry_matr_60
    global Entry_matr_61
    global Entry_matr_62
    global Entry_matr_63
    global Entry_matr_64
    global Entry_matr_65
    global Entry_matr_66
    global Entry_matr_67
    global Entry_matr_68
    global Entry_matr_70
    global Entry_matr_71
    global Entry_matr_72
    global Entry_matr_73
    global Entry_matr_74
    global Entry_matr_75
    global Entry_matr_76
    global Entry_matr_77
    global Entry_matr_78
    global Entry_matr_80
    global Entry_matr_81
    global Entry_matr_82
    global Entry_matr_83
    global Entry_matr_84
    global Entry_matr_85
    global Entry_matr_86
    global Entry_matr_87
    global Entry_matr_88
    Entry_matr_00 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_01 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_02 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_03 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_04 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_05 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_06 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_07 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_08 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_10 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_11 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_12 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_13 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_14 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_15 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_16 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_17 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_18 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_20 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_21 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_22 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_23 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_24 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_25 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_26 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_27 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_28 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_30 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_31 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_32 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_33 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_34 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_35 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_36 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_37 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_38 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_40 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_41 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_42 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_43 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_44 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_45 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_46 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_47 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_48 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_50 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_51 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_52 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_53 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_54 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_55 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_56 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_57 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_58 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_60 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_61 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_62 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_63 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_64 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_65 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_66 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_67 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_68 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_70 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_71 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_72 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_73 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_74 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_75 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_76 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_77 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_78 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_80 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_81 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_82 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_83 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_84 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_85 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_86 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_87 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_88 = Entry(matr, width=5, font='Arial 16')
    Entry_matr_00.grid(row=0, column=0, sticky=N)
    Entry_matr_01.grid(row=0, column=1, sticky=N)
    Entry_matr_02.grid(row=0, column=2, sticky=N)
    Entry_matr_03.grid(row=0, column=3, sticky=N)
    Entry_matr_04.grid(row=0, column=4, sticky=N)
    Entry_matr_05.grid(row=0, column=5, sticky=N)
    Entry_matr_06.grid(row=0, column=6, sticky=N)
    Entry_matr_07.grid(row=0, column=7, sticky=N)
    Entry_matr_08.grid(row=0, column=8, sticky=N)
    Entry_matr_10.grid(row=1, column=0, sticky=N)
    Entry_matr_11.grid(row=1, column=1, sticky=N)
    Entry_matr_12.grid(row=1, column=2, sticky=N)
    Entry_matr_13.grid(row=1, column=3, sticky=N)
    Entry_matr_14.grid(row=1, column=4, sticky=N)
    Entry_matr_15.grid(row=1, column=5, sticky=N)
    Entry_matr_16.grid(row=1, column=6, sticky=N)
    Entry_matr_17.grid(row=1, column=7, sticky=N)
    Entry_matr_18.grid(row=1, column=8, sticky=N)
    Entry_matr_20.grid(row=2, column=0, sticky=N)
    Entry_matr_21.grid(row=2, column=1, sticky=N)
    Entry_matr_22.grid(row=2, column=2, sticky=N)
    Entry_matr_23.grid(row=2, column=3, sticky=N)
    Entry_matr_24.grid(row=2, column=4, sticky=N)
    Entry_matr_25.grid(row=2, column=5, sticky=N)
    Entry_matr_26.grid(row=2, column=6, sticky=N)
    Entry_matr_27.grid(row=2, column=7, sticky=N)
    Entry_matr_28.grid(row=2, column=8, sticky=N)
    Entry_matr_30.grid(row=3, column=0, sticky=N)
    Entry_matr_31.grid(row=3, column=1, sticky=N)
    Entry_matr_32.grid(row=3, column=2, sticky=N)
    Entry_matr_33.grid(row=3, column=3, sticky=N)
    Entry_matr_34.grid(row=3, column=4, sticky=N)
    Entry_matr_35.grid(row=3, column=5, sticky=N)
    Entry_matr_36.grid(row=3, column=6, sticky=N)
    Entry_matr_37.grid(row=3, column=7, sticky=N)
    Entry_matr_38.grid(row=3, column=8, sticky=N)
    Entry_matr_40.grid(row=4, column=0, sticky=N)
    Entry_matr_41.grid(row=4, column=1, sticky=N)
    Entry_matr_42.grid(row=4, column=2, sticky=N)
    Entry_matr_43.grid(row=4, column=3, sticky=N)
    Entry_matr_44.grid(row=4, column=4, sticky=N)
    Entry_matr_45.grid(row=4, column=5, sticky=N)
    Entry_matr_46.grid(row=4, column=6, sticky=N)
    Entry_matr_47.grid(row=4, column=7, sticky=N)
    Entry_matr_48.grid(row=4, column=8, sticky=N)
    Entry_matr_50.grid(row=5, column=0, sticky=N)
    Entry_matr_51.grid(row=5, column=1, sticky=N)
    Entry_matr_52.grid(row=5, column=2, sticky=N)
    Entry_matr_53.grid(row=5, column=3, sticky=N)
    Entry_matr_54.grid(row=5, column=4, sticky=N)
    Entry_matr_55.grid(row=5, column=5, sticky=N)
    Entry_matr_56.grid(row=5, column=6, sticky=N)
    Entry_matr_57.grid(row=5, column=7, sticky=N)
    Entry_matr_58.grid(row=5, column=8, sticky=N)
    Entry_matr_60.grid(row=6, column=0, sticky=N)
    Entry_matr_61.grid(row=6, column=1, sticky=N)
    Entry_matr_62.grid(row=6, column=2, sticky=N)
    Entry_matr_63.grid(row=6, column=3, sticky=N)
    Entry_matr_64.grid(row=6, column=4, sticky=N)
    Entry_matr_65.grid(row=6, column=5, sticky=N)
    Entry_matr_66.grid(row=6, column=6, sticky=N)
    Entry_matr_67.grid(row=6, column=7, sticky=N)
    Entry_matr_68.grid(row=6, column=8, sticky=N)
    Entry_matr_70.grid(row=7, column=0, sticky=N)
    Entry_matr_71.grid(row=7, column=1, sticky=N)
    Entry_matr_72.grid(row=7, column=2, sticky=N)
    Entry_matr_73.grid(row=7, column=3, sticky=N)
    Entry_matr_74.grid(row=7, column=4, sticky=N)
    Entry_matr_75.grid(row=7, column=5, sticky=N)
    Entry_matr_76.grid(row=7, column=6, sticky=N)
    Entry_matr_77.grid(row=7, column=7, sticky=N)
    Entry_matr_78.grid(row=7, column=8, sticky=N)
    Entry_matr_80.grid(row=8, column=0, sticky=N)
    Entry_matr_81.grid(row=8, column=1, sticky=N)
    Entry_matr_82.grid(row=8, column=2, sticky=N)
    Entry_matr_83.grid(row=8, column=3, sticky=N)
    Entry_matr_84.grid(row=8, column=4, sticky=N)
    Entry_matr_85.grid(row=8, column=5, sticky=N)
    Entry_matr_86.grid(row=8, column=6, sticky=N)
    Entry_matr_87.grid(row=8, column=7, sticky=N)
    Entry_matr_88.grid(row=8, column=8, sticky=N)
    btn_matr_do = Button(matr, text='Ввести', font='Arial 12 bold', bg='green', width=8, command=ma1tr_window1)\
        .place(x=0, y=N1_matr_size*28.15, height=50, width=N1_matr_size*32)
    btn_matr_exit = Button(matr, text='Выход', font='Arial 12 bold', bg='red', width=8, command=out) \
        .place(x=N1_matr_size*32, y=N1_matr_size*28.15, height=50, width=N1_matr_size*32)
    matr.mainloop()


# Ввод матрицы А
def ma1tr_input():
    global aaa_matr
    aaa_matr = np.zeros((N1_matr_size, N1_matr_size))
    if Entry_matr_00.get() != '':
        aaa_matr[0, 0] = Entry_matr_00.get()
    if Entry_matr_01.get() != '':
        aaa_matr[0, 1] = Entry_matr_01.get()
    if Entry_matr_02.get() != '':
        aaa_matr[0, 2] = Entry_matr_02.get()
    if Entry_matr_03.get() != '':
            aaa_matr[0, 3] = Entry_matr_03.get()
    if Entry_matr_04.get() != '':
        aaa_matr[0, 4] = Entry_matr_04.get()
    if Entry_matr_05.get() != '':
        aaa_matr[0, 5] = Entry_matr_05.get()
    if Entry_matr_06.get() != '':
        aaa_matr[0, 6] = Entry_matr_06.get()
    if Entry_matr_06.get() != '':
            aaa_matr[0, 7] = Entry_matr_07.get()
    if Entry_matr_08.get() != '':
        aaa_matr[0, 8] = Entry_matr_08.get()
    if Entry_matr_10.get() != '':
            aaa_matr[1, 0] = Entry_matr_10.get()
    if Entry_matr_11.get() != '':
        aaa_matr[1, 1] = Entry_matr_11.get()
    if Entry_matr_12.get() != '':
        aaa_matr[1, 2] = Entry_matr_12.get()
    if Entry_matr_13.get() != '':
        aaa_matr[1, 3] = Entry_matr_13.get()
    if Entry_matr_14.get() != '':
        aaa_matr[1, 4] = Entry_matr_14.get()
    if Entry_matr_15.get() != '':
        aaa_matr[1, 5] = Entry_matr_15.get()
    if Entry_matr_16.get() != '':
        aaa_matr[1, 6] = Entry_matr_16.get()
    if Entry_matr_17.get() != '':
        aaa_matr[1, 7] = Entry_matr_17.get()
    if Entry_matr_18.get() != '':
        aaa_matr[1, 8] = Entry_matr_18.get()
    if Entry_matr_20.get() != '':
        aaa_matr[2, 0] = Entry_matr_20.get()
    if Entry_matr_21.get() != '':
        aaa_matr[2, 1] = Entry_matr_21.get()
    if Entry_matr_22.get() != '':
        aaa_matr[2, 2] = Entry_matr_22.get()
    if Entry_matr_23.get() != '':
        aaa_matr[2, 3] = Entry_matr_23.get()
    if Entry_matr_24.get() != '':
        aaa_matr[2, 4] = Entry_matr_24.get()
    if Entry_matr_25.get() != '':
        aaa_matr[2, 5] = Entry_matr_25.get()
    if Entry_matr_26.get() != '':
        aaa_matr[2, 6] = Entry_matr_26.get()
    if Entry_matr_27.get() != '':
        aaa_matr[2, 7] = Entry_matr_27.get()
    if Entry_matr_28.get() != '':
        aaa_matr[2, 8] = Entry_matr_28.get()
    if Entry_matr_30.get() != '':
        aaa_matr[3, 0] = Entry_matr_30.get()
    if Entry_matr_31.get() != '':
        aaa_matr[3, 1] = Entry_matr_31.get()
    if Entry_matr_32.get() != '':
        aaa_matr[3, 2] = Entry_matr_32.get()
    if Entry_matr_33.get() != '':
        aaa_matr[3, 3] = Entry_matr_33.get()
    if Entry_matr_34.get() != '':
        aaa_matr[3, 4] = Entry_matr_34.get()
    if Entry_matr_35.get() != '':
        aaa_matr[3, 5] = Entry_matr_35.get()
    if Entry_matr_36.get() != '':
        aaa_matr[3, 6] = Entry_matr_36.get()
    if Entry_matr_37.get() != '':
        aaa_matr[3, 7] = Entry_matr_37.get()
    if Entry_matr_38.get() != '':
        aaa_matr[3, 8] = Entry_matr_38.get()
    if Entry_matr_40.get() != '':
        aaa_matr[4, 0] = Entry_matr_40.get()
    if Entry_matr_41.get() != '':
        aaa_matr[4, 1] = Entry_matr_41.get()
    if Entry_matr_42.get() != '':
        aaa_matr[4, 2] = Entry_matr_42.get()
    if Entry_matr_43.get() != '':
        aaa_matr[4, 3] = Entry_matr_43.get()
    if Entry_matr_44.get() != '':
        aaa_matr[4, 4] = Entry_matr_44.get()
    if Entry_matr_45.get() != '':
        aaa_matr[4, 5] = Entry_matr_45.get()
    if Entry_matr_46.get() != '':
        aaa_matr[4, 6] = Entry_matr_46.get()
    if Entry_matr_47.get() != '':
        aaa_matr[4, 7] = Entry_matr_47.get()
    if Entry_matr_48.get() != '':
        aaa_matr[4, 8] = Entry_matr_48.get()
    if Entry_matr_50.get() != '':
        aaa_matr[5, 0] = Entry_matr_50.get()
    if Entry_matr_51.get() != '':
        aaa_matr[5, 1] = Entry_matr_51.get()
    if Entry_matr_52.get() != '':
        aaa_matr[5, 2] = Entry_matr_52.get()
    if Entry_matr_53.get() != '':
        aaa_matr[5, 3] = Entry_matr_53.get()
    if Entry_matr_54.get() != '':
        aaa_matr[5, 4] = Entry_matr_54.get()
    if Entry_matr_55.get() != '':
        aaa_matr[5, 5] = Entry_matr_55.get()
    if Entry_matr_56.get() != '':
        aaa_matr[5, 6] = Entry_matr_56.get()
    if Entry_matr_57.get() != '':
        aaa_matr[5, 7] = Entry_matr_57.get()
    if Entry_matr_58.get() != '':
        aaa_matr[5, 8] = Entry_matr_58.get()
    if Entry_matr_60.get() != '':
        aaa_matr[6, 0] = Entry_matr_60.get()
    if Entry_matr_61.get() != '':
        aaa_matr[6, 1] = Entry_matr_61.get()
    if Entry_matr_62.get() != '':
        aaa_matr[6, 2] = Entry_matr_62.get()
    if Entry_matr_63.get() != '':
        aaa_matr[6, 3] = Entry_matr_63.get()
    if Entry_matr_64.get() != '':
        aaa_matr[6, 4] = Entry_matr_64.get()
    if Entry_matr_65.get() != '':
        aaa_matr[6, 5] = Entry_matr_65.get()
    if Entry_matr_66.get() != '':
        aaa_matr[6, 6] = Entry_matr_66.get()
    if Entry_matr_67.get() != '':
        aaa_matr[6, 7] = Entry_matr_67.get()
    if Entry_matr_68.get() != '':
        aaa_matr[6, 8] = Entry_matr_68.get()
    if Entry_matr_70.get() != '':
        aaa_matr[7, 0] = Entry_matr_70.get()
    if Entry_matr_71.get() != '':
        aaa_matr[7, 1] = Entry_matr_71.get()
    if Entry_matr_72.get() != '':
        aaa_matr[7, 2] = Entry_matr_72.get()
    if Entry_matr_73.get() != '':
        aaa_matr[7, 3] = Entry_matr_73.get()
    if Entry_matr_74.get() != '':
        aaa_matr[7, 4] = Entry_matr_74.get()
    if Entry_matr_75.get() != '':
        aaa_matr[7, 5] = Entry_matr_75.get()
    if Entry_matr_76.get() != '':
        aaa_matr[7, 6] = Entry_matr_76.get()
    if Entry_matr_77.get() != '':
        aaa_matr[7, 7] = Entry_matr_77.get()
    if Entry_matr_78.get() != '':
        aaa_matr[7, 8] = Entry_matr_78.get()
    if Entry_matr_80.get() != '':
        aaa_matr[8, 0] = Entry_matr_80.get()
    if Entry_matr_81.get() != '':
        aaa_matr[8, 1] = Entry_matr_81.get()
    if Entry_matr_82.get() != '':
        aaa_matr[8, 2] = Entry_matr_82.get()
    if Entry_matr_83.get() != '':
        aaa_matr[8, 3] = Entry_matr_83.get()
    if Entry_matr_84.get() != '':
        aaa_matr[8, 4] = Entry_matr_84.get()
    if Entry_matr_85.get() != '':
        aaa_matr[8, 5] = Entry_matr_85.get()
    if Entry_matr_86.get() != '':
        aaa_matr[8, 6] = Entry_matr_86.get()
    if Entry_matr_87.get() != '':
        aaa_matr[8, 7] = Entry_matr_87.get()
    if Entry_matr_88.get() != '':
        aaa_matr[8, 8] = Entry_matr_88.get()


# Второе окно
def ma1tr_window1():
    global matr1
    matr1 = Toplevel(matr)
    matr1.title('Выберите действие')
    matr1.geometry("409x350+800+250")
    matr1.resizable(width=False, height=False)
    btn_matr1 = Button(matr1, text='Возведение в степень', font='Arial 12 bold', bg='lightblue', width=40, command=power) \
        .grid(row=0, column=0, sticky=W + S + N + E)
    btn_matr2 = Button(matr1, text='Собственных значения и вектора', font='Arial 12 bold', bg='lightblue', width=40, command=eiq) \
        .grid(row=1, column=0, sticky=W + S + N + E)
    btn_matr3 = Button(matr1, text='Обратная матрица', font='Arial 12 bold', bg='lightblue',
                       width=40, command=inv) \
        .grid(row=2, column=0, sticky=W + S + N + E)
    btn_matr4 = Button(matr1, text='Определитель матрицы', font='Arial 12 bold', bg='lightblue',
                       width=40, command=det) \
        .grid(row=3, column=0, sticky=W + S + N + E)
    btn_matr5 = Button(matr1, text='Ранг матрицы', font='Arial 12 bold', bg='lightblue',
                       width=40, command=rank) \
        .grid(row=4, column=0, sticky=W + S + N + E)
    btn_matr6 = Button(matr1, text='PLU-разложение', font='Arial 12 bold', bg='lightblue',
                       width=40, command=PLU) \
        .grid(row=5, column=0, sticky=W + S + N + E)
    btn_matr7 = Button(matr1, text='QR-разложение', font='Arial 12 bold', bg='lightblue',
                       width=40, command=QR) \
        .grid(row=6, column=0, sticky=W + S + N + E)
    btn_matr8 = Button(matr1, text='Разложение Холецкого', font='Arial 12 bold', bg='lightblue',
                       width=40, command=chol) \
        .grid(row=7, column=0, sticky=W + S + N + E)
    btn_matr8 = Button(matr1, text='Решение системы линейных уравнений', font='Arial 12 bold', bg='lightblue',
                       width=40, command=s1a1u) \
        .grid(row=8, column=0, sticky=W + S + N + E)
    btn_matr9 = Button(matr1, text='Очистить матрицу', font='Arial 12 bold', bg='lightblue',
                       width=40, command=matr_clean_1) \
        .grid(row=9, column=0, sticky=W + S + N + E)


# Очистка матрицы А
def matr_clean_1():
    Entry_matr_00.delete(0, END)
    Entry_matr_01.delete(0, END)
    Entry_matr_02.delete(0, END)
    Entry_matr_03.delete(0, END)
    Entry_matr_04.delete(0, END)
    Entry_matr_05.delete(0, END)
    Entry_matr_06.delete(0, END)
    Entry_matr_07.delete(0, END)
    Entry_matr_08.delete(0, END)
    Entry_matr_10.delete(0, END)
    Entry_matr_11.delete(0, END)
    Entry_matr_12.delete(0, END)
    Entry_matr_13.delete(0, END)
    Entry_matr_14.delete(0, END)
    Entry_matr_15.delete(0, END)
    Entry_matr_16.delete(0, END)
    Entry_matr_17.delete(0, END)
    Entry_matr_18.delete(0, END)
    Entry_matr_20.delete(0, END)
    Entry_matr_21.delete(0, END)
    Entry_matr_22.delete(0, END)
    Entry_matr_23.delete(0, END)
    Entry_matr_24.delete(0, END)
    Entry_matr_25.delete(0, END)
    Entry_matr_26.delete(0, END)
    Entry_matr_27.delete(0, END)
    Entry_matr_28.delete(0, END)
    Entry_matr_30.delete(0, END)
    Entry_matr_31.delete(0, END)
    Entry_matr_32.delete(0, END)
    Entry_matr_33.delete(0, END)
    Entry_matr_34.delete(0, END)
    Entry_matr_35.delete(0, END)
    Entry_matr_36.delete(0, END)
    Entry_matr_37.delete(0, END)
    Entry_matr_38.delete(0, END)
    Entry_matr_40.delete(0, END)
    Entry_matr_41.delete(0, END)
    Entry_matr_42.delete(0, END)
    Entry_matr_43.delete(0, END)
    Entry_matr_44.delete(0, END)
    Entry_matr_45.delete(0, END)
    Entry_matr_46.delete(0, END)
    Entry_matr_47.delete(0, END)
    Entry_matr_48.delete(0, END)
    Entry_matr_50.delete(0, END)
    Entry_matr_51.delete(0, END)
    Entry_matr_52.delete(0, END)
    Entry_matr_53.delete(0, END)
    Entry_matr_54.delete(0, END)
    Entry_matr_55.delete(0, END)
    Entry_matr_56.delete(0, END)
    Entry_matr_57.delete(0, END)
    Entry_matr_58.delete(0, END)
    Entry_matr_60.delete(0, END)
    Entry_matr_61.delete(0, END)
    Entry_matr_62.delete(0, END)
    Entry_matr_63.delete(0, END)
    Entry_matr_64.delete(0, END)
    Entry_matr_65.delete(0, END)
    Entry_matr_66.delete(0, END)
    Entry_matr_67.delete(0, END)
    Entry_matr_68.delete(0, END)
    Entry_matr_70.delete(0, END)
    Entry_matr_71.delete(0, END)
    Entry_matr_72.delete(0, END)
    Entry_matr_73.delete(0, END)
    Entry_matr_74.delete(0, END)
    Entry_matr_75.delete(0, END)
    Entry_matr_76.delete(0, END)
    Entry_matr_77.delete(0, END)
    Entry_matr_78.delete(0, END)
    Entry_matr_80.delete(0, END)
    Entry_matr_81.delete(0, END)
    Entry_matr_82.delete(0, END)
    Entry_matr_83.delete(0, END)
    Entry_matr_84.delete(0, END)
    Entry_matr_85.delete(0, END)
    Entry_matr_86.delete(0, END)
    Entry_matr_87.delete(0, END)


# Ввод матрицы B
def s1a1u1():
    global bbb_matr
    bbb_matr = np.zeros((N1_matr_size, 1))
    if Entry_matr_00.get() != '':
        bbb_matr[0, 0] = Entry_matr_100.get()
    if Entry_matr_01.get() != '':
        bbb_matr[1, 0] = Entry_matr_101.get()
    if Entry_matr_02.get() != '':
        bbb_matr[2, 0] = Entry_matr_102.get()
    if Entry_matr_03.get() != '':
        bbb_matr[3, 0] = Entry_matr_103.get()
    if Entry_matr_04.get() != '':
        bbb_matr[4, 0] = Entry_matr_104.get()
    if Entry_matr_05.get() != '':
        bbb_matr[5, 0] = Entry_matr_105.get()
    if Entry_matr_06.get() != '':
        bbb_matr[6, 0] = Entry_matr_106.get()
    if Entry_matr_06.get() != '':
        bbb_matr[7, 0] = Entry_matr_107.get()
    if Entry_matr_08.get() != '':
        bbb_matr[8, 0] = Entry_matr_108.get()
    slau()


# Третье окно для B
def s1a1u():
    global matr2
    global Entry_matr_100
    global Entry_matr_101
    global Entry_matr_102
    global Entry_matr_103
    global Entry_matr_104
    global Entry_matr_105
    global Entry_matr_106
    global Entry_matr_107
    global Entry_matr_108
    matr2 = Toplevel(matr1)
    matr2.title('B')
    matr2.geometry(f"350x{N1_matr_size * 28 + 75}+800+250")
    matr2.resizable(width=False, height=False)
    Label(matr2, text='Введите матрицу '
                      'свободных членов', width=35, font='Arial 12 bold').grid(row=0, sticky=W+S+E+N, column=0)
    Entry_matr_100 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_101 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_102 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_103 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_104 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_105 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_106 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_107 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_108 = Entry(matr2, width=8, font='Arial 16')
    Entry_matr_100.grid(row=1, column=0, sticky=N)
    Entry_matr_101.grid(row=2, column=0, sticky=N)
    Entry_matr_102.grid(row=3, column=0, sticky=N)
    Entry_matr_103.grid(row=4, column=0, sticky=N)
    Entry_matr_104.grid(row=5, column=0, sticky=N)
    Entry_matr_105.grid(row=6, column=0, sticky=N)
    Entry_matr_106.grid(row=7, column=0, sticky=N)
    Entry_matr_107.grid(row=8, column=0, sticky=N)
    Entry_matr_108.grid(row=9, column=0, sticky=N)
    btn_matr2 = Button(matr2, text='Решить', font='Arial 12 bold', bg='lightblue', width=8, command=s1a1u1) \
        .place(y=N1_matr_size * 28 + 25, height=50, width=350)


"""Вывод матриц"""


def ma1r_pr1nt(s):
    global matr3
    matr3 = Toplevel(matr1)
    matr3.title('Ответ')
    matr3.geometry("700x500+600+230")
    Label(matr3, text=f'{s}', width=50, font='Arial 16 bold').grid(row=0, sticky=N, column=0)


def ma1r_pr1nt1(s):
    Label(matr3, text=f'{s}', width=50, font='Arial 16 bold').grid(row=1, sticky=N, column=0)


def ma1r_pr1nt2(s):
    Label(matr3, text=f'{s}', width=50, font='Arial 16 bold').grid(row=2, sticky=N, column=0)


"""Квадратные уравнения"""


def clean_kv():
    EntryResult1.delete(0, END)
    EntryResult2.delete(0, END)


# Нахождение корней
def kva1drat():
    global f
    a1 = Entry_koef_a.get()
    a1 = int(a1)
    b1 = Entry_koef_b.get()
    b1 = int(b1)
    c1 = Entry_koef_c.get()
    c1 = int(c1)
    """Постройка графика"""
    f = f'{a1}*(x)**2 + {b1}*x + {c1}'
    """ Решает квадратное уравнение """
    D = b1*b1 - 4*a1*c1
    if D >= 0:
        x1 = str((-b1 + sqrt(D)) / (2*a1))
        x2 = str((-b1 - sqrt(D)) / (2*a1))
        clean_kv()
        EntryResult1.insert(0, x1)
        EntryResult2.insert(0, x2)
    else:
        D = sqrt(-D)
        D = (complex(0, D))
        b1 = complex(b1)
        x1 = str((-b1 + D) / (2 * a1))
        x2 = str((-b1 - D) / (2 * a1))
        clean_kv()
        EntryResult1.insert(0, x1)
        EntryResult2.insert(0, x2)
    gra_f()


# Окно ввода
def kva1drat_yr1avn():
    global kv1
    global Entry_koef_a
    global Entry_koef_b
    global Entry_koef_c
    global EntryResult1
    global EntryResult2
    """Окно ввода"""
    kv1 = Toplevel(root)
    kv1.title("Квадратное уравнение")
    kv1.geometry("510x400+800+250")
    kv1.resizable(width=False, height=False)
    Label(kv1, text='Коэффициент a', width=17, font='Arial 12').grid(row=0, sticky=W, column=0)
    Label(kv1, text='Коэффициент b', width=15, font='Arial 12').grid(row=0, sticky=W, column=1)
    Label(kv1, text='Коэффициент c', width=15, font='Arial 12').grid(row=0, sticky=W, column=2)
    Entry_koef_a = Entry(kv1, width=7, font='Arial 16')
    Entry_koef_b = Entry(kv1, width=7, font='Arial 16')
    Entry_koef_c = Entry(kv1, width=7, font='Arial 16')
    EntryResult1 = Entry(kv1, font='Arial 30')
    EntryResult2 = Entry(kv1, font='Arial 30')
    Entry_koef_a.grid(row=1, column=0, sticky=N)
    Entry_koef_b.grid(row=1, column=1, sticky=N)
    Entry_koef_c.grid(row=1, column=2, sticky=N)
    EntryResult1.place(relx=.005, rely=.30, height=100, width=500)
    EntryResult2.place(relx=.005, rely=.57, height=100, width=500)
    Label(kv1, text='x^2 +', font='Arial 16').grid(row=1, column=0, sticky=E)
    Label(kv1, text='x +', font='Arial 16').grid(row=1, column=1, sticky=E)
    Label(kv1, text='= 0', font='Arial 16').grid(row=1, column=4, sticky=W, padx=15)
    btn = Button(kv1, text='Посчитать', font='Arial 16', width=3, command=kva1drat)\
        .grid(row=3, column=0, columnspan=5, sticky=N+W+E, pady=15)
    btn_exit = Button(kv1, text='Выход', font='Arial 16 bold', width=3, command=out, bg='red')\
        .place(relx=.005, rely=.83, height=67, width=500)
    kv1.mainloop()


"""Окно ввода графика"""


# Окно воода функции
def gra_ph11k():
    global gr2
    global EntryF
    gr2 = Toplevel(root)
    gr2.title('Ввод графика')
    gr2.geometry("700x100+400+600")
    gr2.resizable(width=False, height=False)
    Label(gr2, text='Введите функцию:', width=40, font='Arial 12 bold').grid(row=0, sticky=W, column=0)
    Label(gr2, text='f(x) = ', width=5, font='Arial 16').grid(row=1, sticky=W, column=0)
    EntryF = Entry(gr2, width=28, font='Arial 16')
    EntryF.grid(row=1, sticky=E, column=0)

    """Кнопочки"""
    btn = Button(gr2, text='Построить', font='Arial 14 bold', width=10, command=f_get, bg='green') \
        .grid(row=2, column=0, sticky=W + S + N)
    btn_help = Button(gr2, text='Помощь', font='Arial 14 bold', width=10, command=tutorial, bg='lightblue') \
        .grid(row=2, column=0, sticky=S + N)
    btn_exit = Button(gr2, text='Выход', font='Arial 14 bold', width=10, command=out, bg='red') \
        .grid(row=2, column=0, sticky=E + S + N)

    siz1e2()
    btn_size_more = Button(gr2, text='+', font='Arial 12', width=12, command=siz1e1, bg='grey') \
        .grid(row=1, column=1, sticky=N)
    btn_size_less = Button(gr2, text='-', font='Arial 12', width=12, command=siz1e2, bg='grey') \
        .grid(row=2, column=1, sticky=N)

    less1()
    btn_grr_more = Button(gr2, text='Приблизить', font='Arial 11 bold', width=12, command=more1, bg='grey') \
        .grid(row=1, column=2, sticky=N)
    btn_grr_less = Button(gr2, text='Отдалить', font='Arial 11 bold', width=12, command=less1, bg='grey') \
        .grid(row=2, column=2, sticky=N)
    gr2.mainloop()


# Считывания функции + график
def f_get():
    global f
    """Считывания функции"""
    f = EntryF.get()
    gra_f()


# График
def gra_f():
    global vxv
    global f
    global x_1
    global n_nv
    """Ввод размера поля"""
    """Размер поля"""
    n1 = n_nv*100
    """Создание графического окна + оси"""
    gr1 = Toplevel(root)
    gr1.title('График')
    can_v = Canvas(gr1, width=n1, height=n1, bg="lightyellow")
    can_v.create_line((n1/2), n1, (n1/2), 0, width=3, arrow=LAST)
    can_v.create_line(0, (n1/2), n1, (n1/2), width=3, arrow=LAST)
    """Позиция"""
    first_x = -(n1/2)
    m1 = (n1*16)
    """Разметка + построение графика"""
    for i in range(m1):
        if vxv < 8:
            if (i % (m1/20)) == 0:
                k = first_x + ((1/(m1/1000)) * i)
                # Разметка
                can_v.create_line(k*vxv + (n1/2), -3 + (n1/2), k*vxv + (n1/2), 3 + (n1/2), width=1, fill='black')
                can_v.create_text(k*vxv + (n1/2) + 15, -10 + (n1/2), text=str(k), fill="red", font="Arial 10")
                if k != 0:
                    # Разметка
                    can_v.create_line(-3 + (n1/2), k*vxv + (n1/2), 3 + (n1/2), k*vxv + (n1/2), width=1, fill='black')
                    can_v.create_text(20 + (n1/2), k*vxv + (n1/2), text=str(k), fill="red", font="Arial 10")
        if (vxv >= 8) and (vxv < 20):
            if (i % (m1/100)) == 0:
                k = first_x + ((1/(m1/1000)) * i)
                # Разметка
                can_v.create_line(k*vxv + (n1/2), -3 + (n1/2), k*vxv + (n1/2), 3 + (n1/2), width=1, fill='black')
                can_v.create_text(k*vxv + (n1/2) + 15, -10 + (n1/2), text=str(k), fill="red", font="Arial 10")
                if k != 0:
                    # Разметка
                    can_v.create_line(-3 + (n1/2), k*vxv + (n1/2), 3 + (n1/2), k*vxv + (n1/2), width=1, fill='black')
                    can_v.create_text(20 + (n1/2), k*vxv + (n1/2), text=str(k), fill="red", font="Arial 10")
        if (vxv >= 20) and (vxv < 40):
            if (i % (m1/500)) == 0:
                k = first_x + ((1/(m1/1000)) * i)
                # Разметка
                can_v.create_line(k*vxv + (n1/2), -3 + (n1/2), k*vxv + (n1/2), 3 + (n1/2), width=1, fill='black')
                can_v.create_text(k*vxv + (n1/2) + 15, -10 + (n1/2), text=str(k), fill="red", font="Arial 10")
                if k != 0:
                    # Разметка
                    can_v.create_line(-3 + (n1/2), k*vxv + (n1/2), 3 + (n1/2), k*vxv + (n1/2), width=1, fill='black')
                    can_v.create_text(20 + (n1/2), k*vxv + (n1/2), text=str(k), fill="red", font="Arial 10")
        if vxv >= 40:
            if (i % (m1 / 1000)) == 0:
                k = first_x + ((1 / (m1 / 1000)) * i)
                # Разметка
                can_v.create_line(k * vxv + (n1 / 2), -3 + (n1 / 2), k * vxv + (n1 / 2), 3 + (n1 / 2), width=1,
                                  fill='black')
                can_v.create_text(k * vxv + (n1 / 2) + 15, -10 + (n1 / 2), text=str(k), fill="red", font="Arial 10")
                if k != 0:
                    # Разметка
                    can_v.create_line(-3 + (n1 / 2), k * vxv + (n1 / 2), 3 + (n1 / 2), k * vxv + (n1 / 2), width=1,
                                      fill='black')
                    can_v.create_text(20 + (n1 / 2), k * vxv + (n1 / 2), text=str(k), fill="red", font="Arial 10")

        """Построение графика"""
        try:
            x = (first_x + ((1/(m1/1000)) * i))
            if (x > -n_nv * 100) or (x < n_nv * 100):
                x_1 = (first_x + ((1/(m1/1000)) * i))/vxv
                per()
                y = (-eval(new_f))*vxv + (n1/2)
                x += (n1/2)
                can_v.create_oval(x, y, x + 1, y + 1, fill='black')
                can_v.pack()
        except Exception:
            gr1.destroy()
            pass                            # Пока что без вывода ошибки в отдельном окне


# Исправление ошибок при вводе
def per():
    global new_f
    new_f = f.replace('x', str(x_1))
    new_f = new_f.replace('^', '**')
    new_f = new_f.replace('Sin', 'sin')
    new_f = new_f.replace('Cos', 'cos')
    new_f = new_f.replace('exp', 'e**')
    new_f = new_f.replace('ln', 'log')


# Кнопка помощь
def tutorial():
    gr1 = Toplevel(root)
    gr1.title('Туториал')
    gr1.geometry("200x180+900+300")
    gr1.resizable(width=False, height=False)
    Label(gr1, text='f(x) = sin(x)', width=22, font='Arial 12').grid(row=0, sticky=N, column=0)
    Label(gr1, text='f(x) = cos(x)', width=22, font='Arial 12').grid(row=1, sticky=N, column=0)
    Label(gr1, text='f(x) = log(x)', width=22, font='Arial 12').grid(row=5, sticky=N, column=0)
    Label(gr1, text='f(x) = (e)^(x)', width=22, font='Arial 12').grid(row=3, sticky=N, column=0)
    Label(gr1, text='f(x) = (x)^(2) + (x)', width=22, font='Arial 12').grid(row=4, sticky=N, column=0)
    Label(gr1, text='f(x) = cosh(x)', width=22, font='Arial 12').grid(row=2, sticky=N, column=0)
    Label(gr1, text='f(x) = sin(pi + 0.5*(x))*10', width=22, font='Arial 12').grid(row=6, sticky=N, column=0)


# Очистка строки ввода
def clean_gr():
    EntryF.delete(0, END)


"""Изменение размера поля графика и прближения графика"""


def siz1e1():
    global n_nv
    if n_nv < 10:
        n_nv += 1
    Label(gr2, text=f'Размер поля: {n_nv-5}', width=18, font='Arial 10 bold').grid(row=0, sticky=W, column=1)


def siz1e2():
    global n_nv
    if n_nv > 5:
        n_nv -= 1
    Label(gr2, text=f'Размер поля: {n_nv-5}', width=18, font='Arial 10 bold').grid(row=0, sticky=W, column=1)


def more1():
    global vxv
    if vxv < 60:
        vxv += 2
    Label(gr2, text=f'Увеличение х{vxv}', width=17, font='Arial 10 bold').grid(row=0, sticky=W, column=2)


def less1():
    global vxv
    if vxv > 1:
        vxv -= 2
    Label(gr2, text=f'Увеличение х{vxv}', width=18, font='Arial 10 bold').grid(row=0, sticky=W, column=2)


"""Выход из программы"""


def out():
    exit()


"""Создание главного окна ввода"""

root = Tk()
root.title('Ввод графика')
root.geometry("609x203+400+400")
root.resizable(width=False, height=False)

btn_root1 = Button(root, text='Построить график функции f(x)', font='Arial 18 bold', width=40, command=gra_ph11k, bg='lightgreen') \
        .grid(row=0, column=0, sticky=W + S + N)
btn_root2 = Button(root, text='Посчитать квадратное уравнение', font='Arial 18 bold', width=40, command=kva1drat_yr1avn, bg='lightgreen') \
        .grid(row=1, column=0, sticky=W + S + N)
btn_root3 = Button(root, text='Преобразование матриц', font='Arial 18 bold', width=40, command=matr_size, bg='lightgreen') \
        .grid(row=2, column=0, sticky=W + S + N)
btn_root4 = Button(root, text='Выход', font='Arial 18 bold', width=40, command=out, bg='red') \
        .grid(row=3, column=0, sticky=W + S + N)


root.mainloop()
