# 7. Větvení

Větvení je jedna z nejsilnějších funkcí Gitu. Umožňuje pracovat na více věcech najednou bez vzájemného ovlivňování.

---

## Proč větvit?

Představ si, že pracuješ na projektu a potřebuješ:
- Opravit kritickou chybu v produkci
- Zároveň vyvíjet novou funkci
- Experimentovat s něčím, co možná zahazu

Bez větví by se tyto změny míchaly dohromady. **Větve** ti umožňují každou věc vyvíjet izolovaně a teprve hotovou ji začlenit do hlavní větve.

---

## Princip větvení

Každý repozitář má alespoň jednu větev. Výchozí větev se tradičně jmenuje `master` (nebo nověji `main`).

```
master:  A --- B --- C
```

Když vytvoříš novou větev, vznikne z aktuálního commitu „odbočka":

```
master:       A --- B --- C
                           \
nova-funkce:                D --- E
```

Větve se vyvíjejí nezávisle. Když je nová funkce hotová, sloučíš ji zpět do master:

```
master:  A --- B --- C ----------- F (merge)
                      \           /
nova-funkce:           D --- E ---
```

---

## Práce s větvemi

### Zobrazení větví

```bash
git branch
```

```
* master
```

Hvězdička označuje aktuální větev.

### Vytvoření nové větve

Vytvoříme větev pro přidání názvu básničky:

```bash
git branch nazev-basnicky
```

Zobraz větve znovu:

```bash
git branch
```

```
* master
  nazev-basnicky
```

Větev `nazev-basnicky` existuje, ale stále jsi na `master` (hvězdička).

### Přepnutí na větev

```bash
git checkout nazev-basnicky
```

Novější syntax (Git 2.23+):

```bash
git switch nazev-basnicky
```

Zkontroluj:

```bash
git branch
```

```
  master
* nazev-basnicky
```

Teď jsi na větvi `nazev-basnicky`.

### Vytvoření a přepnutí zároveň (zkratka)

```bash
git checkout -b nazev-basnicky
# nebo novější:
git switch -c nazev-basnicky
```

---

## Práce na větvi

Přidej do básničky název na první řádek a ulož. Commit:

```bash
git add basnicka.txt
git commit -m "Pridan nazev basnicky"
```

Podívej se na historii:

```bash
git log --oneline
```

```
b7c8d9e (HEAD -> nazev-basnicky) Pridan nazev basnicky
a1b2c3d (master) Pridana druha sloha
9f8e7d6 Pridana basnicka
```

Větev `master` stojí na `a1b2c3d`, větev `nazev-basnicky` je o commit napřed.

Zobraz vizuálně v gitk:

```bash
gitk --all
```

---

## Merge – sloučení větví

Až je práce na větvi hotová, sloučíme ji zpět do `master`.

**Pravidlo:** `git merge` slučuje specifikovanou větev **do aktuální větve**.

1. Přepni se na `master`:

```bash
git checkout master
```

2. Slij větev `nazev-basnicky` do `master`:

```bash
git merge nazev-basnicky
```

```
Updating a1b2c3d..b7c8d9e
Fast-forward
 basnicka.txt | 1 +
 1 file changed, 1 insertion(+)
```

`Fast-forward` znamená, že master jednoduše „přeskočil" na konec větve – žádné komplikace.

---

## Konflikt při slučování

Konflikty nastávají, když dvě větve změnily **stejné místo ve stejném souboru** různě.

### Simulace konfliktu

Vytvoř novou větev pro doplnění autora:

```bash
git checkout -b doplneni-autora
```

Přidej jméno autora na první řádek básničky a commitni:

```bash
git add basnicka.txt
git commit -m "Pridan autor basnicky"
```

Přepni zpět na `master` a udělej jinou změnu na stejném místě:

```bash
git checkout master
```

Uprav první řádek básničky jinak (třeba přidej jiný text) a commitni.

Teď zkus merge:

```bash
git merge doplneni-autora
```

```
Auto-merging basnicka.txt
CONFLICT (content): Merge conflict in basnicka.txt
Automatic merge failed; fix conflicts and then commit the result.
```

### Jak vyřešit konflikt

Otevři soubor `basnicka.txt`. Git do něj vložil značky:

```
<<<<<<< HEAD
Holka modrooká (verze z master)
=======
Holka modrooká - autor: Karel Erben (verze z doplneni-autora)
>>>>>>> doplneni-autora
```

- Část mezi `<<<<<<< HEAD` a `=======` je verze z aktuální větve (master)
- Část mezi `=======` a `>>>>>>> doplneni-autora` je verze ze slučované větve

Ručně rozhodneš, jak má soubor vypadat. Smaž všechny značky (`<<<<<<<`, `=======`, `>>>>>>>`) a nechej výslednou verzi:

```
Holka modrooká - autor: Karel Erben
```

Uložíš soubor, přidáš do staging a commitneš:

```bash
git add basnicka.txt
git commit -m "Vyreseny konflikt pri mergi autora"
```

---

## Smazání větve

Po úspěšném sloučení lze větev smazat – commity zůstanou v historii, jen se smaže pojmenovaný ukazatel:

```bash
git branch -d doplneni-autora
```

Přepínač `-d` (delete) funguje jen pokud je větev sloučená. Pro vynucené smazání neslouičené větve použij `-D`.

---

## Shrnutí příkazů

| Příkaz | Popis |
|--------|-------|
| `git branch` | Zobrazí větve (hvězdička = aktuální) |
| `git branch nazev` | Vytvoří novou větev |
| `git checkout nazev` | Přepne na větev |
| `git switch nazev` | Přepne na větev (novější syntax) |
| `git checkout -b nazev` | Vytvoří větev a přepne na ni |
| `git switch -c nazev` | Vytvoří větev a přepne na ni (novější) |
| `git merge nazev` | Sloučí větev `nazev` do aktuální větve |
| `git branch -d nazev` | Smaže sloučenou větev |
| `git branch -D nazev` | Smaže větev vynuceně |

---

[← Práce na internetu](../06-prace-na-internetu/README.md) | [Spolupráce →](../08-spoluprace/README.md)
