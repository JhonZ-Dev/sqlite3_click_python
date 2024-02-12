import sqlite3
import click
# Función para crear la base de datos
def crear_base_datos():
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tareas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, descripcion TEXT, completada INTEGER)''')
    conn.commit()
    conn.close()