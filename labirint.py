f = open("labirint.txt", 'r')

rand = [0, 0, 1, -1]
col = [1, -1, 0, 0]

def citire_fisier():
    global n, intrare, iesire, labirint, solutii
    
    n = int(f.readline()) #dimensiunea matricei
    intrare = [int(y) for y in f.readline().split()]
    iesire = [int(y) for y in f.readline().split()]
    
    solutii = [0]*n
    for i in range (n):
        solutii[i] = [0]*n
        
    labirint = [0]*n
    for i in range (n):
        labirint[i] = [0]*n
        
    for linie in f:
        campuri = [int(y) for y in linie.split()]
        labirint[campuri[0]-1][campuri[1]-1] = campuri[2]
        
def afisare():
    global labirint, n
    for i in range (n):
        for j in range(n):
            print(labirint[i][j], end = ' ')
        print()
        
def gasire_solutii(i, j):
    global n, intrare, iesire, labirint, solutii
    solutii[intrare[0]][intrare[1]] = 5
    if i == iesire[0] and j == iesire[1]:
        for k in range(n):
            for l in range(n):
                print(solutii[k][l], end = '')
            print()
        print('------------------------------')
    else:
        for k in range(n):
            a = i + rand[k]
            b = j + col[k]
            if POSIBIL(a, b):
                gasire_solutii(a, b)
                solutii[a][b] = 0
      
def POSIBIL(i, j):
    global labirint, solutii
    if i >= 0 and i < len(labirint) and j >= 0 and j < len(labirint) and labirint[i][j] == 1 and solutii[i][j] == 0:
        return True;
    return False;
        
def alege_optiune():
    Meniu={}
    Meniu[1]="Citirea din fisier"
    Meniu[2]="Afisarea labirintului"
    Meniu[3]="Rezolvarea labirintului"
    Meniu[4]="Informatii autor"
    Meniu[5]="Exit"
    print()
    for item in Meniu:
        print(str(item)+".",Meniu[item])
    x=int(input("\nAlegeti o optiune "))
    print()
    return x;

while True:
    opt=alege_optiune()
    if opt==1:
        citire_fisier()
        input('press any key : ')
    if opt==2:
        afisare()
        input('press any key')
    if opt==3:
        gasire_solutii(intrare[0], intrare[1])
        input('press any key : ')
    if opt==4:
        print("Dumitriu Beniamin grupa 3131B")
        input('press any key : ')
    if opt==5:
        f.close()
        exit(0) 
    