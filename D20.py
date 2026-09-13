import random
wuerfel=random.randint(1, 20)
Damage=random.randint(1,6)
print("Lasst die Würfel entscheiden!")
print(wuerfel)
if(wuerfel) >=10:
    print("Treffer!")
    if (wuerfel)==20: 
        print("kritischer Treffer!")
        print("Du Hast") 
        print(Damage*2) 
        print("Schaden verursacht!")
    else:
        print("Du Hast")
        print(Damage)
        print("Schaden verursacht!")
if(wuerfel) <10:
    print ("miss")