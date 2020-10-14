jmeno = "Jana"

def predstav_se():
    # Nova lokalni promenna 'jmeno' s hodnotou 'Eva'
    # Zastini globalni promennou
    # Ale globalni stale existuje
    jmeno = "Eva"
    print("Ahoj, ja jsem " + jmeno)

predstav_se() # Ahoj, ja jsem Eva (vypisuje lokalni promennnou uvnitr funkce)
print(jmeno) # Jana (globalni promenna zezacatku souboru)