soubor = open('basnicka.txt', encoding='utf-8')

try:
    obsah = soubor.read()
    1/0 #Chyba pri cteni souboru
    print(obsah)
finally:
    print('Zaviram soubor')
    soubor.close()
