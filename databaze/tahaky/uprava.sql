create table cat_facts (fact varchar20, source varchar20);
insert into cat_facts values ('fact1', 'api')
update cat_facts set source = 'user' where ROWID = 2
select * from cat_facts