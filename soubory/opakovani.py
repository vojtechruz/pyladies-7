# While -----------------------------------------------------------------
odpoved = input('Řekni Ááá! ')
while odpoved != 'Ááá':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni Ááá! ')

# For --------------------------------------------------------------------
soucet = 0

for cislo in 8, 45, 9, 21:
    soucet = soucet + cislo

print(soucet)

# For in range -----------------------------------------------------------
from turtle import forward, penup, pendown, exitonclick

for i in range(10):
    forward(10)
    penup()
    forward(5)
    pendown()

exitonclick()

# Tri zpusoby zapisu retezce ---------------------------------------------
'tohle je řetězec'
"tohle taky"
'''Haló haló!
Co se stalo?
Prase kozu potrkalo!'''

# Zakladni operace s retezci ---------------------------------------------
spojeny_retezec = 'a' + 'b'
dlouhy_retezec = 'ó' * 100
pate_pismeno = 'čokoláda'[4]
#  [0] [1] [2] [3] [4] [5] [6] [7]
# [-8][-7][-6][-5][-4][-3][-2][-1]
#   Č   o   k   o   l   á   d   a


len(retezec)
x in retezec
x not in retezec

upper()
lower()

# Formatovani retezce --------------------------------------------------
vypis = '{}×{} je {}'.format(3, 4, 3 * 4)

# Sekani retezce -------------------------------------------------------
retezec = 'čokoláda'
print(retezec[:4])
print(retezec[2:5])
print(retezec[-4:])

# Funkce --------------------------------------------------------------

# Funkce bez navratove hodnoty vraci None

# Lokalni promenne uvnitr funkci
  # Nelze priradit no lokalni promenne stejneho jmena jako je existujici globalni -> Vytvori se nova lokalni