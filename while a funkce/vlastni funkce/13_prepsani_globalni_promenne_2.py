jmeno = "Jana"

def predstav_se():
    global jmeno # Nyni rikame, ze chceme odkazovat na globalni promennou jmeno
    print(jmeno) # Jana - puvodni hodnota z vnejsku funkce
    jmeno = "Eva"
    print("Ahoj, ja jsem " + jmeno)

predstav_se() # Ahoj, ja jsem Eva
print(jmeno) # Eva