
import random

width = 60

border = "*"
fill = "                                                          "

rando = random.randint(1,59)
rand = random.randint(1,29)


line_n = 60-rando-3
linee = border + rando * " " + "@" + line_n*" " + border
print(linee)

controll = input("Merre szeretnél lépni?")

while controll != "elmennék" :
    line = ""
    print(border * width)
    line = border + fill + border
    for i in range(31):
        print(line)
        if i == rand:
            print(linee)
    print(border * width)
    if rando == 0 or rando >= 57 :
        break
    elif rand == 0 or rand >= 30 :
        break
    controll = input("Merre szeretnél lépni?")
    if controll == "le" :
        rand = rand + 1
    elif controll == "fel" :
        rand = rand - 1
    elif controll == "jobb" :
        rando = rando + 1
    elif controll == "bal" :
        rando = rando - 1


    line_n = 57-rando
    linee = border + rando * " " + "@" + line_n*" " + border



