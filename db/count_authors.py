import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug12\catalog.db")
cur = con.cursor()

cur.execute("select count(id) from authors")
print("No. of Authors = ", cur.fetchone()[0])
con.close()




