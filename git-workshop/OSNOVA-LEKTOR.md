je# Osnova pro lektora

Tento dokument slouží jako průvodce workshopem. Obsahuje časové odhady, poznámky k výkladu a tipy na co si dát pozor.

Materiály pro účastníky jsou v jednotlivých složkách – tento dokument je jen pro tebe.

---

## Přehled a časový plán

| # | Sekce | Čas |
|---|-------|-----|
| 1 | Úvod | 20 min |
| 2 | Lokální práce | 40 min |
| 3 | Grafické zobrazení | 5 min |
| 4 | Ignorování souborů | 15 min |
| — | **Přestávka** | 10 min |
| 5 | GitHub | 15 min |
| 6 | Práce na internetu | 25 min |
| 7 | Větvení | 40 min |
| — | **Přestávka** | 10 min |
| 8 | Spolupráce | 20 min |
| 9 | Cvičení: Receptář | 30 min |
| 10 | Grafická rozhraní | 10 min |
| 11 | Užitečné příkazy | 10 min |
| — | Závěr a dotazy | 10 min |
| | **Celkem** | **~4,5 hod** |

Časy jsou orientační – přizpůsob tempu skupiny. Cvičení (receptář) může trvat déle.

---

## 1. Úvod (20 min)

**Cíl:** Všichni vědí, co je Git a proč ho používat, mají nainstalovaný a nakonfigurovaný Git.

### Zahájení

- Přivítej skupinu, představ sebe i kouče
- Zeptej se, kdo už Git někdy používal → uprav hloubku výkladu
- Vysvětli, jak bude workshop probíhat (materiály jsou online, kouči pomáhají)

### Výklad

- **Proč verzovat** – ukáž příklad s `projekt_final_v2_opravdu_final.zip`; nech skupinu se zamyslet, jak to řeší oni sami
- **Distribuovanost** – zdůrazni práci offline; tohle je klíčová věc, která Git odlišuje od starších systémů (SVN, CVS)
- Krátce zmiň alternativy ke Gitu (Mercurial, SVN) – jen pro kontext, nerozebírej

### Kontrola instalace

- Nech všechny spustit `git --version`
- Kouči obcházejí a pomáhají těm, kteří Git nemají

### Konfigurace

- Projdi `user.name`, `user.email`, `core.editor`, `core.autocrlf` (Windows)
- **Zdůrazni:** email bude veřejný v commitech, ať použijí skutečný
- Nech všechny spustit `git config --global --list` a ověřit nastavení

### Časté problémy

- Git není v PATH (Windows) → restart terminálu nebo reinstalace
- Uživatel otevřel cmd místo Git Bash → nasměruj ho
- Chybí oprávnění k instalaci → potřebuje admin

---

## 2. Lokální práce (40 min)

**Cíl:** Účastníci zvládají základní cyklus: init → add → commit → log.

### Výklad

- **Repozitář a složka `.git`** – inicializuj repozitář živě, ukaž složku `.git`, ale varuj před ruční úpravou
- **Staging area** – tohle je největší konceptuální krok; věnuj mu čas
  - Nakresli na tabuli/sdílenou plochu: `Working Directory → Staging → Repository`
  - Analogie: staging area je jako přípravná krabice – do zásilky (commitu) vložíš jen to, co tam dáš
- **Commit zprávy** – zdůrazni, že zpráva by měla popisovat *proč*, ne *co* (co je vidět v diffu)

### Živá ukázka – básnička

Projdi celý cyklus se skupinou:

1. `mkdir muj-projekt && cd muj-projekt`
2. `git init` → ukaž `.git`
3. Vytvoř `basnicka.txt` v editoru
4. `git status` → červený soubor
5. `git add basnicka.txt`
6. `git status` → zelený soubor
7. `git commit -m "Pridana basnicka"`
8. Zopakuj – přidej sloku, projdi cyklus znovu
9. `git log` a `git log --oneline`

### git diff – důraz

- Spusť diff **před** `git add` i **po** něm
- Ukaž `git diff`, `git diff --staged`, `git diff HEAD`
- Mnoho účastníků si tuto trojici plete – kresli schéma

### Časté problémy

- Účastník commitne bez zprávy → otevře se editor, zavře ho pomocí `:q!` (vim) nebo zavřením okna (notepad) → vysvětli nastavení editoru
- Záměna `git add .` a `git add soubor.txt` → obojí je správně, tečka přidá vše
- `git status` ukazuje detached HEAD → pravděpodobně spustili `git checkout <hash>` omylem

---

## 3. Grafické zobrazení (5 min)

**Cíl:** Účastníci znají `gitk` a umějí ho otevřít.

- Spusť `gitk --all` a ukaž co se zobrazuje
- Zatím nemají větve, takže je to jednoduché – dobré na demonstraci
- Zmiň, že gitk je hlavně užitečný u větví (vrátíme se k tomu v sekci 7)
- Ukaž i `git log --all --oneline --graph --decorate` jako terminálovou alternativu

---

## 4. Ignorování souborů (15 min)

**Cíl:** Účastníci umí vytvořit `.gitignore` a chápou, že patří do repozitáře.

### Výklad

- Ukaž situaci *bez* `.gitignore`: vytvoř `debug.log`, spusť `git status` → obtěžuje nás
- Vytvoř `.gitignore`, napiš `debug.log`, ukaž `git status` znovu → soubor zmizel
- Projdi vzory: `*.log`, `debug?.log`, `build/`
- **Zdůrazni:** `.gitignore` se commituje! Je to součást projektu.

### Důležité upozornění

- Vysvětli případ already-committed souboru – toto je časté úskalí
- `git rm --cached` neodstraní soubor fyzicky

### Tip

Zmiň [github.com/github/gitignore](https://github.com/github/gitignore) – šablony pro různé technologie. Účastníci si je mohou prohlédnout, ale na workshopu neřešíme.

---

## 5. GitHub (15 min)

**Cíl:** Účastníci jsou zaregistrováni na GitHubu a chápou rozdíl Git vs. GitHub.

### Výklad

- **Git vs. GitHub** – toto je nejčastější zmatek; zdůrazni, že Git funguje i bez GitHubu
- Ukaž GitLab jako alternativu – existují firmy, kde se GitLab používá místo GitHubu
- **Open source** – ukaž živě pár velkých projektů na GitHubu (Python, VS Code)
- **Portfolio** – motivuj účastníky dávat kód na GitHub; i začátečnické projekty mají hodnotu

### Registrace

- Nech všechny vytvořit účet, pokud ho nemají
- Kouči pomáhají s ověřením emailu apod.

---

## 6. Práce na internetu (25 min)

**Cíl:** Účastníci umí vytvořit repozitář na GitHubu, naklonovat ho, pushovat a pullovat.

### Živá ukázka

1. Vytvoř nový repozitář na GitHubu (sdílej obrazovku)
   - Ukaž volbu `.gitignore` a `README.md` při zakládání
2. Naklonuj ho: `git clone <url>`
3. Přidej soubor, commit, `git push`
4. Ověř na GitHubu, že soubor tam je
5. Ručně uprav soubor přímo na GitHubu (klikni na tužku)
6. Lokálně zkontroluj – soubor se **nezměnil**
7. `git pull` → teď je aktuální

### Zdůrazni

- Lokální a vzdálený repozitář jsou dvě oddělené kopie
- `git push` / `git pull` jsou explicitní synchronizace
- Doporučený postup: začínáme každý den `git pull`

### Časté problémy

- Chybí autentizace při push → GitHub vyžaduje Personal Access Token nebo SSH klíč; kouči pomohou
- Účastník klonoval přes SSH ale nemá klíče → přepni na HTTPS

---

## 7. Větvení (40 min)

**Cíl:** Účastníci chápou princip větví, umí je vytvořit, přepínat a mergovat včetně řešení konfliktů.

### Výklad – princip

- Nakresli schéma větví na tabuli/sdílenou plochu
- Zdůrazni: `master` je hlavní větev, feature branches jsou dočasné
- Analogie: větev je jako pracovní kopie, na které pracuješ izolovaně

### Živá ukázka – větve

1. `git branch` → ukáže jen master
2. `git branch nazev-basnicky`
3. `git branch` → ukáže obě větve, hvězdička na master
4. `git checkout nazev-basnicky` (zmiň i `git switch`)
5. `git branch` → hvězdička se přesunula
6. Ukaž v `gitk --all`
7. Uprav soubor, commit
8. Ukaž `git log` – větev je napřed

### Merge bez konfliktu

1. `git checkout master`
2. `git merge nazev-basnicky`
3. Ukaž výsledek v `git log` a `gitk --all`
4. `git branch -d nazev-basnicky` → úklid

### Merge s konfliktem – pomalý postup

Toto je nejnáročnější část – věnuj mu dostatek času.

1. Vytvoř větev `doplneni-autora`
2. Uprav první řádek básničky v nové větvi, commitni
3. Přepni na master, uprav **stejné místo** jinak, commitni
4. `git merge doplneni-autora` → CONFLICT
5. Otevři soubor a ukáž `<<<<<<<`, `=======`, `>>>>>>>`
6. Vyřeš ručně, ukaž `git status` (unmerged paths)
7. `git add`, `git commit`

**Důležité:** Zdůrazni, že konflikt není průšvih – je to normální součást práce. Git jen říká: "Nevím, co chceš, rozhodni za mě."

### Časté problémy

- Účastník zapomene přepnout větev před mergem → `git branch` je rychlá kontrola
- Editor se otevře při merge commitu bez `-m` → zavřít s výchozí zprávou je OK
- Účastník neodstranil conflict markery → commit selže nebo soubor bude rozbití

---

## 8. Spolupráce (20 min)

**Cíl:** Účastníci chápou model fork + pull request a umí nastavit remote.

### Výklad

- Ukaž obrázek/diagram: původní repozitář → fork → clone → commit → PR
- Zdůrazni: fork je kopie, ke které máš plný přístup
- Pull request je "žádost o začlenění" – autor projektu ho může přijmout, odmítnout nebo okomentovat

### Živá ukázka

1. Forkni nějaký ukázkový repozitář (předem připrav)
2. Naklonuj fork
3. `git remote -v` → ukáže origin (fork)
4. Přidej upstream: `git remote add upstream <url-puvodniho>`
5. `git remote -v` → ukáže oba
6. Udělej změnu, push, PR na GitHubu

---

## 9. Cvičení: Receptář (30 min)

**Cíl:** Každý účastník projde celým cyklem fork → clone → commit → push → PR.

### Příprava (udělej předem)

- Vytvoř repozitář `receptar` na GitHubu
- Přidej `README.md` s popisem a vzor receptu

### Průběh

1. Vysvětli zadání (viz [09-spoluprace-receptar](09-spoluprace-receptar/README.md))
2. Účastníci pracují samostatně, kouči pomáhají
3. Jakmile začnou přicházet PR, merguj je živě a ukazuj skupině
4. Na konci nech všechny udělat `git pull upstream master` → vidí cizí recepty

### Na co si dát pozor

- Konflikty při mergování PR (dva účastníci editují stejný soubor) → ukaž jako bonus jak je řešit na GitHubu
- Účastníci forkují špatný repozitář (lektorův, ne ten správný) → zkontroluj URL při klonování

---

## 10. Grafická rozhraní (10 min)

**Cíl:** Účastníci vědí, že existují grafické nástroje a kde je najít.

- Ukaž IntelliJ IDEA nebo PyCharm pokud ho účastníci znají
- Ukaž GitKraken – stačí screenshoty nebo live demo
- **Zdůrazni:** Nauč se příkazovou řádku nejdřív, pak GUI jako doplněk

---

## 11. Užitečné příkazy (10 min)

**Cíl:** Účastníci vědí, jak se dostat z nejčastějších problémů.

- Projdi reset, revert, restore
- Zdůrazni `--hard` jako nebezpečný příkaz
- Ukaž `git revert` jako bezpečnou alternativu pro pushnuté commity
- Nemusíš vše demonstrovat live – stačí projít tabulku příkazů

---

## Závěr a dotazy (10 min)

### Co jsme probrali

Stručně shrň journey: lokální práce → GitHub → větvení → spolupráce.

### Co dál

- [Pro Git](https://git-scm.com/book/cs/v2) – bezplatná kniha, existuje český překlad
- [Learn Git Branching](https://learngitbranching.js.org/?locale=cs_CZ) – interaktivní vizuální cvičení
- [GitHub Skills](https://skills.github.com) – interaktivní kurzy přímo na GitHubu
- Přispívání do open source: [firstcontributions.github.io](https://firstcontributions.github.io)

### Průzkum zpětné vazby

Pokud sbíráte zpětnou vazbu, zmiň odkaz nebo formulář.

---

## Obecné tipy pro lektora

- **Tempo:** Raději jdi pomaleji a dej lidem čas vyzkoušet si příkazy, než abys přednášel rychle
- **Kouči:** Před začátkem projdi s kouči osnovu – každý by měl vědět, co se probírá a jaký je postup při problémech
- **Chyby jsou OK:** Pokud uděláš chybu live, je to skvělá příležitost ukázat, jak se z ní dostat
- **Terminál na projekci:** Zvětši font terminálu (aspoň 18pt), používej světlé téma nebo vysoký kontrast
- **Nezahlcuj:** Je lepší, aby si účastníci odnesli solidní základy, než aby projeli vše povrchně
