import sqlite3

con = sqlite3.connect(r"e:\classroom\python\aug12\catalog.db")
cur = con.cursor()

name  = input("Enter name  :")
email = input("Enter email :")
phone = input("Enter phone :")

try:
    cur.execute("insert into authors(name,email,phone) values(?,?,?)",
                        (name,email,phone))
    print("Added Author Successfully!")
    con.commit()
except Exception as ex:
    print("Author was not added due to error : ", ex)


con.close()




