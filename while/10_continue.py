# Continue neukonci cely cyklus jako break, ale jen preskoci aktualni opakovani a pokracuje dal
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    # Tady muze byt spousta dalsich radku