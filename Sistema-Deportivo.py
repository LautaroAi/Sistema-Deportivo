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

 def registrar_jugador(nombre, edad, posicion):
    cursor.execute("INSERT INTO jugadores (nombre, edad, posicion) VALUES (?, ?, ?)", (nombre, edad, posicion))
    conn.commit()

# HU2: Listado de jugadores
listar_jugadores() 