try:
    #Zkusme deleni nulou
    print(1/0)
    #Zkusme prevest retezec na cele cislo
    int("haf!")
except ZeroDivisionError:
    print('Tohle se provede, kdyz delim nulou!')
except ArithmeticError:
    print('Tohle se neprovede, protoze uz jsem odchytil deleni nulou!')
except Exception:
    print('Tohle se provede, pokud nastane jiná chyba')
    # (kromě SystemExit a KeyboardInterrupt, ty chytat nechceme)
else:
    print('Tohle se provede, pokud chyba nenastane')
finally:
    print('Tohle se provede vždycky; i pokud v `try` bloku byl např. `return`')
