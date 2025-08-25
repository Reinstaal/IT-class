from random import randint

target1 = randint (1, 6)
target2 = randint (1, 6)
target3 = randint (1, 6)
targets = target1 + target2 + target3
print(
        "Die drei Glückswürfe des Tages:" ,
        str(target1) , str(target2) , str(target3) ,
        "(Summe:" , str(targets) + ")"
)

Lotto1 = str(randint (1,49))
Lotto2 = str(randint (1,49))
Lotto3 = str(randint (1,49))
Lotto4 = str(randint (1,49))
Lotto5 = str(randint (1,49))
Lotto6 = str(randint (1,49))
print ("Deine Lottozahlen von heute:" , Lotto1 , Lotto2 , Lotto3 , Lotto4 , Lotto5 , Lotto6)