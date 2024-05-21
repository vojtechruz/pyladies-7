#Ukol
# - Zeptej se uzivatele na jmeno, ktere chce vyhledat. Vrat mu prislusne telefonni cislo
# Bonus: Pokud zadane jmeno v seznamu neni, informuj uzivatele a ptej se znovu

zlate_stranky = {
    'Alice': '603888921',
    'Bohous': '777891776',
    'Cyril': '602345666',
    'Daniela': '728910000',
    'Eva': '777633798',
    'Filip': '608915433',
}

# Zeptame se uzivatele na hledane jmeno
hledane_jmeno = input("Zadej jmeno, ktere chces vyhledat:\n")
print("Hledam jmeno ", hledane_jmeno, "ve zlatych strankach...")

if hledane_jmeno in zlate_stranky:
    # Pokud v seznamu jmeno je
    print(hledane_jmeno, " ma telefonni cislo", zlate_stranky[hledane_jmeno])
else:
    # Pokud v seznamu jmeno neni
    print(hledane_jmeno, "v seznamu neni!")