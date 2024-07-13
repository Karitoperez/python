import tkinter as tk
from tkinter import messagebox, ttk
from tabulate import tabulate

class Tienda: 
    def __init__(self, nombre_tienda, administrador, identificador):
        self.nombre_tienda = nombre_tienda
        self.administrador = administrador
        self.identificador = identificador
        self.computadores = []  

    def mostrar_informacion(self, filtro_marca=None): 
        if filtro_marca:
            computadores_filtrados = [pc for pc in self.computadores if pc.computador.marca.lower() == filtro_marca.lower()]
            if not computadores_filtrados:
                messagebox.showinfo("Info", "No hay computadores de la marca especificada.")
                return
            info_text = ""
            for pc in computadores_filtrados:
                info_text += pc.obtener_info() + "\n\n"
            messagebox.showinfo(f"Computadores {filtro_marca}", info_text)
        else:
            messagebox.showinfo("Info", "No se ha especificado una marca para filtrar.")

    def agregar_computador(self, nombre_tienda, administrador, identificador, marca, memoria, caracteristicas, sistema, precio, modelo):
        if len(self.computadores) < 10:
            computador_nuevo = Computador(marca, memoria, caracteristicas, sistema, precio, modelo)
            pc = PC(nombre_tienda, administrador, identificador, computador_nuevo)
            self.computadores.append(pc)
            messagebox.showinfo("Info", "Nuevo computador agregado correctamente.")
        else:
            messagebox.showinfo("Info", "Ya ha alcanzado el límite de computadores (10).")

    def obtener_marcas(self):
        return list(set([pc.computador.marca for pc in self.computadores]))

    def obtener_computadores_por_marca(self, marca):  
        return [pc for pc in self.computadores if pc.computador.marca.lower() == marca.lower()]

class PC:
    def __init__(self, nombre_tienda, administrador, identificador, computador):
        self.nombre_tienda = nombre_tienda
        self.administrador = administrador
        self.identificador = identificador
        self.computador = computador

    def obtener_info(self):
        return f"Tienda: {self.nombre_tienda}\nAdministrador: {self.administrador}\nIdentificador de la tienda: {self.identificador}\nMarca: {self.computador.marca}\nCantidad de memoria: {self.computador.cantidad_memoria}\nCaracterísticas del procesador: {self.computador.caracteristicas_procesador}\nSistema operativo: {self.computador.sistema}\nPrecio del PC: {self.computador.precio}\nModelo: {self.computador.modelo}"

class Computador:
    def __init__(self, marca, cantidad_memoria, caracteristicas_procesador, sistema, precio, modelo):
        self.marca = marca
        self.cantidad_memoria = cantidad_memoria
        self.caracteristicas_procesador = caracteristicas_procesador
        self.sistema = sistema
        self.precio = precio
        self.modelo = modelo

def agregar_pc(tienda):
    # Crear una ventana Tkinter
    window = tk.Tk()
    window.title("Agregar Computador")

    # Etiqueta y entrada para Nombre de la tienda
    tk.Label(window, text="Tienda:").grid(row=0, column=0)
    tienda_entry = tk.Entry(window)
    tienda_entry.grid(row=0, column=1)

    # Etiqueta y entrada para Administrador
    tk.Label(window, text="Administrador:").grid(row=1, column=0)
    administrador_entry = tk.Entry(window)
    administrador_entry.grid(row=1, column=1)

    # Etiqueta y entrada para Identificador
    tk.Label(window, text="Identificador:").grid(row=2, column=0)
    identificador_entry = tk.Entry(window)
    identificador_entry.grid(row=2, column=1)

    # Etiqueta y lista desplegable para Marca
    tk.Label(window, text="Marca:").grid(row=3, column=0)
    marca_combobox = ttk.Combobox(window, values=["Mac", "Asus", "HP"])
    marca_combobox.grid(row=3, column=1)

    # Etiqueta y entrada para Memoria
    tk.Label(window, text="Memoria:").grid(row=4, column=0)
    memoria_entry = tk.Entry(window)
    memoria_entry.grid(row=4, column=1)

    # Etiqueta y entrada para Características
    tk.Label(window, text="Características:").grid(row=5, column=0)
    caracteristicas_entry = tk.Entry(window)
    caracteristicas_entry.grid(row=5, column=1)

    # Etiqueta y entrada para Sistema
    tk.Label(window, text="Sistema:").grid(row=6, column=0)
    sistema_entry = tk.Entry(window)
    sistema_entry.grid(row=6, column=1)

    # Etiqueta y entrada para Precio
    tk.Label(window, text="Precio:").grid(row=7, column=0)
    precio_entry = tk.Entry(window)
    precio_entry.grid(row=7, column=1)

    # Etiqueta y entrada para Modelo
    tk.Label(window, text="Modelo:").grid(row=8, column=0)
    modelo_entry = tk.Entry(window)
    modelo_entry.grid(row=8, column=1)

    # Función que se llama al hacer clic en el botón "Agregar"
    def agregar_click():
        nombre_tienda = tienda_entry.get()
        administrador = administrador_entry.get()
        identificador = identificador_entry.get()
        marca = marca_combobox.get()
        memoria = memoria_entry.get()
        caracteristicas = caracteristicas_entry.get()
        sistema = sistema_entry.get()
        precio = precio_entry.get()
        modelo = modelo_entry.get()

        tienda.agregar_computador(nombre_tienda, administrador, identificador, marca, memoria, caracteristicas, sistema, precio, modelo)
        window.destroy()

    # Botón para agregar el PC
    tk.Button(window, text="Agregar", command=agregar_click).grid(row=9, columnspan=2)

    window.mainloop()

def mostrar_datos_guardados(tienda):
    # Crear una ventana Tkinter
    window = tk.Tk()
    window.title("Buscar Computadores")

    def mostrar_computadores():
        marca_seleccionada = marca_combobox.get()
        computadores_marca = tienda.obtener_computadores_por_marca(marca_seleccionada)
        if not computadores_marca:
            messagebox.showinfo("Info", f"No hay computadores de la marca {marca_seleccionada}.")
            return

        info_text = ""
        for pc in computadores_marca:
            info_text += pc.obtener_info() + "\n\n"
        messagebox.showinfo(f"Computadores {marca_seleccionada}", info_text)

    # Etiqueta para Marca
    tk.Label(window, text="Seleccione la marca:").grid(row=0, column=0)
    # Combobox para Marca
    marca_combobox = ttk.Combobox(window, values=["Mac", "Asus", "HP"])
    marca_combobox.grid(row=0, column=1)

    # Botón para mostrar los computadores
    tk.Button(window, text="Mostrar Computadores", command=mostrar_computadores).grid(row=1, columnspan=2)

    window.mainloop()

# Crear una tienda de ejemplo
tienda_ejemplo = Tienda("Mi Tienda", "Administrador", "1234")

# Crear una ventana Tkinter para la primera vista
main_window = tk.Tk()
main_window.title("Gestión de Tienda")

# Botón para agregar un PC
tk.Button(main_window, text="Agregar Computador", command=lambda: agregar_pc(tienda_ejemplo)).pack()

# Botón para mostrar los datos guardados
tk.Button(main_window, text="Buscar Computadores", command=lambda: mostrar_datos_guardados(tienda_ejemplo)).pack()

# Botón para terminar el programa
tk.Button(main_window, text="Terminar", command=main_window.destroy).pack()

main_window.mainloop()
