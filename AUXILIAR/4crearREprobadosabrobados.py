import os
def crearAchivo():
    #voy crear carpeta Data
    if not os.path.exists('data'):
        os.makedirs('data')
        print('Carpeta "data" creada.')
    if os.path.exists('data/alumnos.txt'):
        print('El archivo "alumnos.txt" \nya existe en la carpeta "data".')
    else:
        print('El archivo "alumnos.txt" no existe\n en la carpeta "data". Se creará.')
        archive = open('data/alumnos.txt','w' )
        archive.close()
def leerDara():
    print('=====DATOS DE ESTUDIANTE Y  3 NOTAS=========')
    nombre = input("Nombre:")
    apellido = input("Apellido:")
    nota1 = int(input("Nota1:"))
    nota2 = int(input("Nota2:"))
    nota3 = int(input("Nota3:"))
    return nombre,apellido,nota1, nota2, nota3   
def guardarRegistros(n,a,n1,n2,n3):
    archivo=open('data/alumnos.txt','a')
    datos=f'{n},{a},{n1},{n2},{n3}\n'
    archivo.write(datos)
    print('Registro guardado con éxito\n')
    print(f"Datos de :{n} {a} en 'alumnos.txt'.")
    print('____________________________________\n')
def mostrarREgistro():
    if os.path.exists('data/alumnos.txt'):
        with open('data/alumnos.txt','r') as archivo:
            print('=========MOSRTAR  DATOS DE ALUMNOS=========')
            for linea in archivo:
                print(linea.strip())
def ClasificacionNotas(nota):
    if nota >=51:
        return 'Aprobado'
    else:
        return 'Reprobado'
def guardarListaAprobadosRebropbados(n,a,n1,n2,n3):
    if n1>=51:
        with open('data/aprobados.txt','a') as fileAprobado:
            fileAprobado.write(f'{n},{a},{n1}\n')
            print(f"Nota1 {n1} de {n} {a} guardada en 'Aprobados.txt'.")
    else:
        with open('data/reprobados.txt','a') as fileRepbrado:
            fileRepbrado.write(f"Nota1 {n},{a},{n1}\n ")
            print(f"Nota1 {n1} de {n} {a} guardada en 'Reprobados.txt'.")
    if n2>=51:
        with open('data/aprobados.txt','a') as fileAprobado:
            fileAprobado.write(f'{n},{a},{n2}\n')
            print(f"Nota2 {n2} de {n} {a} guardada en 'Aprobados.txt'.")
    else:
        with open('data/reprobados.txt','a') as fileRepbrado:
            fileRepbrado.write(f'{n},{a},{n2}\n')
            print(f"Nota2 {n2} de {n} {a} guardada en 'Reprobados.txt'.")
    if n3>=51:
        with open('data/aprobados.txt','a') as fileAprobado:
            fileAprobado.write(f'{n},{a},{n3}\n')
            print(f"Nota3 {n3} de {n} {a} guardada en 'Aprobados.txt'.")
    else:
        with open('data/reprobados.txt','a') as fileRepbrado:
            fileRepbrado.write(f'{n},{a},{n3}\n')
            print(f"Nota3 {n3} de {n} {a} guardada en 'Reprobados.txt'.")

def mostrarListaAprobadoReprobado():
    print('==========LISTA DE APROBADOS===============')
    if os.path.exists('data/aprobados.txt'):
        with open('data/aprobados.txt','r') as archivo:
            if archivo:
                for linea in archivo:
                    print(linea.strip())
            else:
                print('No hay estuidanmtes Aprobados.')
    else:
        print("No se ha generado el archivo de aprobados.")
    print('==========LISTA DE REPROBADOS===============')
    if os.path.exists('data/reprobados.txt'):
        with open('data/reprobados.txt','r') as archivo:
            if archivo:
                for linea in archivo:
                    print(linea.strip())
            else:
                print('No hay estudiantes Reprobados.')
    else:
        print("No se ha generado el archivo de reprobados.")
#_______________Function Main_____________
nombre,apellido,nota1,nota2,nota3 = leerDara()
crearAchivo()
guardarRegistros(nombre,apellido,nota1,nota2,nota3)
mostrarREgistro()
guardarListaAprobadosRebropbados(nombre,apellido,nota1,nota2,nota3)
mostrarListaAprobadoReprobado()
