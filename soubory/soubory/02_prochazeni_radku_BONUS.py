print('Slyšela jsem tuto básničku:')
print()
soubor = open('basnicka.txt', encoding='utf-8')

for radek in soubor:
    print('    ' + radek)
soubor.close()
print()
print('Jak se ti líbí?')

# BONUS: Misto prazdnych mezer pred kazdy radek napis cislo radku cislovane od jednicky, napr: