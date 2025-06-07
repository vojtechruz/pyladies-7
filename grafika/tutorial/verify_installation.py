"""
Jednoduchý skript pro ověření správné instalace knihovny Pyglet.
Spusťte tento skript pomocí příkazu:
    python verify_installation.py
"""

try:
    import pyglet
    print(f"Pyglet je úspěšně nainstalován! Verze: {pyglet.version}")
    
    # Vytvoření jednoduchého okna pro ověření funkčnosti
    window = pyglet.window.Window(width=400, height=200, caption="Ověření instalace Pyglet")
    
    label = pyglet.text.Label('Pyglet funguje správně!',
                              font_name='Arial',
                              font_size=18,
                              x=window.width//2, y=window.height//2,
                              anchor_x='center', anchor_y='center')
    
    @window.event
    def on_draw():
        window.clear()
        label.draw()
    
    # Funkce pro zavření okna po 3 sekundách
    def close_window(dt):
        window.close()
    
    # Naplánování zavření okna
    pyglet.clock.schedule_once(close_window, 3)
    
    print("Otevírám testovací okno na 3 sekundy...")
    pyglet.app.run()
    
    print("Test proběhl úspěšně! Vše je připraveno pro práci s Pygletem.")
    
except ImportError:
    print("Chyba: Pyglet není nainstalován!")
    print("Nainstalujte Pyglet pomocí příkazu:")
    print("    pip install -r requirements.txt")
    print("nebo")
    print("    pip install pyglet")
except Exception as e:
    print(f"Chyba při testování Pygletu: {e}")
    print("Zkontrolujte, zda je Pyglet správně nainstalován.")