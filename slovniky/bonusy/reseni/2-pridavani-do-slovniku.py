#Ukol
# - Zeptej se uzivatele na jmeno ktere chce pridat do seznamu
# - Pote se zeptej na telefonni cislo
# - Pridej ziskane polozky do telefoniho seznamu nize
# Bonus: Zkontroluj ze zadane cislo ma 9 znaku, jinak se ptej znovu
# Bonus: Zkontroluj zda dane jmenu v seznamu uz neni. Pokud tam je, ptej se znovu

zlate_stranky = {
    'Alice': '603888921',
    'Bohous': '777891776',
    'Cyril': '602345666',
    'Daniela': '728910000',
    'Eva': '777633798',
    'Filip': '608915433',
}

# Cyklus pro zadavani jmena stale dokola dokud nebude platne
while True:
    # Zeptame se uzivatele na jmeno k pridani
    jmeno = input("Zadej jmeno, ktere chces pridat:\n")

    # Pokud jmeno uz je v seznamu
    if jmeno in zlate_stranky:

        print(jmeno, " uz v seznamu je. Zadej jine jmeno.")
        # Skocime opet na zacatek cyklu,
        # ignoreujeme zbytek cyklu a ptame se znova
        continue

    # Ukoncime cyklus
    break

# Cyklus pro zadavani cisla stale dokola dokud nebude platna
while True:
    # Zeptame se uzivatele na cislo k pridani
    tel_cislo = input("Zadej cislo, ktere chces pridat:\n")

    if len(tel_cislo) != 9:
        print("Telefonni cislo musi mit 9 znaku. Zadej platne cislo.")
        # Skocime opet na zacatek cyklu,
        # ignoreujeme zbytek cyklu a ptame se znova
        continue

    # Muzeme pridat polozku, protoze sem to dojde jen
    # pokud je vse v poradku
    zlate_stranky[jmeno] = tel_cislo
    print("Pridano nove jmeno", jmeno, " s cislem", tel_cislo)

    # Ukoncime cyklus
    break
