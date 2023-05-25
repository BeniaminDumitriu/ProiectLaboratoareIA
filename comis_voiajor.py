def citeste_date_intrare(nume_fisier):
    with open(nume_fisier, 'r') as f:
        n = int(f.readline().strip())
        orase = []
        for i in range(n):
            orase.append(f.readline().strip())
        distante = []
        for i in range(n):
            linie = [int(x) for x in f.readline().strip().split()]
            distante.append(linie)
        start = int(f.readline().strip())
        if n < 4:
            print("Matricea trebuie sa aiba cel putin 4 orase.")
            return None
        for i in range(n):
            for j in range(i+1, n):
                if distante[i][j] != distante[j][i]:
                    print("Matricea nu este simetrica.")
                    return None
        print("Datele de intrare citite cu succes:")
        print("Numarul de orase: ", n)
        print("Orasele: ", orase)
        print("Matricea de distante:")
        for i in range(n):
            print(distante[i])
        print("Orasul de start: ", orase[start-1])
        return n, orase, distante, start

def comis_voiajor(n, orase, distante, start):
    import time
    import sys
    
    vizitat = [0] * n
    drum = [start]
    vizitat[start-1] = 1
    DT = 0
    current = start
    t_start = time.time()

    while len(drum) < n:
        dist_min = sys.maxsize
        next_city = None
        for i in range(n):
            if vizitat[i] == 0 and distante[current-1][i] < dist_min:
                dist_min = distante[current-1][i]
                next_city = i+1
        if next_city is None:
            break
        DT += dist_min
        drum.append(next_city)
        vizitat[next_city-1] = 1
        current = next_city

    DT += distante[drum[-1]-1][start-1]
    drum.append(start)

    t_final = time.time()
    timp_executie = t_final - t_start

    print("Solutia problemei:")
    for i in range(len(drum)):
        print(orase[drum[i]-1], end=' ')
        if i < len(drum) - 1:
            print("->", end=' ')
    print("\nDistanta totala a traseului: ", DT)
    print("Timpul de executie: ", timp_executie, " secunde.")


n, orase, distante, start = citeste_date_intrare('comis_voiajor_input1.txt')
if n is not None:
    comis_voiajor(n, orase, distante, start)
