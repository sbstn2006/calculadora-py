import tkinter as tk
from tkinter import messagebox


class Calculadora:
    def __init__(self, parent):
        self.parent = parent

        # Colores para la interfaz
        self.calc_bg = "#ffffff"
        self.btn_bg = "#e0e0e0"
        self.btn_active = "#d5d5d5"
        self.op_bg = "#f39c12"
        self.op_active = "#d68910"
        self.eq_bg = "#2ecc71"
        self.eq_active = "#27ae60"

        # RF08 - Estructura de datos: Lista para almacenar el historial de operaciones
        self.historial = []

        # Cadena de caracteres que representa la expresión matemática actual
        self.expresion = ""

        self.crear_diseno()

    def crear_diseno(self):
        # Distribución en dos secciones principales
        # Panel Izquierdo: Calculadora
        self.frame_calc = tk.LabelFrame(
            self.parent,
            text=" Calculadora ",
            font=("Helvetica", 11, "bold"),
            bg="#f4f6f9",
            padx=10,
            pady=10
        )
        self.frame_calc.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Panel Derecho: Historial
        self.frame_hist = tk.LabelFrame(
            self.parent,
            text=" Historial de Operaciones ",
            font=("Helvetica", 11, "bold"),
            bg="#f4f6f9",
            padx=10,
            pady=10
        )
        self.frame_hist.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

        # --- 1. Componentes de la Calculadora ---
        # Pantalla de visualización (Entry)
        self.txt_pantalla = tk.Entry(
            self.frame_calc,
            font=("Consolas", 18),
            justify="right",
            bd=5,
            relief=tk.SUNKEN,
            bg=self.calc_bg
        )
        self.txt_pantalla.grid(row=0, column=0, columnspan=4, ipady=8, pady=(0, 15), sticky="nsew")

        # Configuración de pesos para redimensionamiento en cuadrícula
        for i in range(1, 6):
            self.frame_calc.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.frame_calc.grid_columnconfigure(j, weight=1)

        # Botones Fila 1
        self.crear_boton('C', 1, 0, self.op_bg, self.op_active)
        self.crear_boton('←', 1, 1, self.op_bg, self.op_active)
        self.crear_boton('/', 1, 2, self.op_bg, self.op_active)
        self.crear_boton('*', 1, 3, self.op_bg, self.op_active)

        # Botones Fila 2
        self.crear_boton('7', 2, 0, self.btn_bg, self.btn_active)
        self.crear_boton('8', 2, 1, self.btn_bg, self.btn_active)
        self.crear_boton('9', 2, 2, self.btn_bg, self.btn_active)
        self.crear_boton('-', 2, 3, self.op_bg, self.op_active)

        # Botones Fila 3
        self.crear_boton('4', 3, 0, self.btn_bg, self.btn_active)
        self.crear_boton('5', 3, 1, self.btn_bg, self.btn_active)
        self.crear_boton('6', 3, 2, self.btn_bg, self.btn_active)
        self.crear_boton('+', 3, 3, self.op_bg, self.op_active)

        # Botones Fila 4
        self.crear_boton('1', 4, 0, self.btn_bg, self.btn_active)
        self.crear_boton('2', 4, 1, self.btn_bg, self.btn_active)
        self.crear_boton('3', 4, 2, self.btn_bg, self.btn_active)

        # Botón Igual ("=") que ocupa filas 4 y 5 en la columna 3
        btn_igual = tk.Button(
            self.frame_calc,
            text="=",
            font=("Helvetica", 14, "bold"),
            bg=self.eq_bg,
            fg="white",
            activebackground=self.eq_active,
            activeforeground="white",
            relief=tk.RAISED,
            command=self.calcular
        )
        btn_igual.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=2, pady=2)

        # Botones Fila 5
        # Botón "0" que se expande a dos columnas
        btn_cero = tk.Button(
            self.frame_calc,
            text="0",
            font=("Helvetica", 12, "bold"),
            bg=self.btn_bg,
            activebackground=self.btn_active,
            relief=tk.RAISED,
            command=lambda: self.presionar('0')
        )
        btn_cero.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)

        self.crear_boton('.', 5, 2, self.btn_bg, self.btn_active)

        # --- 2. Componentes del Historial ---
        # Contenedor intermedio para alinear Listbox y Scrollbar juntos
        frame_lista = tk.Frame(self.frame_hist, bg="#f4f6f9")
        frame_lista.pack(fill=tk.BOTH, expand=True)

        self.list_historial = tk.Listbox(
            frame_lista,
            font=("Consolas", 10),
            bg="white",
            selectmode=tk.SINGLE
        )
        self.list_historial.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list_historial.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.list_historial.yview)

        # Botón para borrar el historial debajo del contenedor del historial
        btn_borrar_hist = tk.Button(
            self.frame_hist,
            text="Limpiar Historial",
            font=("Helvetica", 9, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            relief=tk.FLAT,
            command=self.limpiar_historial
        )
        btn_borrar_hist.pack(fill=tk.X, pady=(10, 0), ipady=3)

    def crear_boton(self, texto, fila, col, bg, active_bg):
        """Crea un botón genérico en la cuadrícula de la calculadora."""
        btn = tk.Button(
            self.frame_calc,
            text=texto,
            font=("Helvetica", 12, "bold"),
            bg=bg,
            activebackground=active_bg,
            relief=tk.RAISED,
            command=lambda: self.presionar(texto) if texto not in ('C', '←') else (self.limpiar() if texto == 'C' else self.borrar_ultimo())
        )
        btn.grid(row=fila, column=col, sticky="nsew", padx=2, pady=2)

    def presionar(self, caracter):
        """Agrega un dígito u operador a la expresión actual."""
        # Prevenir múltiples operadores consecutivos de división o multiplicación para evitar errores sencillos
        if len(self.expresion) > 0 and caracter in ('/', '*') and self.expresion[-1] in ('+', '-', '*', '/'):
            # Reemplaza el último operador por el nuevo
            self.expresion = self.expresion[:-1] + caracter
        else:
            self.expresion += caracter
        self.actualizar_pantalla()

    def limpiar(self):
        """Borra por completo la pantalla actual."""
        self.expresion = ""
        self.actualizar_pantalla()

    def borrar_ultimo(self):
        """Borra el último carácter ingresado."""
        self.expresion = self.expresion[:-1]
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        """Refleja la expresión actual en la caja de texto."""
        self.txt_pantalla.delete(0, tk.END)
        self.txt_pantalla.insert(0, self.expresion)

    def calcular(self):
        """Realiza el cálculo de la expresión matemática."""
        exp = self.expresion.strip()

        # RF06 - Validación de campos vacíos
        if not exp:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una operación matemática.")
            return

        try:
            # RF06 - Validación de datos incorrectos
            # Se restringe la evaluación a caracteres permitidos
            for char in exp:
                if char not in "0123456789+-*/. ":
                    raise ValueError("Caracteres no permitidos")

            # Evaluar matemáticamente la expresión
            resultado = eval(exp)

            # Formatear el resultado: si es un decimal cerrado, convertir a entero
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            elif isinstance(resultado, float):
                # Limitar a 6 decimales para mejor legibilidad
                resultado = round(resultado, 6)

            linea_operacion = f"{exp} = {resultado}"

            # RF08 - Guardado en la estructura de datos (lista de Python)
            self.historial.append(linea_operacion)

            # Reflejar el nuevo elemento en la interfaz (Listbox)
            self.list_historial.insert(tk.END, linea_operacion)
            self.list_historial.see(tk.END)  # Auto scroll hacia el final

            # Colocar el resultado en pantalla para continuar operaciones
            self.expresion = str(resultado)
            self.actualizar_pantalla()

        except ZeroDivisionError:
            # RF06 - Validación de división entre cero
            messagebox.showerror("Error de cálculo", "No se permite la división entre cero.")
            self.limpiar()
        except Exception:
            # RF06 - Validación de datos incorrectos / error de formato
            messagebox.showerror("Error de cálculo", "Expresión matemática incorrecta.")
            self.limpiar()

    def limpiar_historial(self):
        """Limpia el historial de operaciones de la estructura y la UI."""
        self.historial.clear()
        self.list_historial.delete(0, tk.END)
        messagebox.showinfo("Historial", "Se ha limpiado el historial de operaciones.")
