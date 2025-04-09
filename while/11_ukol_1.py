# Napis program, kdy pocitac bude hazet sestistennou kostkou
# Tak dlouho dokud nepadne 6
# Kazdy hod vypise do konzole
# Kdyz padne 6 uz se dal nehazi a do konzole se vypise "Konec hry!"

# napoveda:
# from random import randrange
# randrange(7)

#Napr.
# 1
# 3
# 3
# 2
# 5
# 6
# Konec hry!


from random import randrange

#Reseni 1
while True:
    hod = randrange(1,7)
    print(hod)
    if hod == 6:
        break


# Reseni 2
hod = 0
while hod != 6:
    hod = randrange(1,7)
    print(hod)
