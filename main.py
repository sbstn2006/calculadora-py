import sqlite3
import os
from login import Login


def inicializar_base_de_datos():
    """Crea la base de datos local SQLite y la tabla de usuarios si no existen."""
    ruta_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.db")
    conexion = sqlite3.connect(ruta_db)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                usuario TEXT UNIQUE NOT NULL,
                clave TEXT NOT NULL
            )
        """)
        conexion.commit()
    except Exception as error:
        print(f"Error al inicializar la base de datos: {error}")
    finally:
        conexion.close()


if __name__ == "__main__":
    inicializar_base_de_datos()
    app = Login()
    app.ejecutar()
