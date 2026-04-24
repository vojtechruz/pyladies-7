# 3. Grafické zobrazení historie

Příkaz `git log` zobrazuje historii textově. Pro přehlednější vizualizaci – zejména při práci s větvemi – se hodí grafické nástroje.

---

## gitk – vestavěný prohlížeč

Git obsahuje vestavěný grafický prohlížeč `gitk`. Spustíš ho z terminálu ve složce repozitáře:

```bash
gitk --all
```

Přepínač `--all` zajistí, že se zobrazí všechny větve, nejen aktuální.

### Co v gitk uvidíš

- **Horní část:** Graf commitů s větvemi a tagy – každá tečka je jeden commit
- **Levý sloupec pod grafem:** Detail vybraného commitu – zpráva, autor, datum
- **Pravý sloupec:** Diff – co se v daném commitu změnilo

### Kdy je gitk užitečný

- Když chceš přehledně vidět strukturu větví
- Při slučování (merge) – uvidíš, kde se větve rozdělily a kde se sloučily
- Pro pochopení vztahů mezi commity

---

## git log s grafem v terminálu

Pokud nechceš otevírat grafické okno, můžeš získat ASCII graf přímo v terminálu:

```bash
git log --all --oneline --graph --decorate
```

Výstup bude vypadat přibližně takto (po vytvoření větví v pozdějších sekcích):

```
* a1b2c3d (HEAD -> master) Pridana treti sloha
* 9f8e7d6 Pridana druha sloha
* 3c2b1a0 Pridana basnicka
```

Nebo s větvemi:

```
*   d4e5f6g (HEAD -> master) Merge branch 'nazev-basnicky'
|\
| * b7c8d9e (nazev-basnicky) Pridany nazev basnicky
* | a1b2c3d Opraveny preklepey
|/
* 9f8e7d6 Pridana basnicka
```

---

## Shrnutí příkazů

| Příkaz | Popis |
|--------|-------|
| `gitk --all` | Otevře grafický prohlížeč všech větví |
| `git log --all --oneline --graph --decorate` | ASCII graf v terminálu |

---

[← Lokální práce](../02-lokalni-prace/README.md) | [Ignorování souborů →](../04-ignorovani-souboru/README.md)
