import tkinter as tk
from calculadora import Calculadora


class PaginaInicial:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.ventana = tk.Tk()
        self.ventana.title("Página Principal - Calculadora")
        self.ventana.geometry("700x520")
        self.ventana.resizable(False, False)

        # Paleta de colores / Estilos
        self.bg_color = "#f4f6f9"
        self.header_bg = "#2c3e50"
        self.header_fg = "#ffffff"

        self.ventana.configure(bg=self.bg_color)
        self.crear_componentes()

    def crear_componentes(self):
        # Encabezado con mensaje de bienvenida (RF03)
        frame_header = tk.Frame(self.ventana, bg=self.header_bg, height=60)
        frame_header.pack(fill=tk.X, side=tk.TOP)
        frame_header.pack_propagate(False)

        lbl_bienvenida = tk.Label(
            frame_header,
            text=f"Bienvenido, {self.nombre_usuario}",
            font=("Helvetica", 14, "bold"),
            bg=self.header_bg,
            fg=self.header_fg,
            anchor="w",
            padx=20
        )
        lbl_bienvenida.pack(fill=tk.BOTH, expand=True)

        # Contenedor principal para la calculadora y el historial
        frame_cuerpo = tk.Frame(self.ventana, bg=self.bg_color)
        frame_cuerpo.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Inicializa e inserta la calculadora (RF04)
        self.calculadora = Calculadora(frame_cuerpo)

    def ejecutar(self):
        self.ventana.mainloop()
