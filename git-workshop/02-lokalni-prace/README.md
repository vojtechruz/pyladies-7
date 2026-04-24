# 2. Lokální práce s Gitem

V této sekci se naučíš základní pracovní cyklus Gitu: vytvořit repozitář, přidat soubory, commitovat změny a prohlížet historii.

---

## Vytvoření repozitáře

Nejprve si vytvoř novou složku pro projekt a přejdi do ní:

```bash
mkdir muj-projekt
cd muj-projekt
```

Teď inicializuj Git repozitář:

```bash
git init
```

Výstup:
```
Initialized empty Git repository in /cesta/k/muj-projekt/.git/
```

### Co je repozitář?

**Repozitář** (repository, zkráceně repo) je složka projektu, ve které Git sleduje změny. Obsahuje celou historii projektu.

### Složka `.git`

Po spuštění `git init` vznikla ve složce projektu skrytá podsložka `.git`. Tuto složku Git používá k ukládání veškeré historie a konfigurace.

```bash
ls -la
```

Uvidíš složku `.git`. Nikdy do ní nic ručně nezasahuj – Git si ji spravuje sám.

> Na Windows jsou skryté soubory (začínající tečkou) standardně schované. Zobrazíš je přes Průzkumník souborů → Zobrazit → Skryté položky.

---

## git status – kontrola stavu

Příkaz `git status` ti kdykoli řekne, co se děje v repozitáři:

```bash
git status
```

Ve čistém, právě vytvořeném repozitáři uvidíš:

```
On branch master

No commits yet

nothing to commit (create/copy files and start working)
```

`git status` budeš používat velmi často – je to tvůj nejlepší přítel.

---

## První soubor – básnička

Vytvoř textový soubor `basnicka.txt` s libovolnou básničkou. Například:

```
Holka modrooká
nestůj u potoka
```

Uložíme ji a podíváme se na stav:

```bash
git status
```

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        basnicka.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Soubor je **červený** – Git ho vidí, ale nesleduje ho. Je "untracked".

---

## Staging area – přípravná oblast

Než soubory commitneš, musíš je přidat do tzv. **staging area** (přípravné oblasti, indexu). Je to místo, kde řekneš Gitu: "Tyto změny chci zahrnout do dalšího commitu."

Přidej soubor:

```bash
git add basnicka.txt
```

Zkontroluj stav:

```bash
git status
```

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   basnicka.txt
```

Soubor je teď **zelený** – je ve staging area a připravený na commit.

### Jak to funguje – tři oblasti

```
Working Directory  →  git add  →  Staging Area  →  git commit  →  Repository
   (pracovní)                     (přípravná)                      (historie)
```

---

## git commit – uložení změn

Commit je trvalé uložení stavu staging area do historie. Každý commit by měl mít popisnou zprávu.

### Commit s parametrem -m (doporučeno)

```bash
git commit -m "Pridana basnicka"
```

Výstup:
```
[master (root-commit) a1b2c3d] Pridana basnicka
 1 file changed, 2 insertions(+)
 create mode 100644 basnicka.txt
```

Zkontroluj stav – měl by být čistý:

```bash
git status
```

```
On branch master
nothing to commit, working tree clean
```

---

## Celý cyklus znovu

Zkus celý cyklus ještě jednou. Přidej do básničky další sloku a ulož soubor.

```bash
git status        # soubor je červený - modifikovaný
git add basnicka.txt
git status        # soubor je zelený - ve staging
git commit -m "Pridana druha sloka"
git status        # čistý stav
```

---

## git log – prohlížení historie

```bash
git log
```

```
commit a1b2c3d4e5f6789... (HEAD -> master)
Author: Jan Novák <jan@example.com>
Date:   Thu Apr 24 10:00:00 2026 +0200

    Pridana druha sloha

commit 9f8e7d6c5b4a3...
Author: Jan Novák <jan@example.com>
Date:   Thu Apr 24 09:55:00 2026 +0200

    Pridana basnicka
```

**Ukončení `git log`:** Pokud je historie dlouhá, otevře se prohlížeč (pager). Pro ukončení stiskni `q`.

### Identifikátory commitů

Každý commit má jedinečný identifikátor – **hash** (dlouhý hexadecimální řetězec jako `a1b2c3d4e5f6...`). Slouží k jednoznačné identifikaci commitu. Při odkazování stačí prvních 7 znaků.

Přehlednější výpis:

```bash
git log --oneline
```

```
a1b2c3d Pridana druha sloha
9f8e7d6 Pridana basnicka
```

---

## git diff – zobrazení rozdílů

Před přidáním změn do staging area je dobré zkontrolovat, co vlastně měníš.

Uprav básničku a ulož. Pak:

### Rozdíl mezi pracovním adresářem a staging area

```bash
git diff
```

Zobrazí změny, které **ještě nejsou** ve staging area (co je nového v souboru oproti tomu, co je připraveno k commitu).

### Rozdíl mezi HEAD a staging area

```bash
git diff --staged
```

Zobrazí změny, které **jsou** ve staging area a budou součástí dalšího commitu.

### Rozdíl mezi HEAD a pracovním adresářem

```bash
git diff HEAD
```

Zobrazí **všechny** změny od posledního commitu (jak staged, tak unstaged).

### Jak číst výstup diffu

```diff
-Holka modrooká
+Holka modrooká,
 nestůj u potoka
+nestůj u rybníka.
```

- Řádky začínající `-` byly **odebrány**
- Řádky začínající `+` byly **přidány**
- Ostatní řádky jsou kontext

---

## Odebrání souboru ze staging area

Pokud jsi soubor přidal/a do staging area omylem, vyjmeš ho příkazem:

```bash
git rm --cached basnicka.txt
```

Soubor zůstane v pracovním adresáři (neodstraní ho), ale bude odebrán ze staging area. Je to opak `git add`.

---

## Shrnutí pracovního cyklu

```
1. Uprav soubor
2. git status    → zkontroluj co se změnilo
3. git diff      → prohlédni si změny
4. git add       → přidej do staging area
5. git commit -m → ulož do historie
```

## Shrnutí příkazů

| Příkaz | Popis |
|--------|-------|
| `git init` | Vytvoří nový repozitář |
| `git status` | Zobrazí aktuální stav repozitáře |
| `git add soubor.txt` | Přidá soubor do staging area |
| `git add .` | Přidá všechny změněné soubory do staging area |
| `git commit -m "zpráva"` | Vytvoří commit se zprávou |
| `git log` | Zobrazí historii commitů |
| `git log --oneline` | Zobrazí zkrácenou historii |
| `git diff` | Rozdíl: pracovní adresář vs. staging |
| `git diff --staged` | Rozdíl: staging vs. HEAD |
| `git diff HEAD` | Rozdíl: HEAD vs. pracovní adresář |
| `git rm --cached soubor.txt` | Odebere soubor ze staging area |

---

[← Úvod](../01-uvod/README.md) | [Grafické zobrazení →](../03-graficke-zobrazeni/README.md)
