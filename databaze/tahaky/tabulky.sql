-- Vytvori novou tabulku se sloupci fact a source, ktere jsou retezce az 20 znaku dlouhe
create table cat_facts (fact varchar20, source varchar20);

-- Pro jednotlive sloupce muzeme nastavit ze hodnota nesmi byt prazdna
create table cat_facts (fact varchar20 not null, source varchar20 not null);

-- Smaze celou tabulku
drop table cat_facts;