import random

def wczytaj():
    berlin = open('berlin52.txt', 'r')
    tablica = berlin.read().split('\n')
    nowa = []
    for element in tablica:
        nowa.append(element.split(' '))
    return nowa

wczytane = wczytaj()
matrix = []
temp = []
for element in wczytane:
    temp = []
    for i in element:
        temp.append(int(i))
    matrix.append(temp)
print(matrix)

def trasa(macierz):
    dlugosc = 0
    for i in range(2, len(macierz)):
        dlugosc += macierz[i][-2]
    return dlugosc+macierz[-1][0]


def losowanie(macierz, liczba):
    osobniki = []
    return osobniki

print(trasa(matrix))
print(losowanie(matrix, 20))