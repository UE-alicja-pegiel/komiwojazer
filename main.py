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
print('matrix: ', matrix)


def trasa(macierz):
    dlugosc = 0
    for i in range(2, len(macierz)):
        dlugosc += macierz[i][-2]
    return dlugosc+macierz[-1][0]


def losowanie(macierz, liczba):
    osobniki = []
    wybrane = []
    for i in range(liczba+1):
        wybor = random.choice(range(2, macierz[0][0]))

        while wybor in wybrane:
            wybor = random.choice(range(2, macierz[0][0]))

        wybrane.append(wybor)

        if len(wybrane) == 1:
            dlugosc = macierz[wybor][-1]

        elif len(wybrane) == liczba+1:
            osobniki = osobniki[1:]
            indeks = -(abs(wybor - wybrane[0]) + 1)
            if wybrane[0] > wybor:
                dlugosc = macierz[wybrane[0]][indeks]
            else:
                dlugosc = macierz[wybor][indeks]

        else:
            indeks = -(abs(wybor - wybrane[i-1]) + 1)
            if wybrane[i-1] > wybor:
                dlugosc = macierz[wybrane[i-1]][indeks]
            else:
                dlugosc = macierz[wybor][indeks]
        osobniki.append(dlugosc)
    print(wybrane)
    return osobniki


osobniki = losowanie(matrix, 20)
print(osobniki)

