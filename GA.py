import math
import random



#function yang ingin di cari minimalnya
def h(x,y):
    return ((math.cos(x) + math.sin(y))**2)/ ((x**2) + (y**2))

#fitness
def fitness(x1, x2):
    x, y = decode(x1,x2)

    result = h(x,y)

    if result == 0:
        return 9999999999999
    else:
        return abs(1/(result+0.1))

#initialize pop
def init_pop(population, size):
    for s in range(size):
        population.append( (random.uniform(0, 1), 
                            random.uniform(0, 1)) )

#decode kromosom
def decode(x1, x2):

    x = -5 + ((5 - (-5))/2) * (x1)
    y = -5 + ((5 - (-5))/2) * (x2)

    return x, y

#parent select pakai tournament
def tournament(ranked):
    best = []
    

    for i in range(10):
        indv = ranked[random.randint(0,size-1)][1]
        if best == [] or fitness(indv[0],indv[1]) > fitness(best[0], best[1]):
            best = indv
    return best

#crossover discrete
def discrete(best, size):
    newGen = []
    for i in range(size):
        e1 = random.choice(best)
        e2 = random.choice(best)

        e1,e2 = mutation(e1,e2)
    
        newGen.append( (e1, e2) )
    return newGen

#mutasi uniform
def mutation(elemen1, elemen2):
    prob1 = random.random()

    if prob1 < 0.1:
        elemen1 = random.uniform(0,1)
    
    prob2 = random.random()

    if prob2 < 0.1:
        elemen2 = random.uniform(0,1)

    
    return elemen1, elemen2
        
        
    


    
size = int(input("Masukkan size populasi yang diinginkan: "))
population = []

init_pop(population, size)

min = 0
hasil = []
iterasi = 0
gen = int(input("Masukkan Maximum Generasi: "))
prev_best = []

#main loop
for i in range(gen):

    rankedsol = []

    #append fitness + kromosom ke list rankedsol
    for s in population:
        rankedsol.append( (fitness(s[0], s[1]), s) )


    #sort rankedsol agar menemukan kromosom dengan fitness tertinggi
    rankedsol.sort()
    rankedsol.reverse()
    print(f"\n=== GEN {i+1} BEST SOLUTIONS === ")

    print("Kromosom = ", rankedsol[0][1])
    print("fitness = ", rankedsol[0][0])
    print(rankedsol[0])

    #cek jika solusi sebelumnya sama seperti solusi generasi sekarang
    if prev_best == rankedsol[0]:
        iterasi += 1

        #jika solusi telah sama sebanyak 3 kali, maka program akan stop
        if iterasi >= 3:
            break

    else:
        iterasi = 0

    best = []
    
    #mencari parent untuk dimasukan ke mating pool
    for j in range(size//2):
        temp = tournament(rankedsol)
        best.append(temp[0])
        best.append(temp[1])


    print("Mating Pool = ", best)
    prev_best = rankedsol[0]
    

    #crossover untuk membuat populasi baru, yang kemudian akan dipakai di generasi selanjutnya
    population = discrete(best, size)
    

print("\n\n\n==== BEST SOLUTION ====")

x,y = decode(rankedsol[0][1][0], rankedsol[0][1][1])
print("Kromosom = ", rankedsol[0][1])
print("Dekode:")
print("x = ", x)
print("y = ", y)
print("fitness = ", rankedsol[0][0])
print("Hasil fungsi = ", h(x,y))




