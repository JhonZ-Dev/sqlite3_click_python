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

# Función para agregar una nueva tarea
@click.command()
@click.option('--nombre', prompt='Nombre de la tarea', help='Nombre de la tarea.')
@click.option('--descripcion', prompt='Descripción de la tarea', help='Descripción de la tarea.')
def agregar_tarea(nombre, descripcion):
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute("INSERT INTO tareas (nombre, descripcion, completada) VALUES (?, ?, ?)", (nombre, descripcion, 0))
    conn.commit()
    click.echo('Tarea agregada correctamente.')
    conn.close()