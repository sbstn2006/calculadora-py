PROYECTO DE NIVELACIÓN: ESTRUCTURAS DE DATOS - PYTHON CON TKINTER
================================================================

DATOS DEL ESTUDIANTE:
---------------------
- Estudiante: Ramírez López Jim Sebastián
- Espacio académico: Diseño y Análisis de Requerimientos / Estructuras de Datos
- Docente: Alexander Navarro
- Fecha de sustentación: Jueves 09 de julio - 7:00 p.m.


DESCRIPCIÓN DEL PROYECTO:
-------------------------
Este sistema es una aplicación de escritorio desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica. Permite el registro de nuevos usuarios, inicio de sesión mediante credenciales seguras almacenadas en una base de datos local SQLite, y despliega una pantalla principal con un mensaje de bienvenida personalizado que aloja una calculadora funcional.


ESTRUCTURA DE ARCHIVOS DEL PROYECTO:
-------------------------------------
El código fuente está debidamente modulado en clases independientes, facilitando su comprensión, mantenimiento y sustentación:

1. main.py:
   Es el punto de entrada de la aplicación. Se encarga de inicializar de forma automática la base de datos SQLite local (creando el archivo 'usuarios.db' y la tabla 'usuarios' si no existen) y arranca la ventana de Login.

2. login.py:
   Contiene la clase 'Login' encargada de la interfaz gráfica y la lógica del inicio de sesión. Valida que las credenciales coincidan con las de la base de datos y redirige al usuario hacia la ventana principal al autenticarse de forma correcta.

3. registro.py:
   Contiene la clase 'Registro' (que se ejecuta sobre una ventana Toplevel). Se encarga de capturar y registrar nuevos usuarios. Valida campos vacíos e impide el registro de nombres de usuario duplicados.

4. pagina_inicial.py:
   Contiene la clase 'PaginaInicial' que dibuja la pantalla principal que ve el usuario después de iniciar sesión. Muestra un saludo personalizado ("Bienvenido, [Nombre Completo]") e inserta/aloja el módulo de la calculadora.

5. calculadora.py:
   Contiene la clase 'Calculadora' que define el teclado numérico, operadores aritméticos básicos y lógica de cálculo. Asimismo, maneja la estructura de datos para el historial de operaciones.


CUMPLIMIENTO DE REQUERIMIENTOS:
--------------------------------
- RF01 (Registro): Implementado en 'registro.py' ingresando Nombre, Usuario y Contraseña, guardándose localmente en la base de datos SQL.
- RF02 (Login): Implementado en 'login.py' verificando usuario y clave.
- RF03 (Página inicial): Implementado en 'pagina_inicial.py' con un mensaje de bienvenida.
- RF04 (Calculadora en página inicial): Implementado al instanciar la clase 'Calculadora' dentro de 'pagina_inicial.py'.
- RF05 (Operaciones básicas): Suma (+), Resta (-), Multiplicación (*) y División (/).
- RF06 (Validaciones):
  * Valida que no se ingresen campos vacíos en el registro, login u operaciones.
  * Valida datos e ingresos matemáticos incorrectos (ej. operadores mal puestos).
  * Valida explícitamente y evita la división por cero lanzando una advertencia en pantalla sin interrumpir la ejecución del programa.
- RF07 (Mensajes): Uso de cuadros de diálogo estándar (messagebox) para notificar errores, advertencias y accesos permitidos/denegados.
- RF08 (Estructura de datos): Se utiliza una lista de Python (tipo list) en 'self.historial' dentro de la clase 'Calculadora' para almacenar dinámicamente cada una de las operaciones realizadas con éxito. Este historial se dibuja en pantalla usando un widget Listbox y se puede borrar mediante el botón de vaciar historial.


INSTRUCCIONES PARA EJECUTAR:
-----------------------------
1. Asegúrese de tener Python instalado en su sistema.
2. Abra una consola/terminal y navegue hasta el directorio 'proyecto_nivelacion'.
3. Ejecute el siguiente comando para iniciar el programa:
   python main.py
