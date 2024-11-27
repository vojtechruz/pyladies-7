import sqlite3
con = sqlite3.connect("example.db")

# - vytvor tabulku, ktera bude mit alespon 3 sloupce
# - jeden ze sloupcu je is_deleted
# - vloz alespon 2 radky, hodnota is_deleted je 0
# - nastav u jednoho z radku hodnotu is_deleted na 1
# - smaz vsechny hodnoty z tabulky jtere maji is_deleted 1
# - vypis vsechny radky z tabulky do konzole
# - smaz tabulku