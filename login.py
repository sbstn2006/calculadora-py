import sqlite3
import os
import tkinter as tk
from tkinter import messagebox
from registro import Registro
from pagina_inicial import PaginaInicial


class Login:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesión - Calculadora")
        self.ventana.geometry("380x350")
        self.ventana.resizable(False, False)

        # Paleta de colores / Estilos
        self.bg_color = "#f4f6f9"
        self.fg_color = "#333333"
        self.primary_color = "#4a90e2"
        self.primary_hover = "#357abd"

        self.ventana.configure(bg=self.bg_color)

        # Ruta de la base de datos
        self.ruta_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.db")

        self.crear_componentes()

    def crear_componentes(self):
        # Título
        lbl_titulo = tk.Label(
            self.ventana,
            text="Iniciar Sesión",
            font=("Helvetica", 20, "bold"),
            bg=self.bg_color,
            fg=self.primary_color
        )
        lbl_titulo.pack(pady=(35, 25))

        # Contenedor de usuario
        frame_usuario = tk.Frame(self.ventana, bg=self.bg_color)
        frame_usuario.pack(pady=8)

        lbl_usuario = tk.Label(
            frame_usuario,
            text="Usuario:",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w",
            width=10
        )
        lbl_usuario.pack(side=tk.LEFT)

        self.txt_usuario = tk.Entry(
            frame_usuario,
            font=("Helvetica", 11),
            width=20
        )
        self.txt_usuario.pack(side=tk.LEFT, ipady=3)
        self.txt_usuario.focus()

        # Contenedor de contraseña
        frame_clave = tk.Frame(self.ventana, bg=self.bg_color)
        frame_clave.pack(pady=8)

        lbl_clave = tk.Label(
            frame_clave,
            text="Contraseña:",
            font=("Helvetica", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w",
            width=10
        )
        lbl_clave.pack(side=tk.LEFT)

        self.txt_clave = tk.Entry(
            frame_clave,
            font=("Helvetica", 11),
            show="*",
            width=20
        )
        self.txt_clave.pack(side=tk.LEFT, ipady=3)

        # Botón Ingresar
        btn_ingresar = tk.Button(
            self.ventana,
            text="Ingresar",
            font=("Helvetica", 11, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground=self.primary_hover,
            activeforeground="white",
            cursor="hand2",
            relief=tk.FLAT,
            command=self.login,
            width=18
        )
        btn_ingresar.pack(pady=(25, 10), ipady=5)

        # Botón Registrarse
        btn_registrarse = tk.Button(
            self.ventana,
            text="Crear cuenta nueva",
            font=("Helvetica", 9, "underline"),
            bg=self.bg_color,
            fg="#555555",
            activebackground=self.bg_color,
            activeforeground=self.primary_color,
            cursor="hand2",
            relief=tk.FLAT,
            command=self.abrir_registro
        )
        btn_registrarse.pack()

    def login(self):
        usuario = self.txt_usuario.get().strip()
        clave = self.txt_clave.get().strip()

        # RF06 - Validación de campos vacíos
        if not usuario or not clave:
            messagebox.showwarning("Campos vacíos", "Por favor, ingrese usuario y contraseña.")
            return

        if not os.path.exists(self.ruta_db):
            messagebox.showerror("Error", "La base de datos no está inicializada.")
            return

        conexion = sqlite3.connect(self.ruta_db)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT nombre FROM usuarios WHERE usuario = ? AND clave = ?",
                (usuario, clave)
            )
            resultado = cursor.fetchone()

            # RF07 - Mensaje de confirmación o error
            if resultado:
                nombre_completo = resultado[0]
                messagebox.showinfo("Acceso permitido", f"Acceso exitoso. ¡Bienvenido, {nombre_completo}!")
                self.ventana.destroy()  # Cierra la ventana de login
                
                # Abre la página inicial (RF03)
                app_principal = PaginaInicial(nombre_completo)
                app_principal.ejecutar()
            else:
                messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")
        except Exception as error:
            messagebox.showerror("Error", f"Error al intentar validar credenciales: {error}")
        finally:
            conexion.close()

    def abrir_registro(self):
        # Abre la ventana de registro como Toplevel
        Registro(self.ventana)

    def ejecutar(self):
        self.ventana.mainloop()
