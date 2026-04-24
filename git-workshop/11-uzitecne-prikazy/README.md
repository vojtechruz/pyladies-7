# 11. Užitečné příkazy – Reset a Revert

Tato sekce pokrývá situace, kdy potřebuješ vrátit změny – ze staging area, z posledního commitu nebo na konkrétní starší commit.

> **Pozor:** Příkazy s `--hard` jsou nevratné. Přijdeš o neuložené změny. Vždy zkontroluj, co děláš.

---

## Odebrání souboru ze staging area (unstage)

Přidal/a jsi soubor do staging area (`git add`), ale rozmyslel/a ses:

```bash
git restore --staged soubor.txt
```

Starší varianta (stále funguje):

```bash
git reset HEAD soubor.txt
```

Soubor zůstane v pracovním adresáři se změnami – jen opustí staging area.

### Odebrání všech souborů ze staging

```bash
git restore --staged .
```

---

## Zahození změn v pracovním adresáři

Soubor jsi upravil/a, ale chceš se vrátit k verzi z posledního commitu:

```bash
git restore soubor.txt
```

Starší varianta:

```bash
git checkout -- soubor.txt
```

> **Nevratné!** Změny v souboru budou ztraceny.

---

## Vrácení posledního commitu

### Vrácení commitu se zachováním změn (soft)

Commit se zruší, ale změny zůstanou ve staging area:

```bash
git reset --soft HEAD~1
```

Hodí se, když jsi commitl/a předčasně a chceš upravit zprávu nebo přidat další soubory.

### Vrácení commitu se zachováním změn v pracovním adresáři

Commit se zruší, změny zůstanou v souborech (ale ne ve staging):

```bash
git reset HEAD~1
```

(Výchozí chování – stejné jako `--mixed`)

### Vrácení commitu a zahození změn (hard)

Commit se zruší a **změny se ztratí**:

```bash
git reset --hard HEAD~1
```

> **Nevratné!** Změny z commitu i z pracovního adresáře budou smazány.

---

## Vrácení na konkrétní commit

Pokud chceš vrátit celý repozitář na konkrétní starší commit:

```bash
git reset --hard 0ad5a7a6
```

Kde `0ad5a7a6` je hash commitu (nebo alespoň prvních 7 znaků), který zjistíš z `git log`.

> **Pozor:** Tímto přijdeš o všechny commity, které byly po daném commitu. Použij opatrně – a nikdy na pushnuté commity, které mají ostatní.

---

## Prohlížení starého commitu bez změny větve

Pokud chceš jen **prohlédnout** stav repozitáře v určitém commitu, ale nechceš ztratit aktuální práci:

```bash
git checkout 0ad5a7a6
```

Dostaneš se do tzv. **detached HEAD** stavu – jsi „odpojen/a" od větve. Můžeš soubory prohlížet, ale pokud vytvoříš commit, ztratí se, pokud si nevytvoříš novou větev.

Vrátíš se zpět příkazem:

```bash
git checkout master
```

---

## git revert – bezpečné vrácení commitu

Pokud jsi změny **pushnuté** a sdílené s ostatními, `git reset` není vhodný (přepíše historii). Místo toho použij `git revert`:

```bash
git revert 0ad5a7a6
```

`git revert` vytvoří **nový commit**, který vrátí změny daného commitu. Historie zůstane zachována – jen se přidá „opravný" commit. Bezpečné pro pushnuté změny.

---

## Přehled: kdy co použít

| Situace | Příkaz |
|---------|--------|
| Odebrat soubor ze staging | `git restore --staged soubor.txt` |
| Zahodit změny v souboru | `git restore soubor.txt` |
| Vrátit poslední commit (zachovat změny) | `git reset --soft HEAD~1` |
| Vrátit poslední commit (zahodit změny) | `git reset --hard HEAD~1` |
| Vrátit na konkrétní commit | `git reset --hard <hash>` |
| Prohlédnout starý commit | `git checkout <hash>` |
| Bezpečně vrátit pushnutý commit | `git revert <hash>` |

---

## Zkratka HEAD~

`HEAD` označuje aktuální pozici (poslední commit na aktuální větvi).

- `HEAD~1` nebo `HEAD~` – o jeden commit zpět
- `HEAD~2` – o dva commity zpět
- `HEAD~5` – o pět commitů zpět

---

## Shrnutí příkazů

| Příkaz | Popis |
|--------|-------|
| `git restore --staged soubor.txt` | Odebere soubor ze staging |
| `git restore soubor.txt` | Zahodí změny v souboru |
| `git reset --soft HEAD~1` | Zruší commit, zachová změny ve staging |
| `git reset HEAD~1` | Zruší commit, zachová změny v souborech |
| `git reset --hard HEAD~1` | Zruší commit a zahodí změny |
| `git reset --hard <hash>` | Vrátí na konkrétní commit |
| `git checkout <hash>` | Prohlédne stav v daném commitu |
| `git revert <hash>` | Bezpečně vrátí pushnutý commit |

---

[← Grafická rozhraní](../10-graficke-nastroje/README.md) | [← Zpět na přehled](../README.md)
