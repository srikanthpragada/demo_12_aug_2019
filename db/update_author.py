import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug12\catalog.db")
cur = con.cursor()

id = input("Enter id :")
email = input("Enter new email : ")

cur.execute("update authors set email = ? where id = ?", (email,id))

if cur.rowcount == 1:
    print("Updated Successfully!")
    con.commit()
else:
    print("Author id is not found!")


con.close()




