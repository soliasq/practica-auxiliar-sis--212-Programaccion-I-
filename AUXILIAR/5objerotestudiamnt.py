class Estudiante:
    def __init__(self, ru, apellidos, nombres, primerParcial, segundoParcial, tercerParcial):
        self.ru = ru
        self.apellidos = apellidos
        self.nombres = nombres
        self.primerParcial = primerParcial
        self.segundoParcial = segundoParcial
        self.tercerParcial = tercerParcial
    
    def leer(self):
        self.ru = input("Ingrese el registro universitario: ")
        self.apellidos = input("Ingrese los apellidos: ")
        self.nombres = input("Ingrese los nombres: ")
        self.primerParcial = int(input("Ingrese la nota del primer parcial: "))
        self.segundoParcial = int(input("Ingrese la nota del segundo parcial: "))
        self.tercerParcial = int(input("Ingrese la nota del tercer parcial: "))
    
    def mostrar(self):
        print(f"Registro Universitario: {self.ru}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Nombres: {self.nombres}")
        print(f"Primer Parcial: {self.primerParcial}")
        print(f"Segundo Parcial: {self.segundoParcial}")
        print(f"Tercer Parcial: {self.tercerParcial}")
    
    def notaTotal(self):
        total = self.primerParcial + self.segundoParcial + self.tercerParcial
        print(f"La suma total de las notas es: {total}")
    
    def promedio(self):
        promedio = (self.primerParcial + self.segundoParcial + self.tercerParcial) / 3
        print(f"El promedio de las tres notas es: {promedio}")


estudiante = Estudiante("", "", "", 0, 0, 0)
estudiante.leer()
estudiante.mostrar()
estudiante.notaTotal()
estudiante.promedio()

