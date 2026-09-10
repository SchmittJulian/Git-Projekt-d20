import random
wuerfel=random.randint(1, 20)
Damage=random.randint(1,6)
print("Lasst die Würfel entscheiden!")
print(wuerfel)
if(wuerfel) >=10:
    print("hit")
    print("Der Schaden beträgt:", Damage)
if(wuerfel) <10:
    print ("miss")