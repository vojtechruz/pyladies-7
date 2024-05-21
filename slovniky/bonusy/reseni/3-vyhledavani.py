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
# Hledani budeme opakovat dokud nemame zadne vysledky
while len(vysledky) == 0:

    vyhledavany_vyraz = input("Zadej jmeno/cislo nebo jejich cast k vyhledani:\n")

    # Projdeme kazdou polozku ve zlatych stranckach
    for jmeno, cislo in zlate_stranky.items():
        # Prevedeme jmeno na mala pismena pro porovnavani kde velikost nehraje roli
        jmeno_male = jmeno.lower()

        # Pokud vyhledavany vyraz je soucasti jmena nebo cisla pridame ho do vysledku
        # Jmeno pred porovnavani predeveme take na mala pismena
        # Hledany vyraz i jmeno jsou pak male a velikost nehraje roli
        if vyhledavany_vyraz.lower() in jmeno_male or vyhledavany_vyraz in cislo:
            vysledky.append(jmeno)

    if len(vysledky) == 0:
        print("Hledany vyraz nenalezen:", vyhledavany_vyraz)

# Setridime nalezena jmena dle abecedy
vysledky_setridene = sorted(vysledky)

# Vypiseme vysledky jeden po druhem do konzole
for jmeno in vysledky_setridene:
    print(jmeno, ":", zlate_stranky[jmeno])