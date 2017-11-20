import pytest
#Ukol, uprav nasledujici funkce podle zadani, tak aby prochazely testy
# python -m pytest -v 3-slovniky-ukol-zadani.py

#Funkce musi vratit slovnik, ktery:
    # Obsahuje polozku s klicem 'Jmeno' a hodnotou 'Chundelac'
    # Obsahuje polozku s klicem 'Rasa' a libovolnou hodnotou
    # Obsahuje polozku s klicem 'Vek' a libovolnou hodnotou
def vytvorPsika():
    pass

#Uprav funkci tak, ze:
    # Vaha kocky bude 11
    # Rasa bude odstranena pomoci prikazu del
    # pridej polozku 'Vek' s hodnotou 5
def vytvorKocicku():
    kocicka = {
        'Jmeno': 'Drobek',
        'OblibeneKrmivo': 'CatFood Premium Deluxe',
        'Vaha': 10,
        'Rasa': 'Poulicni smes'
    }

    return kocicka


def test_PsikMaSpravneJmeno():
    pes = vytvorPsika()
    assert pes['Jmeno'] == 'Chundelac'

def test_PsikMaZadanouRasu():
    pes = vytvorPsika()
    pes['Rasa']

def test_PsikMaZadanyVek():
    pes = vytvorPsika()
    pes['Vek']

def test_KocickaMaZmenenouVahu():
    kocka = vytvorKocicku()
    assert kocka['Vaha'] == 11

def test_KocickaMaPridanyVek():
    kocka = vytvorKocicku()
    assert kocka['Vek'] == 5

def test_KocickaMaOdstranenuRasu():
    kocka = vytvorKocicku()

    with pytest.raises(KeyError):
        kocka['Rasa']
