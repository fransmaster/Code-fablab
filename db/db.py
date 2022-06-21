import sqlite3
import perfumes

x= perfumes.Perfume('eros','versace',200.99)
print(x.nombre)

con =sqlite3.connect('perfume.db')
data=con.cursor()



#crear tabla
#data.execute('''CREATE TABLE 'perfumes'(
#'id' INTEGER PRIMARY KEY AUTOINCREMENT,
#'nombre' VARCHAR,
#'marca' VARCHAR,
#'precio' REAL); ''')

#insertar datos
#data.execute('''INSERT INTO perfumes('nombre','marca','precio') VALUES ('montblac','legend',178.99);''')

#visualizar datos
#data.execute('''SELECT * FROM perfumes; ''')
#print(data.fetchall())

#data.execute('''UPDATE perfumes SET precio =420.69 WHERE nombre ='eros';''')
#con.execute(''' DELETE from perfumes WHERE nombre= 'eros';''')

data.execute('''INSERT INTO perfumes('nombre','marca','precio') VALUES(:nombre, :marca, :precio),{'nombre': x.nombre, 'marca': x.marca, 'precio': x.precio});''')
con.commit()
con.close()
