import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug12\catalog.db")
cur = con.cursor()

cur.execute("select * from authors order by id")

for row in cur.fetchall():
    print(f"{row[0]:5} {row[1]:20} {row[2]:30}  {row[3]}")


con.close()




