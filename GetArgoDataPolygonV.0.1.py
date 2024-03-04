import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import filedialog
import json
import pandas as pd
from argovisHelpers import helpers as avh

# Variables para almacenar las fechas seleccionadas
date_start = None
date_end = None
norte = None
sur = None
este = None
oeste = None
date_start = None
date_end = None
API_KEY= None

# Función para procesar el formulario
def procesar_formulario():
    # Obtener los valores ingresados por el usuario
    API_KEY = codigo_entry.get()
    norte = int(norte_entry.get())
    sur = int(sur_entry.get())
    este = int(este_entry.get())
    oeste = int(oeste_entry.get())

    polygon = [[oeste,norte],[este,norte],[este,sur],[oeste,sur],[oeste,norte]]
    params = {
            'startDate': str(date_start) + 'T00:00:00Z',
            'endDate':  str(date_end) + 'T23:59:59Z',
            'source': 'argo_core',
            'polygon': polygon,
            'data': 'all'
        }

    d = avh.query('argo', options=params, apikey=API_KEY, apiroot= 'https://argovis-api.colorado.edu/')

    data = open(selected_folder + '/data_N_'+ str(norte) + '_S_' + str(sur) + '_E_' + str(este) + '_w_' + str(oeste) + '_' + str(date_start) + '_' + str(date_end) +'.json', 'w')
    data.write(json.dumps(d))
    data.close()

    # Aquí puedes realizar las acciones necesarias con los valores ingresados
    # Por ejemplo, imprimirlos en la consola
    print("Código de usuario:", API_KEY)
    print("Coordenadas (Norte, Sur, Este, Oeste):", norte, sur, este, oeste)
    print("Fecha de inicio:", date_start)
    print("Fecha de fin:", date_end)

# Función para abrir el calendario y seleccionar la fecha de inicio
def seleccionar_fecha_inicio():
    def seleccionar():
        # Acceder a la fecha seleccionada en el calendario
        global date_start
        date_start = cal.selection_get()
        fecha_inicio_label.config(text=f"Fecha de inicio seleccionada: {date_start}")
        top.destroy()

    top = tk.Toplevel(ventana)
    cal = Calendar(top, selectmode="day")
    cal.pack(pady=20)
    boton_seleccionar = ttk.Button(top, text="Seleccionar", command=seleccionar)
    boton_seleccionar.pack()

# Función para abrir el calendario y seleccionar la fecha de fin
def seleccionar_fecha_fin():
    def seleccionar():
        # Acceder a la fecha seleccionada en el calendario
        global date_end
        date_end = cal.selection_get()
        fecha_fin_label.config(text=f"Fecha de fin seleccionada: {date_end}")
        top.destroy()

    top = tk.Toplevel(ventana)
    cal = Calendar(top, selectmode="day")
    cal.pack(pady=20)
    boton_seleccionar = ttk.Button(top, text="Seleccionar", command=seleccionar)
    boton_seleccionar.pack()
    print(type(date_end))

# Función para seleccionar la carpeta de destino
def seleccionar_carpeta():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    carpeta_label.config(text=f"Carpeta seleccionada: {selected_folder}")




# Crear la ventana principal
ventana = tk.Tk()
ventana.title("CEO - Descargar Data Argo Floats - Área personalizada")
ventana.geometry("600x500")

# Inmovilizar el tamaño de la ventana
ventana.resizable(False, False)

# Etiqueta y campo para el código de usuario
codigo_label = tk.Label(ventana, text="Código de Usuario:")
codigo_label.pack()

codigo_entry = tk.Entry(ventana)
codigo_entry.pack()

# Etiquetas y campos para las coordenadas
coordenadas_label = tk.Label(ventana, text="Coordenadas:")
coordenadas_label.pack()

norte_label = tk.Label(ventana, text="Norte:")
norte_label.pack()

norte_entry = tk.Entry(ventana)
norte_entry.pack()

sur_label = tk.Label(ventana, text="Sur:")
sur_label.pack()

sur_entry = tk.Entry(ventana)
sur_entry.pack()

este_label = tk.Label(ventana, text="Este:")
este_label.pack()

este_entry = tk.Entry(ventana)
este_entry.pack()

oeste_label = tk.Label(ventana, text="Oeste:")
oeste_label.pack()

oeste_entry = tk.Entry(ventana)
oeste_entry.pack()

# Etiqueta y botón para seleccionar la fecha de inicio
fecha_inicio_label = tk.Label(ventana, text="Fecha de inicio seleccionada:")
fecha_inicio_label.pack(pady=10)

fecha_inicio_boton = tk.Button(ventana, text="Seleccionar Fecha de Inicio", command=seleccionar_fecha_inicio)
fecha_inicio_boton.pack()

# Etiqueta y botón para seleccionar la fecha de fin
fecha_fin_label = tk.Label(ventana, text="Fecha de fin seleccionada:")
fecha_fin_label.pack(pady=10)

fecha_fin_boton = tk.Button(ventana, text="Seleccionar Fecha de Fin", command=seleccionar_fecha_fin)
fecha_fin_boton.pack()

# Etiqueta y botón para seleccionar la carpeta de destino
carpeta_label = tk.Label(ventana, text="Carpeta seleccionada:")
carpeta_label.pack(pady=10)

carpeta_boton = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta)
carpeta_boton.pack()

# Botón para procesar el formulario
procesar_boton = tk.Button(ventana, text="Procesar", command=procesar_formulario)
procesar_boton.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()


