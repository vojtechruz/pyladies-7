# 1. Deti do 10 let vcetne jezdi zadarmo
# 2. Mladez do 18 vcetne let jezdi za polovinu
# 3. Seniori od 65 let vcetne jezdi za tretinu
# 4. Ostatni jezdi za plnou cenu
# 5. Zaporny vek musi skoncit vyjimkou ValueError

#Toto je dulezite pro testovani toho, zda funkce skonci vyjimkou: with pytest.raises(ValueError):
import pytest

def spocitej_slevu_jizdneho(zakladni_cena, vek):

    if zakladni_cena < 0:
        raise ValueError

    if vek < 0:
        raise ValueError
    elif vek <=10:
        return 0
    elif vek <=18:
        return zakladni_cena / 2
    elif vek < 65:
        return zakladni_cena
    elif vek < 80:
        return zakladni_cena / 3
    else:
        return 0

def test_dospely_za_plnou_cenu():
    assert spocitej_slevu_jizdneho(30.0, 35) == 30.0

def test_mladez_za_polovinu():
    assert spocitej_slevu_jizdneho(30.0, 16) == 15.0

def test_senior_za_tretinu():
    assert spocitej_slevu_jizdneho(30.0, 70) == 10.0

def test_deti_zadarmo():
    assert spocitej_slevu_jizdneho(30.0, 5) == 0.0

def test_mladez_za_polovinu_hranicni_vek():
    assert spocitej_slevu_jizdneho(30.0, 18) == 15.0

def test_zaporny_vek_konci_vyjimkou():
    with pytest.raises(ValueError):
        spocitej_slevu_jizdneho(30.0, -666)

def test_zaporna_cena_konci_vyjimkou():
    with pytest.raises(ValueError):
        spocitej_slevu_jizdneho(-30.0, 12)

def test_seniori_zdarma():
    assert spocitej_slevu_jizdneho(30.0, 100) == 0

