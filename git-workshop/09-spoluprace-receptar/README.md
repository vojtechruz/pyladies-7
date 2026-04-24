# 9. Cvičení: Receptář

Toto je praktické cvičení, kde si procvičíš celý pracovní postup spolupráce: fork, clone, přidání obsahu, push a pull request.

---

## Scénář

Lektor vytvoří na GitHubu repozitář **receptar** se základní strukturou. Každý účastník přidá vlastní recept.

---

## Krok 1: Lektor – příprava repozitáře

> Tento krok provádí lektor, ne účastníci.

1. Vytvoř nový repozitář `receptar` na GitHubu
2. Přidej soubor `README.md`:

```markdown
# Receptář

Společný receptář PyLadies workshopu.

## Jak přispět

1. Forkni tento repozitář
2. Přidej svůj recept jako nový soubor do složky `recepty/`
3. Vytvoř Pull Request
```

3. Vytvoř složku `recepty/` s ukázkovým receptem `recepty/vzor.md`:

```markdown
# Název receptu

**Počet porcí:** X  
**Čas přípravy:** Y minut

## Ingredience

- ingredience 1
- ingredience 2

## Postup

1. Krok první
2. Krok druhý
```

---

## Krok 2: Účastníci – Fork

Každý účastník si udělá fork repozitáře `receptar`:

1. Přejdi na GitHub stránku lektorova repozitáře `receptar`
2. Klikni na tlačítko **Fork** vpravo nahoře
3. Vyber svůj účet jako cíl
4. Počkej, až se fork vytvoří

---

## Krok 3: Clone

Naklonuj svůj fork (ne lektorův repozitář – svůj!):

```bash
git clone https://github.com/TVOJE-JMENO/receptar.git
cd receptar
```

Ověř, že jsi naklonoval/a správný repozitář:

```bash
git remote -v
```

Měl/a bys vidět URL se svým uživatelským jménem.

---

## Krok 4: Přidání receptu

Vytvoř nový soubor ve složce `recepty/`. Pojmenuj ho podle svého receptu, např. `recepty/svickova.md`.

```bash
# Na Windows v Git Bash:
cat > recepty/svickova.md
```

Nebo soubor jednoduše vytvoř v editoru. Obsah:

```markdown
# Svíčková na smetaně

**Počet porcí:** 4  
**Čas přípravy:** 180 minut

## Ingredience

- 600 g hovězí svíčkové
- 2 mrkve
- 1 petržel
- 1 celer
- 2 cibule
- 200 ml smetany ke šlehání
- citronová šťáva, bobkový list, nové koření

## Postup

1. Zeleninu nakrájej na kostky a orestuj na oleji
2. Přidej maso a osmahni ze všech stran
3. Zalij vodou, přidej koření a dušuj 2 hodiny
4. Maso vyndej, šťávu rozmixuj se zeleninou
5. Přidej smetanu, dochut citronem
6. Podávej s houskovým knedlíkem a brusinkami
```

---

## Krok 5: Commit a Push

```bash
git status
git add recepty/svickova.md
git commit -m "Pridan recept: Svickova na smetane"
git push
```

Ověř na GitHubu, že soubor ve tvém forku existuje.

---

## Krok 6: Pull Request

1. Přejdi na GitHub – na stránku svého forku
2. GitHub pravděpodobně sám nabídne banner **"Compare & pull request"** – klikni na něj
3. Pokud ne: klikni na **Pull requests** → **New pull request**
4. Zkontroluj:
   - **base repository:** lektorův repozitář, větev `master`
   - **head repository:** tvůj fork, větev `master`
5. Vyplň název PR, např. `Přidán recept: Svíčková na smetaně`
6. Klikni **Create pull request**

---

## Krok 7: Lektor – mergování Pull Requestů

> Tento krok provádí lektor.

1. Přejdi na záložku **Pull requests** v repozitáři
2. Projdi jednotlivé PR
3. Klikni na PR → prohlédni změny → klikni **Merge pull request**
4. Potvrď merge

---

## Krok 8: Účastníci – synchronizace se serverem

Po mergování lektorových PR má původní repozitář nový obsah. Jak ho dostat do svého lokálního repozitáře?

Přidej upstream remote (pokud ještě nemáš):

```bash
git remote add upstream https://github.com/LEKTOR/receptar.git
```

Stáhni změny z původního repozitáře:

```bash
git pull upstream master
```

Teď máš lokálně i recepty ostatních. Odešli je do svého forku:

```bash
git push origin master
```

---

## Co jsme procvičili

- Forkování repozitáře
- Klonování forku
- Přidání souborů a commit
- Push do vlastního forku
- Vytvoření Pull Requestu
- Mergování PR (lektor)
- Synchronizace forku s upstream repozitářem

---

[← Spolupráce](../08-spoluprace/README.md) | [Grafická rozhraní →](../10-graficke-nastroje/README.md)
