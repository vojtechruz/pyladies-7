-- Smaz vsechno z tabulky
delete from cat_facts;

-- Smaz vsechny radky podle zdroje
delete from cat_facts where source = 'user';
delete from cat_facts where source = 'api';
