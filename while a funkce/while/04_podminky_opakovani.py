#Porovnavani - operatory
# ==, !=
# <, >
# <=, >=

vek = int(input("Zadej svuj vek:"))
if vek < 6:
    print("Jizdne zdarma!")
elif vek <= 26:
    print("Studentske jizdne.")
else:
    print("Plna cena.")