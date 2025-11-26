import sqlite3

#CRUD
# create - read - update - delete

con = sqlite3.connect('Banquinho.db')
c = con.cursor()

c. execute(''' CREATE TABLE IF NOT EXISTS tabela(
           
           nome TEXT,
           idade INTEGER

           
           
           
           
           )''')

c.execute('INSERT INTO tabela VALUES(?,?)', ('Julia', 40))
con.commit()

c.execute()



con.close()

