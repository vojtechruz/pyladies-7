# Ukol
# Zeptej se uzivatele na vyhledavany vyraz
# Pote vypis jmeno a telefonni cislo pro vsechny osoby, kde:
# - vyhledavany vyraz je obsazen ve jmene
# - Vyhledavany vyraz je obsazen v telefonnim cisle
# Bonus: - udelej vyhledavani tak, aby nezalezelo na velkych/malych pismenech
# Bonus: - vypis vysledky hledani podle abecedy (podle jmena)
# Bonus: - pokud neni nic nalezeno upozorni uzivatele hlaskou a zeptej se znovu
#          na hledany vyraz

zlate_stranky = {
    'Filip': '608915433',
    'Alice': '603888921',
    'Daniela': '728910000',
    'Cyril': '602345666',
    'Bohous': '777891776',
    'Eva': '777633798'
}

vysledky = []
while len(vysledky) == 0:

    vyhledavany_vyraz = input("Zadej jmeno/cislo nebo jejich cast k vyhledani:\n")

    for jmeno, cislo in zlate_stranky.items():
        jmeno_male = jmeno.lower()

        if vyhledavany_vyraz.lower() in jmeno_male or vyhledavany_vyraz in cislo:
            vysledky.append(jmeno)

    print("Hledany vyraz nenalezen:", vyhledavany_vyraz)


vysledky_setridene = sorted(vysledky)

for jmeno in vysledky_setridene:
    print(jmeno, ":", zlate_stranky[jmeno])