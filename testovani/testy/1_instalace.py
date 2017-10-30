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
#    - python -m pytest -v 1_instalace.py
#    - uspesne spusteni: ========================== 1 passed in 0.03 seconds ===========================

def secti(a, b):
    return a + b

def test_secti():
    assert secti(1, 2) == 3