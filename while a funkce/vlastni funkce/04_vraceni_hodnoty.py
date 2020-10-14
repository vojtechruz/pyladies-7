def obvod_obdelniku_stary(sirka, vyska):
    "Vypocita obvod obdelniku dane sirky a vysky a zapise do konzole"
    obvod = 2 * (sirka + vyska)
    print("Obvod obdelniku je " + str(obvod))

def obvod_obdelniku(sirka, vyska):
    "Vypocita obvod obdelniku dane sirky a vysky"
    return 2 * (sirka + vyska)

def obvod_kvadru(a,b,c):
    return 2*obvod_obdelniku(a,b) + 4*c

obvod_obdelniku_stary(1, 1)
print(obvod_obdelniku(5, 10))
print(obvod_obdelniku(2, 7)*2)
print(obvod_kvadru(10,5,20))