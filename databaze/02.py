import cat_facts
from random import choice

# Tady jsme doplnili fukncionalitu z predesleho ukolu

facts_api = cat_facts.CatFacts()

facts = facts_api.get_random_facts()

while True:
    print("-------------------------------------------------------------------------")
    print('Vitej v nejlepsi kocici encyklopedii Cat Facts 9000. Co si prejes udelat?')
    print('Dostupne prikazy: fakt, konec, nacti, pocet, smazvse')
    volba = input('Zadej prikaz: ')
    volba = volba.lower().strip()

    if volba == 'fakt':
        if len(facts) == 0:
            print("Nemam zadna fakta")
            continue

        print('Fakt o kočkách:', choice(facts))
    elif volba == "nacti":
        print("Nacitam data z API")
        random_facts = facts_api.get_random_facts()
        print("Pocet faktu nactenych z API: "+str(len(random_facts)))
        facts.extend(random_facts)
        print("Pocet faktu po nacteni: "+str(len(facts)))

    elif volba == "smazvse":
        print("Mazu vse")
        facts = []

    elif volba == "pocet":
        print("Pocet faktu: "+str(len(facts)))

    elif volba == "konec":
        break

    else:
        print(f'Volbu "{volba}" neznám.')

print("Na viděnou příště")