import sqlite3
import os
import tkinter as tk
from tkinter import messagebox


class Registro:
    def __init__(self, parent):
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Registro de Usuario")
        self.ventana.geometry("380x380")
        self.ventana.resizable(False, False)

        # Paleta de colores / Estilos
        self.bg_color = "#f4f6f9"
        self.fg_color = "#333333"
        self.primary_color = "#4a90e2"
        self.primary_hover = "#357abd"

        self.ventana.configure(bg=self.bg_color)
        self.ventana.transient(parent)  # Mantiene la ventana de registro encima de la principal
        self.ventana.grab_set()         # Captura toda la interacción hasta que se cierre

        self.ruta_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.db")

        self.crear_componentes()

    def crear_componentes(self):
        # Título
        lbl_titulo = tk.Label(
            self.ventana,
            text="Crear Cuenta",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        lbl_titulo.pack(pady=(30, 20))

        # Nombre Completo
        frame_nombre = tk.Frame(self.ventana, bg=self.bg_color)
        frame_nombre.pack(pady=8)

        lbl_nombre = tk.Label(
            frame_nombre,
            text="Nombre Completo:",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w",
            width=15
        )
        lbl_nombre.pack(side=tk.LEFT)

        self.txt_nombre = tk.Entry(
            frame_nombre,
            font=("Helvetica", 11),
            width=18
        )
        self.txt_nombre.pack(side=tk.LEFT, ipady=3)
        self.txt_nombre.focus()

        # Usuario
        frame_usuario = tk.Frame(self.ventana, bg=self.bg_color)
        frame_usuario.pack(pady=8)

        lbl_usuario = tk.Label(
            frame_usuario,
            text="Usuario:",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w",
            width=15
        )
        lbl_usuario.pack(side=tk.LEFT)

        self.txt_usuario = tk.Entry(
            frame_usuario,
            font=("Helvetica", 11),
            width=18
        )
        self.txt_usuario.pack(side=tk.LEFT, ipady=3)

        # Clave
        frame_clave = tk.Frame(self.ventana, bg=self.bg_color)
        frame_clave.pack(pady=8)

        lbl_clave = tk.Label(
            frame_clave,
            text="Contraseña:",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w",
            width=15
        )
        lbl_clave.pack(side=tk.LEFT)

        self.txt_clave = tk.Entry(
            frame_clave,
            font=("Helvetica", 11),
            show="*",
            width=18
        )
        self.txt_clave.pack(side=tk.LEFT, ipady=3)

        # Botón Registrar
        btn_registrar = tk.Button(
            self.ventana,
            text="Registrar",
            font=("Helvetica", 11, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground=self.primary_hover,
            activeforeground="white",
            cursor="hand2",
            relief=tk.FLAT,
            command=self.registrar,
            width=18
        )
        btn_registrar.pack(pady=(25, 10), ipady=5)

        # Botón Cancelar
        btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            font=("Helvetica", 9),
            bg=self.bg_color,
            fg="#777777",
            activebackground=self.bg_color,
            activeforeground=self.primary_color,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.ventana.destroy
        )
        btn_cancelar.pack()

    def registrar(self):
        nombre = self.txt_nombre.get().strip()
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        # RF06 - Validación de campos vacíos
        if not nombre or not usuario or not clave:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        if not os.path.exists(self.ruta_db):
            messagebox.showerror("Error", "La base de datos no está inicializada.")
            return

        conexion = sqlite3.connect(self.ruta_db)
        try:
            cursor = conexion.cursor()

            # Validación de usuario duplicado
            cursor.execute("SELECT id FROM usuarios WHERE usuario = ?", (usuario,))
            if cursor.fetchone():
                messagebox.showerror("Error de registro", "El nombre de usuario ya existe. Intente con otro.")
                return

            # RF01 - Registro de usuario
            cursor.execute(
                "INSERT INTO usuarios (nombre, usuario, clave) VALUES (?, ?, ?)",
                (nombre, usuario, clave)
            )
            conexion.commit()

            # RF07 - Mensaje de confirmación
            messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado correctamente.")
            self.ventana.destroy()

        except Exception as error:
            messagebox.showerror("Error", f"Error al intentar registrar usuario: {error}")
        finally:
            conexion.close()
