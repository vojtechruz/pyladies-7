# Z řetězce "Čokoláda" získej pomoci pristupu k
# jednotlivym znakum nebo podretezcum nasledujici retezce:

# Č
# á
# kolá
# láda
# a
# Čoko






#
#
# ╭───┬───┬───┬───┬───┬───┬───┬───╮
# │ Č │ o │ k │ o │ l │ á │ d │ a │
# ├───┼───┼───┼───┼───┼───┼───┼───┤
# │   │   │   │   │   │   │   │   │
# 0   1   2   3   4   5   6   7   8
# -8  -7  -6  -5  -4  -3  -2  -1
#
# ╰───────────────╯
# 'čokoláda'[:4] == 'čoko'
#
# ╰───────────────╯
# 'čokoláda'[2:6] == 'kolá'
#
# ╰───────────╯
# 'čokoláda'[-3:] == 'áda'