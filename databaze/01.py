import cat_facts

# Tohle je pocatecni stav naseho programu, ktery budeme postupne vylepsovat

facts_api = cat_facts.CatFacts()

facts = facts_api.get_random_facts()

while True:
    print('Vitej v nejlepsi kocici encyklopedii Cat Facts 9000. Co si prejes udelat?')
    print('Dostupne prikazy: fakt, konec')
    volba = input('Zadej prikaz: ')
    volba = volba.lower().strip()

    if volba == 'fakt':
        # TODO - zobrazit nahodny fakt z lokalniho senzamu
        pass
    elif volba == "nacti":
        # TODO - Nacist z API a pridat do seznamu
        pass
    elif volba == "smazvse":
        # TODO - smazat lokalni seznam faktu
        pass
    elif volba == "pocet":
        # TODO - smazat lokalni seznam faktu
        pass
    elif volba == "konec":
        break
    else:
        print(f'Volbu "{volba}" neznám.')

print("Na viděnou příště")
