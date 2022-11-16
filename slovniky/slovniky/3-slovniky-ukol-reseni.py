import pytest
#Ukol, uprav nasledujici funkce podle zadani nize

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



# Bonus: Zkontroluj spravnost sve implementace pomoci testu
# 1. Ujistete se, ze mate vytvorene virtualni prostredi 'venv'
#     - Instrukce zde: http://naucse.python.cz/2017/pyladies-praha-podzim-cznic/beginners/install/windows/
#     - Prikaz k vytvoreni: py -3 -m venv venv
#     - K aktivaci: \venv\Scripts\activate
#     - Pokud je venv aktivni, na zacatku prikazove radky se ukaze (venv)
#
# 2. Instalujte knihovnu pytest
#     - python -m pip install pytest
#     - Pokud je vse v poradku: Successfully installed colorama-0.3.9 py-1.4.34 pytest-3.2.3
#
# 3. Spousteni testu
#    - python -m pytest -v [jmeno-souboru.py]
#    - python -m pytest -v 3-slovniky-ukol-reseni.py
#    - uspesne spusteni: ========================== 1 passed in 0.03 seconds ===========================




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
