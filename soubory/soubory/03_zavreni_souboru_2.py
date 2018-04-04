def iniciala():
    """Vrátí první písmeno v daném souboru."""

    soubor = open('basnicka.txt', encoding='utf-8')
    try:
        obsah = soubor.read()
        return obsah[0]
    finally:
        # Finally blok se provede i po prikazu return!
        print('Zaviram soubor')
        soubor.close()

print(iniciala())