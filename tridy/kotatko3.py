# Trida Kotatko zustava stejna jako v predeslem prikladu.
# Nyni uz vytvarime dve instance tridy Kotatko.
#       kotatko = Kotatko()
#       jineKotatko = Kotatko()
#
# Abychom je od sebe rozeznali, priradime kazdemu kotatku jmeno do atributu tridy "jmeno":
#       kotatko.jmeno = 'Micka'
#       jineKotatko.jmeno = 'Mourek'
#
# K atributu jmeno pak muzeme opet pristupovat a pouzit ho pri vypisu do konzole:
#       print('Jmeno prvniho kotatka je {}'.format(kotatko.jmeno))
#       print('Jmeno druheho kotatka je {}'.format(jineKotatko.jmeno))


class Kotatko:
    def zamnoukej(self, zprava):
        print('Kotatko: {}'.format(zprava))


kotatko = Kotatko()
kotatko.jmeno = 'Micka'
print('Jmeno prvniho kotatka je {}'.format(kotatko.jmeno))

jine_kotatko = Kotatko()
jine_kotatko.jmeno = 'Mourek'
print('Jmeno druheho kotatka je {}'.format(jine_kotatko.jmeno))
