import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug12\catalog.db")
cur = con.cursor()

f = open("authors.txt","rt")
rows  = []
for line in f:
    rows.append(line.strip('\n').split(','))

f.close()

# print(rows)

try:
    cur.executemany("insert into authors(name,email,phone) values(?,?,?)",
                    rows)
    print(f"Inserted {cur.rowcount} row(s).")
    con.commit()
except Exception as ex:
    print("Authors were not added due to error : ", ex)


con.close()




