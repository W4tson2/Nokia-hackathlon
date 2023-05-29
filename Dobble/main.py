

szam = int(input("mennyi"))
item = ""

list = []
while len(list) != szam:
    rand = random.randint(0, 10)
    while rand not in list:
        list.append(rand)
rendo = random.randint(0, szam - 1)
item = list[rendo]
print(list)



true = True


while true == True:
    lista = []
    while len(lista) != szam :
        rand = random.randint(0, 10)
        while rand not in lista :
            lista.append(rand)
            ran = random.randint(0,szam-1)
    while item not in lista :
        lista[ran] = item
        rendo = random.randint(0, szam - 1)
        item = lista[rendo]
    print(lista)


    rand = random.randint(0,10)
    while rand not in lista :
        lista.append(rand)







