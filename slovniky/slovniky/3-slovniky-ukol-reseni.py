import pytest
#Ukol, uprav nasledujici funkce podle zadani, tak aby prochazely testy
# python -m pytest -v 3-slovniky-ukol-zadani.py

#Funkce musi vratit slovnik, ktery:
# Obsahuje polozku s klicem 'jmeno' a hodnotou 'Chundelac'
# Obsahuje polozku s klicem 'rasa' a libovolnou hodnotou
# Obsahuje polozku s klicem 'Vek' a libovolnou hodnotou
def vytvor_psika():
    return {
        'jmeno':'Chundelac',
        'rasa':'Poulicni smes',
        'vek':3
    }

#Uprav funkci tak, ze:
# Vaha kocky bude 11
# Rasa bude odstranena pomoci prikazu del
# pridej polozku 'vek' s hodnotou 5
def vytvor_kocicku():
    kocicka = {
        'jmeno': 'Drobek',
        'OblibeneKrmivo': 'CatFood Premium Deluxe',
        'vaha': 10,
        'rasa': 'Poulicni smes'
    }


    del kocicka['rasa']
    kocicka['vek'] = 5
    kocicka['vaha'] = 11

    return kocicka


def test_psik_ma_spravne_jmeno():
    pes = vytvor_psika()
    assert pes['jmeno'] == 'Chundelac'

def test_psik_ma_zadanou_rasu():
    pes = vytvor_psika()
    pes['rasa']

def test_psik_ma_zadany_vek():
    pes = vytvor_psika()
    pes['vek']

def test_kocicka_ma_zmenenou_vahu():
    kocka = vytvor_kocicku()
    assert kocka['vaha'] == 11

def test_kocicka_ma_pridany_vek():
    kocka = vytvor_kocicku()
    assert kocka['vek'] == 5

def test_kocicka_ma_odstranenu_rasu():
    kocka = vytvor_kocicku()

    with pytest.raises(KeyError):
        kocka['rasa']
