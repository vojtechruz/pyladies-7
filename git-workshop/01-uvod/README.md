# 1. Úvod do Gitu

## Co je verzování?

Při práci na projektu – ať už jde o program, dokument nebo cokoliv jiného – přijde chvíle, kdy potřebuješ:

- Vrátit se ke starší verzi souboru
- Zjistit, kdo a kdy udělal určitou změnu
- Pracovat na více věcech najednou bez vzájemného rušení
- Spolupracovat s dalšími lidmi na stejném projektu

**Verzovací systém** (version control system, VCS) tyto problémy řeší. Ukládá historii změn, umožňuje se k nim vracet a podporuje spolupráci.

### Bez verzování

Bez verzovacího systému se situace typicky vyřeší takto:

```
projekt_v1.zip
projekt_v2.zip
projekt_final.zip
projekt_final2.zip
projekt_final_opravdu_final.zip
projekt_final_opravdu_final_TOTO.zip
```

Je to nepřehledné, náchylné k chybám a pro spolupráci nevhodné.

---

## Co je Git?

**Git** je distribuovaný verzovací systém. Je nejpoužívanější verzovací systém na světě. Vytvořil ho Linus Torvalds (autor Linuxu) v roce 2005 pro vývoj jádra Linuxu.

### Distribuovanost – práce bez internetu

Git je **distribuovaný** – každý vývojář má u sebe **kompletní kopii celé historie** projektu.

Co to znamená v praxi:
- Commituješ, prohlížíš historii, větváš a slučuješ – **vše bez internetu**
- Pokud server vypadne, máš všechno u sebe
- Většina operací je rychlá, protože probíhá lokálně

Na internet se připoješ jen tehdy, když chceš sdílet změny s ostatními (push/pull).

---

## Instalace a kontrola

### Kontrola, zda je Git nainstalovaný

Otevři terminál (na Windows **Git Bash**) a zadej:

```bash
git --version
```

Výstup by měl vypadat přibližně takto:

```
git version 2.44.0
```

Pokud příkaz Git nezná, je potřeba ho nainstalovat.

### Instalace na Windows

1. Jdi na [git-scm.com](https://git-scm.com) a stáhni instalátor
2. Spusť ho a projdi průvodcem – výchozí nastavení jsou většinou vhodná
3. Po instalaci máš k dispozici **Git Bash** i integraci do příkazové řádky

Pokud si nevíš rady, přivolej kouče.

---

## Git Bash vs příkazová řádka

Na Windows máš po instalaci Gitu dvě možnosti, jak Git spouštět:

| | Git Bash | Příkazová řádka (cmd) / PowerShell |
|---|---|---|
| Syntax příkazů | Unix/Linux styl | Windows styl |
| Doporučení | ✅ Doporučeno | Funguje také |

**Na tomto workshopu používáme Git Bash** (nebo terminál na macOS/Linux – tam je to identické).

Git Bash najdeš v nabídce Start nebo kliknutím pravým tlačítkem v průzkumníku souborů → *Git Bash Here*.

---

## Konfigurace Gitu

Před prvním použitím je potřeba nastavit jméno a email. Tyto údaje budou přiloženy ke každému tvému commitu – identifikují, kdo změnu provedl.

### Nastavení jména

```bash
git config --global user.name "Tvoje Jméno"
```

Například:

```bash
git config --global user.name "Jan Novák"
```

### Nastavení emailu

```bash
git config --global user.email "tvuj@email.cz"
```

Použij **skutečný email** – v open source projektech jsou tyto informace veřejné.

### Nastavení editoru

Git občas potřebuje, abys napsal/a zprávu (například podrobnější popis commitu). Nastavíme editor, který se má otevřít:

**Notepad (Windows – nejjednodušší volba):**
```bash
git config --global core.editor notepad
```

**VS Code:**
```bash
git config --global core.editor "code --wait"
```

### Konce řádků na Windows

Windows používá pro konce řádků `CRLF`, zatímco Linux a macOS používají `LF`. Aby Git na Windows nezpůsoboval problémy při spolupráci s ostatními, nastav:

```bash
git config --global core.autocrlf true
```

Toto říká Gitu, aby při stahování souborů (checkout) převáděl `LF` na `CRLF` a při commitu zpět na `LF`. Ostatní tak vždy dostanou soubory s konci řádků, které jim vyhovují.

### Zobrazení aktuální konfigurace

```bash
git config --global --list
```

Výstup by měl obsahovat alespoň:

```
user.name=Tvoje Jméno
user.email=tvuj@email.cz
core.editor=notepad
core.autocrlf=true
```

---

## Shrnutí příkazů

| Příkaz | Popis |
|--------|-------|
| `git --version` | Zobrazí verzi Gitu |
| `git config --global user.name "Jméno"` | Nastaví uživatelské jméno |
| `git config --global user.email "email"` | Nastaví email |
| `git config --global core.editor notepad` | Nastaví editor na Notepad |
| `git config --global core.autocrlf true` | Nastaví zpracování konců řádků (Windows) |
| `git config --global --list` | Zobrazí celou konfiguraci |

---

[← Zpět na přehled](../README.md) | [Lokální práce →](../02-lokalni-prace/README.md)
