#coding:utf-8
import sqlite3

try:
	connection=sqlite3.connect("baseSqlite.db")
	cursor=connection.cursor()

	req= cursor.execute("SELECT name from sqlite_master WHERE type='table';")
	print(cursor.fetchall())
	req= cursor.execute("SELECT *from tt_users;")

	for row in req.fetchall():
		print(row[1])

except Exception as e:
	print("[ERREUR]",e)
	connection.rollback()


finally :
	connection.close()


"""new_user =(cursor.lastrowid,"Gani",23)
cursor.execute('INSERT INTO tt_users VALUES(?,?,?)',new_user)
connection.commit()
print("nouvelle utilisateur ajouté !")"""

"""my_username=("Soul",)
cursor.execute('SELECT * FROM tt_users WHERE user_name= ?',my_username)
result =cursor.fetchone()
print(f"Le nom d'utilisateur est : {result}")"""

