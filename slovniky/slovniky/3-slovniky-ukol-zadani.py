import pytest
#Ukol, uprav nasledujici funkce podle zadani, tak aby prochazely testy
# python -m pytest -v 3-slovniky-ukol-zadani.py

#Funkce musi vratit slovnik, ktery:
    # Obsahuje polozku s klicem 'Jmeno' a hodnotou 'Chundelac'
    # Obsahuje polozku s klicem 'Rasa' a libovolnou hodnotou
    # Obsahuje polozku s klicem 'Vek' a libovolnou hodnotou
def vytvor_psika():
    pass

#Uprav funkci tak, ze:
    # Vaha kocky bude 11
    # Rasa bude odstranena pomoci prikazu del
    # pridej polozku 'Vek' s hodnotou 5
def vytvor_kocicku():
    kocicka = {
        'Jmeno': 'Drobek',
        'OblibeneKrmivo': 'CatFood Premium Deluxe',
        'Vaha': 10,
        'Rasa': 'Poulicni smes'
    }

    return kocicka


def test_psik_ma_spravne_jmeno():
    pes = vytvor_psika()
    assert pes['Jmeno'] == 'Chundelac'

def test_psik_ma_zadanou_rasu():
    pes = vytvor_psika()
    pes['Rasa']

def test_psik_ma_zadany_vek():
    pes = vytvor_psika()
    pes['Vek']

def test_kocicka_ma_zmenenou_vahu():
    kocka = vytvor_kocicku()
    assert kocka['Vaha'] == 11

def test_kocicka_ma_pridany_vek():
    kocka = vytvor_kocicku()
    assert kocka['Vek'] == 5

def test_kocicka_ma_odstranenu_rasu():
    kocka = vytvor_kocicku()

    with pytest.raises(KeyError):
        kocka['Rasa']
