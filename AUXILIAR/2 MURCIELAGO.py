def convertirClaveMurcielago(cadenas):
    conversion = {
        'M': '0', 'U': '1', 'R': '2', 'C': '3', 'I': '4',
        'E': '5', 'L': '6', 'A': '7', 'G': '8', 'O': '9'
    }
    resultados = []
    for cadena in cadenas:
        resultado = ''
        for letra in cadena:
            if letra in conversion:
                resultado += conversion[letra]
            else:
                resultado += letra
        resultados.append(resultado)
    return resultados

n = int(input("Ingrese el número de palabras: "))
cadenas = []

print('___________Ingrese Solo PALABRAS Mayúsculas___________')
for i in range(1, n + 1):
    palabra = input(f'{i}= ').strip()
    cadenas.append(palabra)

resultados = convertirClaveMurcielago(cadenas)

print('___________Mostrando Resultados___________')
for resultado in resultados:
    print(resultado)
