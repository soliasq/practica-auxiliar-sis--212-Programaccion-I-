import tkinter as tk
from tkinter import messagebox

usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

class Estudiante:
    def __init__(self, ru, apellidos, nombres, primerParcial, segundoParcial, tercerParcial):
        self.ru = ru
        self.apellidos = apellidos
        self.nombres = nombres
        self.primerParcial = primerParcial
        self.segundoParcial = segundoParcial
        self.tercerParcial = tercerParcial
    
    def calcularSumaNotas(self):
        return self.primerParcial + self.segundoParcial + self.tercerParcial
    
    def calcularPromedioNotas(self):
        suma = self.calcularSumaNotas()
        return suma / 3

def verificarSesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if usuario in usuarios and usuarios[usuario] == contrasena:
        login_frame.pack_forget()
        mostrarFormulario()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def mostrarLogin():
    global login_frame, entry_usuario, entry_contrasena
    login_frame = tk.Frame(root)
    login_frame.pack(pady=50)
    
    label_usuario = tk.Label(login_frame, text="Usuario:")
    label_usuario.grid(row=0, column=0, padx=10, pady=10)
    entry_usuario = tk.Entry(login_frame)
    entry_usuario.grid(row=0, column=1, padx=10, pady=10)
    label_contrasena = tk.Label(login_frame, text="Contraseña:")
    label_contrasena.grid(row=1, column=0, padx=10, pady=10)
    entry_contrasena = tk.Entry(login_frame, show="*")
    entry_contrasena.grid(row=1, column=1, padx=10, pady=10)
    btn_login = tk.Button(login_frame, text="Iniciar Sesión", command=verificarSesion)
    btn_login.grid(row=2, column=0, columnspan=2, pady=20)

def mostrarFormulario():
    global formulario_frame, entry_ru, entry_apellidos, entry_nombres, entry_primerParcial, entry_segundoParcial, entry_tercerParcial
    formulario_frame = tk.Frame(root)
    formulario_frame.pack(pady=50)

    label_ru = tk.Label(formulario_frame, text="Registro Universitario:")
    label_ru.grid(row=0, column=0, padx=10, pady=10)
    entry_ru = tk.Entry(formulario_frame)
    entry_ru.grid(row=0, column=1, padx=10, pady=10)

    label_apellidos = tk.Label(formulario_frame, text="Apellidos:")
    label_apellidos.grid(row=1, column=0, padx=10, pady=10)
    entry_apellidos = tk.Entry(formulario_frame)
    entry_apellidos.grid(row=1, column=1, padx=10, pady=10)

    label_nombres = tk.Label(formulario_frame, text="Nombres:")
    label_nombres.grid(row=2, column=0, padx=10, pady=10)
    entry_nombres = tk.Entry(formulario_frame)
    entry_nombres.grid(row=2, column=1, padx=10, pady=10)

    label_primerParcial = tk.Label(formulario_frame, text="Nota Primer Parcial:")
    label_primerParcial.grid(row=3, column=0, padx=10, pady=10)
    entry_primerParcial = tk.Entry(formulario_frame)
    entry_primerParcial.grid(row=3, column=1, padx=10, pady=10)

    label_segundoParcial = tk.Label(formulario_frame, text="Nota Segundo Parcial:")
    label_segundoParcial.grid(row=4, column=0, padx=10, pady=10)
    entry_segundoParcial = tk.Entry(formulario_frame)
    entry_segundoParcial.grid(row=4, column=1, padx=10, pady=10)

    label_tercerParcial = tk.Label(formulario_frame, text="Nota Tercer Parcial:")
    label_tercerParcial.grid(row=5, column=0, padx=10, pady=10)
    entry_tercerParcial = tk.Entry(formulario_frame)
    entry_tercerParcial.grid(row=5, column=1, padx=10, pady=10)

    btn_agregar = tk.Button(formulario_frame, text="Agregar Estudiante", command=agregarEstudiante)
    btn_agregar.grid(row=6, column=0, columnspan=2, pady=10)

    btn_modificar = tk.Button(formulario_frame, text="Modificar Estudiante", command=modificarEstudiante)
    btn_modificar.grid(row=7, column=0, columnspan=2, pady=10)

    btn_listar = tk.Button(formulario_frame, text="Listar Estudiantes", command=listarEstudiantes)
    btn_listar.grid(row=8, column=0, columnspan=2, pady=10)

    btn_buscar = tk.Button(formulario_frame, text="Buscar Estudiante", command=buscarEstudiante)
    btn_buscar.grid(row=9, column=0, columnspan=2, pady=10)

    btn_eliminar = tk.Button(formulario_frame, text="Eliminar Estudiante", command=eliminarEstudiante)
    btn_eliminar.grid(row=10, column=0, columnspan=2, pady=10)

def agregarEstudiante():
    ru = entry_ru.get()
    apellidos = entry_apellidos.get()
    nombres = entry_nombres.get()
    
    try:
        primerParcial = int(entry_primerParcial.get())
        segundoParcial = int(entry_segundoParcial.get())
        tercerParcial = int(entry_tercerParcial.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos para las notas.")
        return

    estudiante = Estudiante(ru, apellidos, nombres, primerParcial, segundoParcial, tercerParcial)
    
    suma = estudiante.calcularSumaNotas()
    promedio = estudiante.calcularPromedioNotas()

    messagebox.showinfo("Estudiante Agregado", f"El estudiante ha sido agregado con éxito.\n\nSuma de notas: {suma}\nPromedio: {promedio}")
    
    with open('archivo_estudiantes.txt', 'r') as archivo:
        estudiantes = archivo.readlines()
        for estudiante_archivo in estudiantes:
            if ru in estudiante_archivo:
                messagebox.showerror("Error", "El estudiante ya existe.")
                return
    
    with open('archivo_estudiantes.txt', 'a') as archivo:
        archivo.write(f"{estudiante.ru},{estudiante.apellidos},{estudiante.nombres},{estudiante.primerParcial},{estudiante.segundoParcial},{estudiante.tercerParcial}\n")
    
    messagebox.showinfo("Estudiante Agregado", "El estudiante ha sido agregado con éxito.")

def modificarEstudiante():
    ru = entry_ru.get()
    apellidos = entry_apellidos.get()
    nombres = entry_nombres.get()
    
    try:
        primerParcial = int(entry_primerParcial.get())
        segundoParcial = int(entry_segundoParcial.get())
        tercerParcial = int(entry_tercerParcial.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos para las notas.")
        return

    estudiante = Estudiante(ru, apellidos, nombres, primerParcial, segundoParcial, tercerParcial)

    suma = estudiante.calcularSumaNotas()
    promedio = estudiante.calcularPromedioNotas()

    with open('archivo_estudiantes.txt', 'r') as archivo:
        estudiantes = archivo.readlines()

    with open('archivo_estudiantes.txt', 'w') as archivo:
        for estudiante_archivo in estudiantes:
            if ru in estudiante_archivo:
                archivo.write(f"{estudiante.ru},{estudiante.apellidos},{estudiante.nombres},{estudiante.primerParcial},{estudiante.segundoParcial},{estudiante.tercerParcial}\n")
            else:
                archivo.write(estudiante_archivo)
    
    messagebox.showinfo("Estudiante Modificado", f"El estudiante ha sido modificado con éxito.\n\nSuma de notas: {suma}\nPromedio: {promedio}")

def eliminarEstudiante():
    ru = entry_ru.get()
    
    with open('archivo_estudiantes.txt', 'r') as archivo:
        estudiantes = archivo.readlines()

    encontrado = False
    with open('archivo_estudiantes.txt', 'w') as archivo:
        for estudiante_archivo in estudiantes:
            if ru not in estudiante_archivo:
                archivo.write(estudiante_archivo)
            else:
                encontrado = True
    
    if encontrado:
        messagebox.showinfo("Estudiante Eliminado", "El estudiante ha sido eliminado con éxito.")
    else:
        messagebox.showerror("Error", "No se encontró un estudiante con ese RU.")

def listarEstudiantes():
    with open('archivo_estudiantes.txt', 'r') as archivo:
        estudiantes = archivo.readlines()

    if estudiantes:
        reporte_ventana = tk.Toplevel(root)
        reporte_ventana.title("Reporte de Estudiantes")
        
        texto_reporte = tk.Text(reporte_ventana, height=15, width=50)
        texto_reporte.pack(padx=10, pady=10)
        
        for estudiante_archivo in estudiantes:
            texto_reporte.insert(tk.END, estudiante_archivo)

def buscarEstudiante():
    ru = entry_ru.get()
    
    with open('archivo_estudiantes.txt', 'r') as archivo:
        estudiantes = archivo.readlines()

    encontrado = False
    for estudiante_archivo in estudiantes:
        if ru in estudiante_archivo:
            encontrado = True
            messagebox.showinfo("Estudiante Encontrado", estudiante_archivo)
            break
    
    if not encontrado:
        messagebox.showerror("Error", "No se encontró un estudiante con ese RU.")

root = tk.Tk()
root.title("Sistema de Gestión de Estudiantes")

mostrarLogin()

root.mainloop()
