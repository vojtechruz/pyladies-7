osoby = 'máma', 'teta', 'babička', 'vrah'
vlastnosti = 'hodná', 'milá', 'laskavá', 'zákeřný'

for osoba, vlastnost in zip(osoby, vlastnosti):
    print('{} je {}'.format(osoba, vlastnost))