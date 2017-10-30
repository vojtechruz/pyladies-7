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

