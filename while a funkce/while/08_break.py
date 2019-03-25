# break prikaz ukonci predcasne cyklus
# pokud je vice vnorenych cyklu ukonci se ten vnitrni


while True:
    barva = input("Jakou barvu si myslim?")
    if barva == "modra":
        print("Spravne! Byla to modra!")
        break
    else:
        print("Ani nahodou!")

