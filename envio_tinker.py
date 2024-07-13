import tkinter as tk
from tkinter import ttk
from enum import Enum
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os

class TipoEnvio(Enum):
    NACIONAL = 1
    INTERNACIONAL = 2

class Contenido(Enum):
    DOCUMENTO = 1
    MERCANCIA = 2

class PaqueteEnvio:
    def __init__(self, destinatario, remitente, tipo_envio, contenido, peso):
        self.remitente = self.Remitente(remitente)
        self.destinatario = self.Destinatario(destinatario)
        self.tipo_envio = tipo_envio
        self.contenido = contenido
        self.peso = peso

    class Remitente:
        def __init__(self, remitente):
            self.nombres = remitente[0]
            self.apellidos = remitente[1]
            self.documento = remitente[2]
            self.direccion = remitente[3]
            self.telefono = remitente[4]

    class Destinatario:
        def __init__(self, destinatario):
            self.nombres = destinatario[0]
            self.apellidos = destinatario[1]
            self.documento = destinatario[2]
            self.direccion = destinatario[3]
            self.telefono = destinatario[4]

    def CalcularValorEnvio(self):
        costoKilo = 0
        if self.tipo_envio == TipoEnvio.NACIONAL:
            if self.contenido == Contenido.DOCUMENTO:
                if self.peso <= 2:
                    costoKilo = 2000
                else: 
                    costoKilo = 3000
            elif self.contenido == Contenido.MERCANCIA:
                if self.peso <= 2:
                    costoKilo = 5000
                else: 
                    costoKilo = 9000
        elif self.tipo_envio == TipoEnvio.INTERNACIONAL:
            if self.contenido == Contenido.DOCUMENTO:
                if self.peso <= 2:
                    costoKilo = 10000
                else: 
                    costoKilo = 15000
            elif self.contenido == Contenido.MERCANCIA:
                if self.peso <= 2:
                    costoKilo = 12000
                else: 
                    costoKilo = 20000 
        valor_envio = costoKilo * self.peso
        return valor_envio

class FormularioEnvio:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de Envío")

        self.frame_remitente = ttk.LabelFrame(self.root, text="Remitente")
        self.frame_remitente.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.label_nombres = ttk.Label(self.frame_remitente, text="Nombres:")
        self.label_nombres.grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_nombres = ttk.Entry(self.frame_remitente)
        self.entry_nombres.grid(row=0, column=1, padx=5, pady=2)

        self.label_apellidos = ttk.Label(self.frame_remitente, text="Apellidos:")
        self.label_apellidos.grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_apellidos = ttk.Entry(self.frame_remitente)
        self.entry_apellidos.grid(row=1, column=1, padx=5, pady=2)

        self.label_documento = ttk.Label(self.frame_remitente, text="Documento:")
        self.label_documento.grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.entry_documento = ttk.Entry(self.frame_remitente)
        self.entry_documento.grid(row=2, column=1, padx=5, pady=2)

        self.label_direccion = ttk.Label(self.frame_remitente, text="Dirección:")
        self.label_direccion.grid(row=3, column=0, padx=5, pady=2, sticky="e")
        self.entry_direccion = ttk.Entry(self.frame_remitente)
        self.entry_direccion.grid(row=3, column=1, padx=5, pady=2)

        self.label_telefono = ttk.Label(self.frame_remitente, text="Teléfono:")
        self.label_telefono.grid(row=4, column=0, padx=5, pady=2, sticky="e")
        self.entry_telefono = ttk.Entry(self.frame_remitente)
        self.entry_telefono.grid(row=4, column=1, padx=5, pady=2)

        self.frame_destinatario = ttk.LabelFrame(self.root, text="Destinatario")
        self.frame_destinatario.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.label_nombres_dest = ttk.Label(self.frame_destinatario, text="Nombres:")
        self.label_nombres_dest.grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_nombres_dest = ttk.Entry(self.frame_destinatario)
        self.entry_nombres_dest.grid(row=0, column=1, padx=5, pady=2)

        self.label_apellidos_dest = ttk.Label(self.frame_destinatario, text="Apellidos:")
        self.label_apellidos_dest.grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_apellidos_dest = ttk.Entry(self.frame_destinatario)
        self.entry_apellidos_dest.grid(row=1, column=1, padx=5, pady=2)

        self.label_documento_dest = ttk.Label(self.frame_destinatario, text="Documento:")
        self.label_documento_dest.grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.entry_documento_dest = ttk.Entry(self.frame_destinatario)
        self.entry_documento_dest.grid(row=2, column=1, padx=5, pady=2)

        self.label_direccion_dest = ttk.Label(self.frame_destinatario, text="Dirección:")
        self.label_direccion_dest.grid(row=3, column=0, padx=5, pady=2, sticky="e")
        self.entry_direccion_dest = ttk.Entry(self.frame_destinatario)
        self.entry_direccion_dest.grid(row=3, column=1, padx=5, pady=2)

        self.label_telefono_dest = ttk.Label(self.frame_destinatario, text="Teléfono:")
        self.label_telefono_dest.grid(row=4, column=0, padx=5, pady=2, sticky="e")
        self.entry_telefono_dest = ttk.Entry(self.frame_destinatario)
        self.entry_telefono_dest.grid(row=4, column=1, padx=5, pady=2)

        self.frame_paquete = ttk.LabelFrame(self.root, text="Paquete de Envío")
        self.frame_paquete.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.label_tipo_envio = ttk.Label(self.frame_paquete, text="Tipo de Envío:")
        self.label_tipo_envio.grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.combo_tipo_envio = ttk.Combobox(self.frame_paquete, values=["NACIONAL", "INTERNACIONAL"])
        self.combo_tipo_envio.grid(row=0, column=1, padx=5, pady=2)
        self.combo_tipo_envio.current(0)

        self.label_contenido = ttk.Label(self.frame_paquete, text="Contenido:")
        self.label_contenido.grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.combo_contenido = ttk.Combobox(self.frame_paquete, values=["DOCUMENTO", "MERCANCIA"])
        self.combo_contenido.grid(row=1, column=1, padx=5, pady=2)
        self.combo_contenido.current(0)

        self.label_peso = ttk.Label(self.frame_paquete, text="Peso (kg):")
        self.label_peso.grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.entry_peso = ttk.Entry(self.frame_paquete)
        self.entry_peso.grid(row=2, column=1, padx=5, pady=2)

        self.frame_resultado = ttk.Frame(self.root)
        self.frame_resultado.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        self.label_resultado = ttk.Label(self.frame_resultado, text="")
        self.label_resultado.grid(row=0, column=0, padx=5, pady=2)

        self.frame_botones = ttk.Frame(self.root)
        self.frame_botones.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.button_enviar = ttk.Button(self.frame_botones, text="Enviar", command=self.enviar_formulario)
        self.button_enviar.grid(row=0, column=0, padx=5, pady=2)
        self.button_limpiar = ttk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_formulario)
        self.button_limpiar.grid(row=0, column=1, padx=5, pady=2)
        self.button_factura = ttk.Button(self.frame_botones, text="Ver Factura", command=self.abrir_factura)
        self.button_factura.grid(row=0, column=2, padx=5, pady=2)

    def enviar_formulario(self):
        remitente = (
            self.entry_nombres.get(),
            self.entry_apellidos.get(),
            self.entry_documento.get(),
            self.entry_direccion.get(),
            self.entry_telefono.get()
        )

        destinatario = (
            self.entry_nombres_dest.get(),
            self.entry_apellidos_dest.get(),
            self.entry_documento_dest.get(),
            self.entry_direccion_dest.get(),
            self.entry_telefono_dest.get()
        )

        tipo_envio = TipoEnvio.NACIONAL if self.combo_tipo_envio.get() == "NACIONAL" else TipoEnvio.INTERNACIONAL
        contenido = Contenido.DOCUMENTO if self.combo_contenido.get() == "DOCUMENTO" else Contenido.MERCANCIA
        peso = float(self.entry_peso.get())

        paquete = PaqueteEnvio(destinatario, remitente, tipo_envio, contenido, peso)
        valor_envio = paquete.CalcularValorEnvio()

        # Mostrar el valor del envío en la etiqueta de resultado
        self.label_resultado.config(text=f"Valor del envío: ${valor_envio:,.2f} COP")

        # Generar factura
        self.generar_factura(valor_envio)

    def generar_factura(self, valor_envio):
        remitente = {
            "Nombres": self.entry_nombres.get(),
            "Apellidos": self.entry_apellidos.get(),
            "Documento": self.entry_documento.get(),
            "Dirección": self.entry_direccion.get(),
            "Teléfono": self.entry_telefono.get()
        }

        destinatario = {
            "Nombres": self.entry_nombres_dest.get(),
            "Apellidos": self.entry_apellidos_dest.get(),
            "Documento": self.entry_documento_dest.get(),
            "Dirección": self.entry_direccion_dest.get(),
            "Teléfono": self.entry_telefono_dest.get()
        }

        tipo_envio = self.combo_tipo_envio.get()
        contenido = self.combo_contenido.get()
        peso = self.entry_peso.get()

        # Crear factura en PDF
        filename = "factura_envio.pdf"
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []

        # Encabezado de la factura
        encabezado = Table([["Factura de Envío"]], colWidths=500, rowHeights=50)
        encabezado.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.lightblue),
                                        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                        ('FONTSIZE', (0, 0), (-1, -1), 20)]))
        elements.append(encabezado)

        # Datos del remitente
        remitente_data = [["Remitente:"]]
        for key, value in remitente.items():
            remitente_data.append([key, value])
        remitente_table = Table(remitente_data, colWidths=[150, 350])
        remitente_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                              ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                              ('FONTSIZE', (0, 0), (-1, -1), 12),
                                              ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                              ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
        elements.append(remitente_table)

        # Datos del destinatario
        destinatario_data = [["Destinatario:"]]
        for key, value in destinatario.items():
            destinatario_data.append([key, value])
        destinatario_table = Table(destinatario_data, colWidths=[150, 350])
        destinatario_table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                                                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                                                 ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                                                 ('FONTSIZE', (0, 0), (-1, -1), 12),
                                                 ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                                 ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
        elements.append(destinatario_table)

        # Otros detalles del envío
        otros_detalles = Table([["Tipo de Envío:", tipo_envio],
                                ["Contenido:", contenido],
                                ["Peso (kg):", peso],
                                ["Valor del Envío:", f"${valor_envio:,.2f} COP"]], colWidths=250)
        otros_detalles.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                                             ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                                             ('FONTSIZE', (0, 0), (-1, -1), 12),
                                             ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                             ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
        elements.append(otros_detalles)

        # Generar el documento PDF
        doc.build(elements)

    def limpiar_formulario(self):
        # Limpiar los campos del formulario
        self.entry_nombres.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_documento.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)

        self.entry_nombres_dest.delete(0, tk.END)
        self.entry_apellidos_dest.delete(0, tk.END)
        self.entry_documento_dest.delete(0, tk.END)
        self.entry_direccion_dest.delete(0, tk.END)
        self.entry_telefono_dest.delete(0, tk.END)

        self.combo_tipo_envio.current(0)
        self.combo_contenido.current(0)
        self.entry_peso.delete(0, tk.END)

    def abrir_factura(self):
        # Abre el archivo PDF de la factura generado
        os.system("factura_envio.pdf")

def main():
    root = tk.Tk()
    formulario = FormularioEnvio(root)
    root.mainloop()

if __name__ == "__main__":
    main()
