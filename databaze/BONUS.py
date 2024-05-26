import cat_facts
from random import choice
import sqlite3

facts_api = cat_facts.CatFacts()

con = sqlite3.connect("05.db")

cursor = con.cursor()

cursor.execute("create table if not exists cat_facts (fact)")

facts_raw = cursor.execute("select * from cat_facts").fetchall()

facts = []
for fact in facts_raw:
    facts.append(fact[0])

# print(facts)

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
        # TODO potom co se ukaze fakt, tak se zeptej uzivatele zda si preje
        # - smazat fakt - lokalne i z db
        # - ulozit fakt mezi oblibene (Muzeme pridat novy sloupec je_oblibeny jako Boolean - true or false)
        # - pokud je fakt uz oblibeny, tak ho odstranit z oblibenych



    elif volba == "nacti":
        print("Nacitam data z API")
        random_facts = facts_api.get_random_facts()
        print("Pocet faktu nactenych z API: "+str(len(random_facts)))
        facts.extend(random_facts)
        print("Pocet faktu po nacteni: "+str(len(facts)))
        # TODO zde budeme ukladat s faktem novou hodnotu - zda pochazi z api nebo od uzivatele

    elif volba == "smazvse":
        print("Mazu vse")
        facts = []

    elif volba == "pocet":
        print("Pocet faktu: "+str(len(facts)))

    elif volba == "konec":
        break
    # TODO nova volba - zobraz oblibena fakta
    # TODO nova volba pridej novy uzivatelsky fakt, zde budeme ukladat s faktem novou hodnotu - zda pochazi z api nebo od uzivatele
    # TODO nova volba - zobraz vsecna rucne vlozena fakta
    else:
        print(f'Volbu "{volba}" neznám.')


print("Zapisuji fakta do db")
cursor.execute("delete from cat_facts")

for fact in facts:
    print(fact)
    cursor.execute("insert into cat_facts values(?)", (fact,))

response = cursor.execute("select * from cat_facts")
print(response.fetchall())
con.commit()


print("Na viděnou příště")