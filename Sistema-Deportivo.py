import sqlite3
from tabulate import tabulate

# Conexión y creación de tablas
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE jugadores (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
edad INTEGER NOT NULL,
posicion TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE partidos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fecha TEXT NOT NULL,
rival TEXT NOT NULL,
resultado TEXT CHECK(resultado IN ('Ganado', 'Perdido', 'Empatado')) NOT NULL
)
''')

# Funciones

def listar_jugadores():
    cursor.execute("SELECT nombre, edad, posicion FROM jugadores")
    datos = cursor.fetchall()
    print("\n📋 Lista de Jugadores:")
    print(tabulate(datos, headers=["Nombre", "Edad", "Posición"], tablefmt="pretty"))

# HU2: Listado de jugadores
listar_jugadores()

