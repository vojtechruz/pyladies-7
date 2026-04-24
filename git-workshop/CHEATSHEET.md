# Git Cheatsheet

Příkazy v pořadí, v jakém se je učíme na workshopu.

---

## Konfigurace (jednou na začátku)

```bash
git config --global user.name "Jméno Příjmení"
git config --global user.email "email@example.com"
git config --global core.editor notepad
git config --global core.autocrlf true   # pouze Windows
git config --global --list               # ověření nastavení
```

---

## Lokální práce

```bash
git init                        # vytvoří repozitář v aktuální složce

git status                      # co se děje? (používej často)

git add soubor.txt              # přidá soubor do staging area
git add .                       # přidá vše (kromě ignorovaných)
git rm --cached soubor.txt      # odebere soubor ze staging (opak add)

git commit -m "zpráva"          # uloží staging do historie

git log                         # historie commitů (ukončení: q)
git log --oneline               # zkrácená historie
git log --oneline --graph --all # graf větví v terminálu

git diff                        # změny: pracovní adresář vs. staging
git diff --staged               # změny: staging vs. poslední commit
git diff HEAD                   # změny: pracovní adresář vs. poslední commit
```

---

## Ignorování souborů

```bash
# Vytvoř soubor .gitignore a napiš do něj vzory, například:
# *.log
# build/
# hesla.txt

git add .gitignore
git commit -m "Pridano .gitignore"
```

---

## Práce na internetu

```bash
git clone https://github.com/uzivatel/repozitar.git   # stáhne repozitář

git push                        # odešle commity na server
git push -u origin master       # první push – nastaví výchozí větev

git pull                        # stáhne a aplikuje změny ze serveru
```

---

## Větvení

```bash
git branch                      # zobrazí větve (* = aktuální)
git branch nazev-vetve          # vytvoří novou větev

git checkout nazev-vetve        # přepne na větev
git switch nazev-vetve          # přepne na větev (novější syntax)

git checkout -b nazev-vetve     # vytvoří větev a přepne na ni
git switch -c nazev-vetve       # totéž, novější syntax

git merge nazev-vetve           # sloučí větev do aktuální
git branch -d nazev-vetve       # smaže sloučenou větev

gitk --all                      # grafické zobrazení větví
```

---

## Spolupráce

```bash
git remote -v                                  # zobrazí nastavené remote
git remote add upstream https://github.com/…   # přidá původní repozitář

git pull upstream master        # stáhne změny z původního repozitáře
git push origin master          # odešle změny do svého forku
```

---

## Vrácení změn

```bash
git restore --staged soubor.txt # odebere soubor ze staging
git restore soubor.txt          # zahodí změny v souboru (nevratné!)

git reset --soft HEAD~1         # zruší poslední commit, zachová staging
git reset HEAD~1                # zruší poslední commit, zachová soubory
git reset --hard HEAD~1         # zruší poslední commit + zahodí změny (nevratné!)
git reset --hard <hash>         # vrátí na konkrétní commit (nevratné!)

git revert <hash>               # bezpečné vrácení pushnutého commitu (přidá nový commit)

git checkout <hash>             # prohlédne stav v daném commitu (detached HEAD)
git checkout master             # vrátí se zpět na větev
```

---

## Nejčastější pracovní cyklus

```bash
git pull                        # 1. stáhni nejnovější změny
# ... pracuj na souborech ...
git status                      # 2. zkontroluj co se změnilo
git diff                        # 3. prohlédni změny
git add .                       # 4. připrav ke commitu
git commit -m "popis změny"     # 5. ulož do historie
git push                        # 6. odešli na server
```
