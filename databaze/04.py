import sqlite3
con = sqlite3.connect("example.db")

cursor = con.cursor()
cursor.execute("CREATE TABLE if not exists movie(title, year, score)")

# cursor.execute("INSERT INTO movie values ('Život Briana', 1979, 86)")
# cursor.execute("INSERT INTO movie values ('Babovřesky', 2014, 24)")
#



# cursor.execute("INSERT INTO movie values (?,?,?)", ('Život Briana', 1979, 86))
cursor.executemany("INSERT INTO movie values (?,?,?)", [('Život Briana', 1979, 86),('Babovřesky', 2014, 24)])

result = cursor.execute("SELECT * from movie")
print(result.fetchone())
print(result.fetchall())

con.commit()

