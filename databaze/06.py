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
            # TODO kdyz nejsou lokalni fakta, zeptej se uzivatele, zda chce nacist a pokud ano nacti (stejne jako volba nacti)
            # TODO mame ted nejakou opakujici se logiku, kterou muzeme vytknout?
            continue

        print('Fakt o kočkách:', choice(facts))
    elif volba == "nacti":
        print("Nacitam data z API")
        random_facts = facts_api.get_random_facts()
        print("Pocet faktu nactenych z API: "+str(len(random_facts)))
        facts.extend(random_facts)
        print("Pocet faktu po nacteni: "+str(len(facts)))
        # TODO po nacteni dat z API ulozime nova fakta do DB

    elif volba == "smazvse":
        print("Mazu vse")
        # TODO smaz vse i v DB
        facts = []

    elif volba == "pocet":
        print("Pocet faktu: "+str(len(facts)))
        # TODO vrat pocet polozek v databazi

    elif volba == "konec":
        break

    else:
        print(f'Volbu "{volba}" neznám.')


print("Zapisuji fakta do db")
cursor.execute("delete from cat_facts")

# TODO tohle uz nebudeme potrebovat, protoze ukladame prubezne
for fact in facts:
    print(fact)
    cursor.execute("insert into cat_facts values(?)", (fact,))

response = cursor.execute("select * from cat_facts")
print(response.fetchall())
con.commit()


print("Na viděnou příště")