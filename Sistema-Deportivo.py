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

# HU1: Registro de jugadores
def registrar_jugador(nombre, edad, posicion):
    cursor.execute("INSERT INTO jugadores (nombre, edad, posicion) VALUES (?, ?, ?)", (nombre, edad, posicion))
    conn.commit()

registrar_jugador("Carlos Pérez", 25, "Defensa")
registrar_jugador("Luis Gómez", 22, "Delantero")
registrar_jugador("Andrés Vidal", 27, "Arquero")


# HU2: Listado de jugadores
def listar_jugadores():
    cursor.execute("SELECT nombre, edad, posicion FROM jugadores")
    datos = cursor.fetchall()
    print("\n📋 Lista de Jugadores:")
    print(tabulate(datos, headers=["Nombre", "Edad", "Posición"], tablefmt="pretty"))

listar_jugadores()


# HU3: Registro de partidos
def registrar_partido(fecha, rival, resultado):
    cursor.execute("INSERT INTO partidos (fecha, rival, resultado) VALUES (?, ?, ?)", (fecha, rival, resultado))
    conn.commit()

registrar_partido("2025-06-01", "Tigres FC", "Ganado")
registrar_partido("2025-06-05", "Leones FC", "Perdido")
registrar_partido("2025-06-10", "Águilas FC", "Ganado")


# HU4: Filtro de partidos ganados
def filtrar_partidos_por_resultado(resultado):
    cursor.execute("SELECT fecha, rival, resultado FROM partidos WHERE resultado = ?", (resultado,))
    datos = cursor.fetchall()
    print(f"\n🎯 Partidos con resultado '{resultado}':")
    print(tabulate(datos, headers=["Fecha", "Rival", "Resultado"], tablefmt="pretty"))

filtrar_partidos_por_resultado("Ganado")