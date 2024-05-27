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
    elif volba == "nacti":
        print("Nacitam data z API")
        random_facts = facts_api.get_random_facts()
        print("Pocet faktu nactenych z API: "+str(len(random_facts)))
        facts.extend(random_facts)
        print("Pocet faktu po nacteni: "+str(len(facts)))

        for fact in random_facts:
            cursor.execute("insert into cat_facts values(?)", (fact,))

    elif volba == "smazvse":
        print("Mazu vse")
        facts = []
        cursor.execute("delete from cat_facts")

    elif volba == "pocet":
        pocet = cursor.execute("select count(*) from main.cat_facts").fetchone()[0]
        print("Pocet faktu: "+str(pocet))

    elif volba == "konec":
        break

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