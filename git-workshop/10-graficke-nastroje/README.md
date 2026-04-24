# 10. Grafická rozhraní pro Git

Příkazová řádka je základ – ale existují i grafické nástroje, které práci s Gitem zpříjemní. Hodí se zejména pro přehledné zobrazení větví, diff a řešení konfliktů.

---

## Git integrace v IntelliJ IDEA

IntelliJ IDEA (a celá rodina JetBrains IDE – PyCharm, WebStorm, GoLand atd.) má výbornou vestavěnou podporu pro Git.

### Otevření Git panelu

- V dolní liště klikni na záložku **Git** (nebo **Version Control**)
- Nebo přes menu: **View → Tool Windows → Git**

### Co nabízí

**Log (Historie)**
- Záložka **Log** zobrazuje celou historii commitů graficky
- Uvidíš větve jako barevné pruhy
- Kliknutím na commit zobrazíš detail změn (diff)
- Filtrace podle větve, autora, data, textu zprávy

**Lokální změny**
- Záložka **Local Changes** zobrazuje modifikované soubory
- Dvojklik na soubor otevře diff editor
- Přímo odsud můžeš stage/unstage soubory

**Commit**
- **Commit** dialog: zaškrtáváš soubory, píšeš zprávu, hned commitneš
- Klávesová zkratka: `Ctrl+K`

**Push / Pull**
- `Ctrl+Shift+K` – Push
- `Ctrl+T` – Update (pull)

### Řešení konfliktů v IntelliJ

IntelliJ má výborný 3-panelový merge editor:
- Levý panel: tvoje verze
- Pravý panel: jejich verze
- Střední panel: výsledek (editovatelný)

Klikáš na šipky u každého konfliktu a vybíráš, která verze vyhraje, nebo ručně edituješ výsledek.

---

## GitKraken

[GitKraken](https://www.gitkraken.com) je samostatný grafický Git klient – funguje nezávisle na IDE.

### Instalace

Stáhni z [gitkraken.com](https://www.gitkraken.com) (zdarma pro veřejné repozitáře).

### Hlavní funkce

**Grafické zobrazení větví**
- Centrální pohled zobrazuje historii jako vizuální strom
- Větve jsou barevně odlišené
- Přehledné zobrazení merge commitů

**Drag & drop operace**
- Větve lze mergovat přetažením
- Cherry-pick commitů přetažením

**Vestavěný editor konfliktů**
- Podobný třípanelovému pohledu jako IntelliJ

**Integrace s GitHubem / GitLabem**
- Přímo v aplikaci vidíš Pull Requesty
- Můžeš je komentovat, schvalovat a mergovat

### GitKraken vs. příkazová řádka

Grafické nástroje jsou pohodlné, ale znalost příkazové řádky je nenahraditelná:
- Na serverech GUI není k dispozici
- Při problémech je příkazová řádka přesnější a předvídatelnější
- Automatizace (skripty) vyžaduje příkazy

**Doporučení:** Nauč se nejprve příkazovou řádku, pak grafické nástroje používej pro každodenní pohodlnost.

---

## Další grafické nástroje

| Nástroj | Platforma | Poznámka |
|---------|-----------|----------|
| **GitHub Desktop** | Win, Mac | Jednoduchý klient přímo od GitHubu |
| **Sourcetree** | Win, Mac | Od Atlassianu, zdarma |
| **VS Code** | Win, Mac, Linux | Vestavěná Git integrace v editoru |
| **gitk** | Všechny | Vestavěný v Gitu, základní |
| **tig** | Mac, Linux | Terminálové TUI rozhraní |

---

[← Cvičení: Receptář](../09-spoluprace-receptar/README.md) | [Užitečné příkazy →](../11-uzitecne-prikazy/README.md)
