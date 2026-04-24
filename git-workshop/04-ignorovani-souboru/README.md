# 4. Ignorování souborů – .gitignore

V každém projektu existují soubory, které do repozitáře nepatří: zkompilované soubory, dočasné soubory editoru, logy, konfigurace s hesly apod. Git umožňuje tyto soubory ignorovat pomocí souboru `.gitignore`.

---

## Proč ignorovat soubory?

- **Vygenerované soubory** (`.pyc`, `.class`, `dist/`) lze vždy znovu vygenerovat
- **Dočasné soubory** editoru (`.idea/`, `.vscode/`, `*.swp`) patří každému vývojáři jinak
- **Soubory s citlivými daty** (hesla, API klíče, `.env`) nesmí být veřejné
- **Velké binární soubory** zbytečně nafukují repozitář

---

## Vytvoření .gitignore

Soubor `.gitignore` se vytváří v kořenové složce repozitáře. Na Linuxu a macOS je soubor začínající tečkou automaticky skrytý. Na Windows ho uvidíš v Průzkumníku jen se zapnutým zobrazením skrytých souborů.

### Ukázka situace před .gitignore

Představ si, že máš v projektu soubor `debug.log`, který si nechceš commitovat:

```bash
git status
```

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        debug.log
        basnicka.txt
```

`debug.log` se stále ukazuje jako untracked – obtěžuje nás.

### Vytvoření souboru .gitignore

Vytvoř soubor `.gitignore` a do něj napiš vzor souborů, které chceš ignorovat:

```
debug.log
```

Ulož soubor a podívej se na stav:

```bash
git status
```

```
Untracked files:
        .gitignore
        basnicka.txt
```

`debug.log` už ve výstupu není! Git ho ignoruje.

---

## Vzory v .gitignore

V `.gitignore` lze používat vzory (patterns):

### Konkrétní soubor

```
hesla.txt
config.local.json
```

### Všechny soubory s danou příponou

```
*.log
*.pyc
*.class
```

### Otazník – jeden libovolný znak

```
debug?.log
```

Bude ignorovat `debug1.log`, `debugA.log`, ale ne `debug.log` ani `debug10.log`.

### Složka – lomítko na konci

```
build/
dist/
__pycache__/
.idea/
```

Lomítko na konci říká, že jde o složku. Git bude ignorovat celý její obsah.

### Komentáře

Řádky začínající `#` jsou komentáře:

```
# Ignoruj logy
*.log

# Ignoruj skompilované Pythonovy soubory
*.pyc
__pycache__/
```

---

## .gitignore je verzovaný soubor!

Soubor `.gitignore` **patří do repozitáře** – je to běžný soubor, který se commituje. Díky tomu ho sdílíš se všemi, kdo na projektu pracují. Každý tak automaticky ignoruje stejné soubory.

Nezapomeň ho přidat:

```bash
git add .gitignore
git commit -m "Pridano .gitignore"
```

---

## git add . – přidání všech souborů

Pokud chceš přidat všechny sledované (non-ignored) soubory najednou, použij tečku:

```bash
git add .
```

Přidá všechny změněné soubory, které nejsou v `.gitignore`. Je to zkratka – v praxi ji používáš, když chceš commitnout vše.

---

## Pozor: already committed soubory

**Důležité:** Pokud jsi soubor **commitl/a dříve, než jsi ho přidal/a do .gitignore**, Git ho bude dál sledovat. `.gitignore` funguje jen pro dosud nesledované soubory.

Jak přestat sledovat již commitnutý soubor:

```bash
git rm --cached nazev-souboru.txt
git commit -m "Odstranek sledovani souboru"
```

`git rm --cached` odstraní soubor z Gitu (přestane ho sledovat), ale fyzicky ho na disku nechá.

---

## Šablony .gitignore

Nemusíš psát `.gitignore` od nuly. GitHub nabízí kolekci šablon pro různé technologie:

- [github.com/github/gitignore](https://github.com/github/gitignore)

Například pro Python, Java, Node.js, VS Code, IntelliJ atd.

---

## Shrnutí

| Vzor | Co ignoruje |
|------|-------------|
| `soubor.txt` | Konkrétní soubor |
| `*.log` | Všechny soubory s příponou `.log` |
| `debug?.log` | `debug1.log`, `debugA.log`, … |
| `build/` | Složka `build` a vše v ní |
| `#komentář` | Komentář (ignorován Gitem) |

| Příkaz | Popis |
|--------|-------|
| `git add .` | Přidá všechny neignorované změny |
| `git rm --cached soubor.txt` | Přestane sledovat soubor (fyzicky ho ponechá) |

---

[← Grafické zobrazení](../03-graficke-zobrazeni/README.md) | [GitHub →](../05-github/README.md)
