
chat = "Pizza ChatBot:"

print(chat)
print(("Üdvözöllek a pizza éttermünkben, kérlej válassz pizzát."))
a = input("(sonkás,kukoricás,hagymás)")
for i in a :
    asd = ""
    dsa = ""
    asd += a.lower()

def asdasd(asd,dsa,chat) :
    if "sonkás" in asd :
        dsa += "sonkás"
        print("rendben akkor", dsa ,"pizzád lesz")
    elif "kukoricás" in asd :
        dsa += "kukoricás"
        print("rendben akkor", dsa ,"pizzád lesz")
    elif "hagymás" in asd :
        dsa += "hagymás"
        print("rendben akkor", dsa ,"pizzád lesz")
    else:
        print("sajnos nem találok ilyen pizzát")
        quit()
    return chat
sda = print(asdasd(asd,dsa,chat))

b = input("(kicsi,közepes,nagy) Mekkora legyen?")
for k in b :
    sdf = ""
    fds = ""
    sdf += b.lower()
def fdsfds(sdf,fds,chat) :
    if "nagy" in sdf :
        fds += "nagy"
        print(fds, "méretű lesz")
    elif "közepes" in sdf :
        fds += "közepes"
        print(fds, "méretű lesz")
    elif "kicsi" in sdf :
        fds += "kicsi"
        print(fds, "méretű lesz")
    else:
        print("sajnos nem találok iylen méretet")
        quit()
    return chat
dfs = print(fdsfds(sdf,fds,chat))

c = input("(kóla,fanta) Rendelésedhez jár még valamilyen ital amit itt tudsz kiválasztani.")
for s in c :
    gfd = ""
    dfg = ""
    gfd += c.lower()
def gfdgfd(gfd,dfg,chat) :
    if "kóla" in gfd:
        dfg += "kóla"
        print(dfg," italt kapsz mellé" )
    elif "fanta" in gfd:
        dfg += "fanta"
        print(dfg,"italt kapsz mellé" )
    else:
        print("nem találok ilyen hozzávalót")
        quit()
    return chat
fgd = print(gfdgfd(gfd, dfg,chat))

c = input("Az összesítést:")
hjk = ""
kjh = ""
hjk += c.lower()
def hjkhjk(hjk,kjh):
    if "igen" in hjk:
        kjh = print("Az összesítés:", chat,sda,dfs, fgd)
    return kjh

sda = print(asdasd(asd,dsa,chat))
dfs = print(fdsfds(sdf,fds,chat))
fgd = print(gfdgfd(gfd, dfg,chat))
print("köszönjük hogy nálunk rendelt")






