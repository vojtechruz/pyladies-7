import pyglet

def tik(uplynuly_cas):
    print("Tik-Tak...")
    print(str(uplynuly_cas) + " sekund od posledního volání")

# Funkce 'tik' bude volána každou 1/2 sekundu
# Poznámka: je to jen 'tik', ne 'tik()'
pyglet.clock.schedule_interval(tik, 1/2)

pyglet.app.run()