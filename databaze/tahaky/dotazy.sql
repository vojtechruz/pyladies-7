-- Vrat vse
select fact, source from cat_facts;
select * from cat_facts;

-- Vrat jen nektere sloupce
select fact from cat_facts;

-- Podminka - pouze radky ktere maji source s urcitou hodnotou
select fact, source from cat_facts where source = 'api';
select fact, source from cat_facts where source = 'user';