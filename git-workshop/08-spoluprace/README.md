# 8. Spolupráce – Fork a Pull Request

Co dělat, když chceš přispět do projektu, ke kterému nemáš přístup? Přesně to řeší fork a pull request.

---

## Problém: Ne každý má právo pushovat

Když najdeš zajímavý open source projekt a chceš opravit chybu nebo přidat funkci, nemáš přístup k původnímu repozitáři. Nemůžeš tedy přímo pushovat.

Řešení: **fork + pull request**.

---

## Fork – vlastní kopie repozitáře

**Fork** je kopie cizího repozitáře ve tvém GitHub účtu. Je to plnohodnotný repozitář, ke kterému máš plný přístup.

```
Původní repozitář             Tvůj fork (kopie)
github.com/nekdo/projekt  →   github.com/ty/projekt
```

### Jak vytvořit fork

1. Přejdi na stránku repozitáře, do kterého chceš přispět
2. Klikni na tlačítko **Fork** vpravo nahoře
3. Vyber svůj účet jako cíl
4. Fork se vytvoří ve tvém účtu

---

## Pracovní postup: Fork → Clone → Commit → PR

### 1. Naklonuj svůj fork

```bash
git clone https://github.com/tvoje-jmeno/projekt.git
cd projekt
```

### 2. Udělej změny a commitni

```bash
# Uprav soubory...
git add .
git commit -m "Opravena chyba v XYZ"
```

### 3. Pushni do svého forku

```bash
git push
```

### 4. Vytvoř Pull Request

Na GitHubu přejdi na svůj fork a klikni na **Compare & pull request**. Vyplň:
- Název (stručně, co změna dělá)
- Popis (proč a jak)

Klikni **Create pull request**.

Autor původního projektu teď vidí tvůj návrh, může ho okomentovat nebo přijmout.

---

## Nastavení vzdálených repozitářů (remote)

Po naklonování forku máš nastavený jen jeden remote – svůj fork (`origin`). Ale pokud chceš sledovat změny v původním repozitáři, potřebuješ přidat druhý remote.

### Zobrazení aktuálních remote

```bash
git remote -v
```

```
origin  https://github.com/tvoje-jmeno/projekt.git (fetch)
origin  https://github.com/tvoje-jmeno/projekt.git (push)
```

Vidíš jen svůj fork.

### Přidání původního repozitáře jako remote

Konvence je pojmenovat ho `upstream`:

```bash
git remote add upstream https://github.com/autor/projekt.git
```

Zkontroluj:

```bash
git remote -v
```

```
origin    https://github.com/tvoje-jmeno/projekt.git (fetch)
origin    https://github.com/tvoje-jmeno/projekt.git (push)
upstream  https://github.com/autor/projekt.git (fetch)
upstream  https://github.com/autor/projekt.git (push)
```

### Aktualizace forku z původního repozitáře

Původní repozitář se mezitím mohl změnit. Jak dostat změny do svého forku?

```bash
# Stáhni změny z původního repozitáře
git pull upstream master

# Odešli je do svého forku
git push origin master
```

---

## Cvičení: Přispění na prezenci

Lektor má repozitář `prezencka` na GitHubu. Každý účastník do něj přidá svůj řádek.

### Postup pro každého účastníka:

1. **Fork** repozitáře `prezencka` od lektora
2. **Clone** svého forku:
   ```bash
   git clone https://github.com/tvoje-jmeno/prezencka.git
   cd prezencka
   ```
3. Přidej svůj řádek do souboru `prezence.txt`
4. Commitni:
   ```bash
   git add prezence.txt
   git commit -m "Pridano jmeno: Jan Novák"
   ```
5. Push:
   ```bash
   git push
   ```
6. Na GitHubu vytvoř **Pull Request** do původního repozitáře lektora

Lektor pull requesty projde a mergne.

---

## Přehled pojmů

| Pojem | Vysvětlení |
|-------|-----------|
| **Fork** | Kopie cizího repozitáře ve tvém GitHub účtu |
| **Pull Request (PR)** | Návrh na začlenění změn z tvého forku do původního repozitáře |
| **origin** | Výchozí název pro vzdálený repozitář (typicky tvůj fork) |
| **upstream** | Konvenční název pro původní repozitář, ze kterého jsi forkoval/a |

## Shrnutí příkazů

| Příkaz | Popis |
|--------|-------|
| `git remote -v` | Zobrazí všechny nastavené remote |
| `git remote add jmeno url` | Přidá nový remote |
| `git pull upstream master` | Stáhne změny z upstream do aktuální větve |
| `git push origin master` | Odešle změny do svého forku |

---

[← Větvení](../07-vetveni/README.md) | [Cvičení: Receptář →](../09-spoluprace-receptar/README.md)
