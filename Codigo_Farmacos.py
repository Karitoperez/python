from tabulate import tabulate

class Producto:
    def __init__(self, nombre, fabricacion, fecha_caducidad):
        self.nombre = nombre
        self.fabricacion = fabricacion
        self.fecha_caducidad = fecha_caducidad

    def mostrar_informacion(self):
        table = [
            ["Nombre del producto", self.nombre],
            ["Fecha de fabricación", self.fabricacion],
            ["Fecha de caducidad", self.fecha_caducidad]
        ]
        print(tabulate(table, headers=["Atributo", "Valor"], tablefmt="grid"))

class Medicamento(Producto):
    def __init__(self, nombre, fabricacion, fecha_caducidad, posologia):
        super().__init__(nombre, fabricacion, fecha_caducidad)
        self.posologia = posologia

    def mostrar_informacion(self):
        super().mostrar_informacion()
        if self.posologia:
            posologia_info = [
                ["Dosis", self.posologia.dosis],
                ["Periodo", self.posologia.periodo],
                ["Recomendaciones", self.posologia.recomendaciones]
            ]
            print(tabulate(posologia_info, headers=["Atributo", "Valor"], tablefmt="grid"))

class Posologia:
    def __init__(self, dosis, periodo, recomendaciones):
        self.dosis = dosis
        self.periodo = periodo
        self.recomendaciones = recomendaciones

    def agregar_medicamento():
        nombre = input("Ingrese el nombre del medicamento: ")
        fabricacion = input("Ingrese la fecha de fabricación (formato: dd/mm/aaaa): ")
        fecha_caducidad = input("Ingrese la fecha de caducidad (formato: dd/mm/aaaa): ")
        dosis = int(input("Ingrese la dosis del medicamento en mg: "))
        periodo = input("Ingrese el periodo de administración: ")
        recomendaciones = input("Ingrese las recomendaciones: ")

        posologia = Posologia(dosis, periodo, recomendaciones)
        medicamento = Medicamento(nombre, fabricacion, fecha_caducidad, posologia)

        return medicamento

def main():
    medicamentos = []

    while True:
        print("\n----- Menú de Medicamentos -----")
        print("1. Agregar medicamento")
        print("2. Ver información de medicamentos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if len(medicamentos) < 5:
                medicamento_nuevo = agregar_medicamento()
                medicamentos.append(medicamento_nuevo)
                print("Medicamento agregado correctamente.")
            else:
                print("Ya ha alcanzado el límite de medicamentos (5).")
        
        elif opcion == "2":
            if len(medicamentos) > 0:
                for i, medicamento in enumerate(medicamentos, 1):
                    print(f"\nMedicamento {i}: {medicamento.nombre}")
                seleccion = int(input("Seleccione el número de medicamento para ver su información: "))
                if 1 <= seleccion <= len(medicamentos):
                    medicamentos[seleccion - 1].mostrar_informacion()
                else:
                    print("Selección inválida.")
            else:
                print("No hay medicamentos guardados.")
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()