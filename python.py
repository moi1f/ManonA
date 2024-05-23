import tkinter as tk
from tkinter import messagebox
import pickle

class Libro:
    def __init__(self, titulo, autor, genero, anio, paginas, idiomas, calificacion, resumen, estado, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio = anio
        self.paginas = paginas
        self.idiomas = idiomas
        self.calificacion = calificacion
        self.resumen = resumen
        self.estado = estado
        self.cantidad = cantidad

class LibreriaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Librería App")
        self.libros = []

        # Intenta cargar los libros desde el archivo
        try:
            with open("libros.dat", "rb") as file:
                self.libros = pickle.load(file)
        except FileNotFoundError:
            pass

        self.create_widgets()

    def create_widgets(self):
        # Crear variables para los campos de entrada
        self.titulo_var = tk.StringVar()
        self.autor_var = tk.StringVar()
        self.genero_var = tk.StringVar()
        self.anio_var = tk.StringVar()
        self.paginas_var = tk.StringVar()
        self.idiomas_var = tk.StringVar()
        self.calificacion_var = tk.StringVar()
        self.resumen_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()

        # Crear etiquetas y campos de entrada
        tk.Label(self.master, text="Título:").grid(row=0, column=0)
        self.titulo_entry = tk.Entry(self.master, textvariable=self.titulo_var)
        self.titulo_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Autor:").grid(row=1, column=0)
        self.autor_entry = tk.Entry(self.master, textvariable=self.autor_var)
        self.autor_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Género:").grid(row=2, column=0)
        self.genero_entry = tk.Entry(self.master, textvariable=self.genero_var)
        self.genero_entry.grid(row=2, column=1)

        tk.Label(self.master, text="Año de Publicación:").grid(row=3, column=0)
        self.anio_entry = tk.Entry(self.master, textvariable=self.anio_var)
        self.anio_entry.grid(row=3, column=1)

        tk.Label(self.master, text="Número de Páginas:").grid(row=4, column=0)
        self.paginas_entry = tk.Entry(self.master, textvariable=self.paginas_var)
        self.paginas_entry.grid(row=4, column=1)

        tk.Label(self.master, text="Idiomas:").grid(row=5, column=0)
        self.idiomas_entry = tk.Entry(self.master, textvariable=self.idiomas_var)
        self.idiomas_entry.grid(row=5, column=1)

        tk.Label(self.master, text="Calificación:").grid(row=6, column=0)
        self.calificacion_entry = tk.Entry(self.master, textvariable=self.calificacion_var)
        self.calificacion_entry.grid(row=6, column=1)

        tk.Label(self.master, text="Resumen:").grid(row=7, column=0)
        self.resumen_entry = tk.Entry(self.master, textvariable=self.resumen_var)
        self.resumen_entry.grid(row=7, column=1)

        tk.Label(self.master, text="Estado:").grid(row=8, column=0)
        self.estado_entry = tk.Entry(self.master, textvariable=self.estado_var)
        self.estado_entry.grid(row=8, column=1)

        tk.Label(self.master, text="Cantidad:").grid(row=9, column=0)
        self.cantidad_entry = tk.Entry(self.master, textvariable=self.cantidad_var)
        self.cantidad_entry.grid(row=9, column=1)

        # Botones
        self.agregar_btn = tk.Button(self.master, text="Agregar Libro", command=self.agregar_libro)
        self.agregar_btn.grid(row=10, column=0)

        self.buscar_btn = tk.Button(self.master, text="Buscar Libro", command=self.buscar_libro)
        self.buscar_btn.grid(row=10, column=1)

        self.mostrar_btn = tk.Button(self.master, text="Mostrar Libros", command=self.mostrar_libros)
        self.mostrar_btn.grid(row=10, column=2)

        self.prestar_btn = tk.Button(self.master, text="Prestar Libro", command=self.prestar_libro)
        self.prestar_btn.grid(row=10, column=3)

    def agregar_libro(self):
        titulo = self.titulo_var.get()
        autor = self.autor_var.get()
        genero = self.genero_var.get()
        anio = self.anio_var.get()
        paginas = self.paginas_var.get()
        idiomas = self.idiomas_var.get()
        calificacion = self.calificacion_var.get()
        resumen = self.resumen_var.get()
        estado = self.estado_var.get()
        cantidad = self.cantidad_var.get()

        libro = Libro(titulo, autor, genero, anio, paginas, idiomas, calificacion, resumen, estado, cantidad)
        self.libros.append(libro)
        self.guardar_libros()
        messagebox.showinfo("Éxito", "Libro agregado correctamente")

        # Limpiar los campos de entrada
        self.limpiar_campos()

    def buscar_libro(self):
        # Obtener el título del libro a buscar
        titulo_buscar = self.titulo_var.get()

        # Buscar el libro en la lista de libros
        resultados = []
        for libro in self.libros:
            if libro.titulo.lower() == titulo_buscar.lower():
                resultados.append(libro)

        # Mostrar los resultados en un cuadro de diálogo
        if resultados:
            mensaje = ""
            for libro in resultados:
                mensaje += f"Título: {libro.titulo}\nAutor: {libro.autor}\n\n"
            messagebox.showinfo("Resultados de Búsqueda", mensaje)
        else:
            messagebox.showinfo("Resultados de Búsqueda", "Libro no encontrado")

    def mostrar_libros(self):
        # Mostrar todos los libros en un cuadro de diálogo
        mensaje = ""
        for libro in self.libros:
            mensaje += f"Título: {libro.titulo}\nAutor: {libro.autor}\n\n"
        messagebox.showinfo("Todos los Libros", mensaje)

    def prestar_libro(self):
        # Implementar la lógica para prestar un libro
        pass

    def limpiar_campos(self):
        self.titulo_var.set("")
        self.autor_var.set("")
        self.genero_var.set("")
        self.anio
