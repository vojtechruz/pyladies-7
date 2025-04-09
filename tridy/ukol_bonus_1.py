# Vytvor tridu auto
# - auto musi dostat pri tvorbe znacku a model
# - volitelne se pri tvorbe da zadat ureven paliva v procentech. Muzi byt mezi 0-100. Pokud neni specifikovano bude 0
# - volitelne se pri tvorbe da specifikovat spotreba, pokud neni dana, bude 1. Nesmi byt mensi nebo rovna 0. Predpokladame jen cela cisla
# - metoda natankuj bere mnozstvi paliva a prida ho k soucansemu mnozstvi. Vysledek opet nemuze byt vetsi nez 100
# - auto ma metodu jed, ktera bere vzdalenost. Za kazdou ujetou jednotku vzdalenosti odecte palivo (vzdalenost*spotreba)
#       - auto vypise o kolik se pohnulo a kolik spotrebovalo benzinu
#       - pokud by pozadovana vzdalenost nebyla dosazitelna s aktualnim mnozstvim paliva, auto pojede kam bude moct dokud mu nedojde palivo
#       - vzdalenost musi byt vetsi nez 0, predpokladame jen cela cisla
# - auto pocita ujetou vzdalenost, pokud presahne 100, je rozbite
#     - stav vozidla jde zjistit metodou je_rozbite
# - pridej metodu je_pojizdne - pojizdne auto je pokud ma benzin a neni rozbite
# - pridej metodu servisuj, ktera opravi auto a doplni paliv
#
# Vytvor instanci auta a zeptej se uzivatele o kolik ma jet. Potom nech auto jen pozadovanou vzdalenost. Pokud je auto nepojizdne jako vysledek informuj uzivatele