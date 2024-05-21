-- Vytvori novou tabulku se sloupci fact a source, ktere jsou retezce az 20 znaku dlouhe
-- datove typy https://www.sqlite.org/datatype3.html
create table cat_facts (fact varchar20, source varchar20);

-- Vytvori tabulku jen pokud neexistuje
create table if not exists cat_facts (fact varchar20, source varchar20);

-- Pro jednotlive sloupce muzeme nastavit ze hodnota nesmi byt prazdna
create table cat_facts (fact varchar20 not null, source varchar20 not null);

-- Smaze celou tabulku
drop table cat_facts;