import random

dlugosc = 0
iloscPop = 20
powtorzenia = 100000


# wczytywanie
def wczytywanie():
    sr = open('berlin52.txt', 'r')
    tablica = sr.read().split('\n')
    nowa = []
    for element in tablica:
        nowa.append(element.split(' '))
    return nowa


def dane(tab):
    tablica = []
    dlugosc = int(tab[0][0])
    idx = 0
    for i in range(dlugosc):
        temp = []
        for j in range(1+idx, dlugosc+1):
            temp.append(int(tab[j][idx]))
        idx += 1
        tablica.append(temp)
    return tablica


tabOdl = dane(wczytywanie())
print(tabOdl)

