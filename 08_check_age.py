annif = int(input("quel est ton année de naissance ?"))
age  = 2026 - annif
print (f"A la fin de l'année tu auras {age} ans ! ")
if age < 12 :
    print ("tu es un enfant")
if 12 < age <= 17 :
    print ("tu es un adolescent")
else :
    print ("tu es un adulte")