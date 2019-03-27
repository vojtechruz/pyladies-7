# break prikaz ukonci predcasne cyklus
# pokud je vice vnorenych cyklu ukonci se ten vnitrni
# break se da pouzit pro for i while

for i in range(10):  # Vnější cyklus
    for j in range(10):  # Vnitřní cyklus
        print(j * i, end=' ')
        if i <= j:
            # Tento break ukonci jen vnitrni cyklus
            break
    print()