# Kombinace podminek
# and - Oboje podminky plati
# or - Alespon jedna podminka plati
# not - Negace podminky

den = input("Jaky je den v tydnu?")

if den != "sobota" and den != "nedele":
    print("Uz aby byl vikend!")