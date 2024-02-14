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


# Función para marcar una tarea como completada
@click.command()
@click.option('--id', prompt='ID de la tarea', type=int, help='ID de la tarea que deseas marcar como completada.')
def completar_tarea(id):
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute("UPDATE tareas SET completada = ? WHERE id = ?", (1, id))
    conn.commit()
    click.echo('Tarea marcada como completada correctamente.')
    conn.close()
# Función para eliminar una tarea
@click.command()
@click.option('--id', prompt='ID de la tarea', type=int, help='ID de la tarea que deseas eliminar.')
def eliminar_tarea(id):
    conn = sqlite3.connect('tareas.db')
    c = conn.cursor()
    c.execute("DELETE FROM tareas WHERE id = ?", (id,))
    conn.commit()
    click.echo('Tarea eliminada correctamente.')
    conn.close()
# Agrupar todos los comandos en una sola interfaz de línea de comandos
@click.group()
def cli():
    pass
cli.add_command(agregar_tarea)
cli.add_command(ver_tareas)
cli.add_command(completar_tarea)
cli.add_command(eliminar_tarea)
# Llamada a la función principal para crear la base de datos si no existe
if __name__ == '__main__':
    crear_base_datos()
    cli()
