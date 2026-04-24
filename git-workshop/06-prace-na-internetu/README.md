# 6. Práce na internetu

Teď propojíme lokální Git s GitHubem. Naučíme se vytvořit vzdálený repozitář, naklonovat ho, odesílat a stahovat změny.

---

## Vytvoření repozitáře na GitHubu

1. Přihlas se na [github.com](https://github.com)
2. Klikni na **+** v pravém horním rohu → **New repository**
3. Vyplň:
   - **Repository name** – např. `moje-basnicky`
   - **Description** – stručný popis (volitelné)
   - **Public / Private** – veřejný nebo soukromý repozitář
4. Zaškrtni **Add a README file** (vytvoří se základní README soubor)
5. V rozbalovacím menu **.gitignore** vyber šablonu pro svůj projekt (např. `Python`)
6. Klikni **Create repository**

### README a Markdown

Soubor `README.md` je první věc, kterou lidé uvidí, když otevřou tvůj repozitář. Přípona `.md` znamená **Markdown** – jednoduchý formátovací jazyk.

Základní Markdown:

```markdown
# Nadpis první úrovně
## Nadpis druhé úrovně

Normální odstavec textu.

**tučně** a *kurzíva*

- odrážka 1
- odrážka 2

[text odkazu](https://example.com)
```

GitHub automaticky zobrazuje `README.md` jako naformátovanou stránku.

---

## Klonování repozitáře

**Klonování** zkopíruje celý vzdálený repozitář (včetně celé historie) na tvůj počítač.

Na stránce repozitáře na GitHubu klikni na zelené tlačítko **Code** a zkopíruj URL (HTTPS adresu).

```bash
git clone https://github.com/tvojejmeno/moje-basnicky.git
```

Tím vznikne nová složka `moje-basnicky` s obsahem repozitáře. Přejdi do ní:

```bash
cd moje-basnicky
```

Git automaticky nastavil propojení se vzdáleným repozitářem pod názvem `origin`.

---

## Přidání souboru a push

Vytvoř nový soubor, commitni ho a odešli na GitHub:

```bash
# Vytvoř soubor
echo "Prší, prší, jen se leje" > dalsi-basnicka.txt

# Přidej a commitni
git add dalsi-basnicka.txt
git commit -m "Pridana dalsi basnicka"

# Odešli na GitHub
git push
```

Po úspěšném push přejdi na GitHub a v repozitáři uvidíš nový soubor.

### Co je push?

`git push` odešle tvé lokální commity na vzdálený server (origin). Ostatní si je pak mohou stáhnout.

Pokud pushujete poprvé nebo na novou větev:

```bash
git push -u origin master
```

Přepínač `-u` nastaví výchozí větev pro budoucí push – příště stačí jen `git push`.

---

## Lokální změny vs. změny na serveru

Důležité je pochopit, že:

- **Lokální repozitář** (na tvém počítači) a **vzdálený repozitář** (GitHub) jsou **dvě samostatné kopie**
- Změny se mezi nimi synchronizují explicitně pomocí `git push` a `git pull`
- Dokud nezpushuješ, ostatní tvé změny nevidí
- Dokud nepullneš, nevidíš změny ostatních

---

## Stažení změn ze serveru – git pull

### Ruční úprava souboru na GitHubu

Na GitHubu otevři soubor `README.md` a klikni na ikonu tužky (Edit). Přidej pár řádků a klikni **Commit changes**.

Teď máš na GitHubu změnu, která **není** v tvém lokálním repozitáři.

Zkontroluj lokálně:

```bash
cat README.md
```

Lokální soubor je stará verze – GitHub změnu nevidí.

### git pull

Stáhni změny ze serveru:

```bash
git pull
```

```
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 3 +++
 1 file changed, 3 insertions(+)
```

Teď zkontroluj soubor znovu – obsahuje změnu z GitHubu:

```bash
cat README.md
```

### Změny v historii

Ruční úprava na GitHubu se zobrazí v historii jako commit:

```bash
git log --oneline
```

```
e4f5g6h (HEAD -> master, origin/master) Update README.md
a1b2c3d Pridana dalsi basnicka
```

---

## Doporučený pracovní postup

Při práci se vzdáleným repozitářem vždy:

1. Začni `git pull` – stáhni nejnovější změny
2. Pracuj a commituj lokálně
3. `git push` – odešli změny na server

Tím minimalizuješ konflikty s ostatními.

---

## Shrnutí příkazů

| Příkaz | Popis |
|--------|-------|
| `git clone <url>` | Naklonuje vzdálený repozitář |
| `git push` | Odešle lokální commity na server |
| `git push -u origin master` | Odešle a nastaví výchozí větev |
| `git pull` | Stáhne a aplikuje změny ze serveru |

---

[← GitHub](../05-github/README.md) | [Větvení →](../07-vetveni/README.md)
