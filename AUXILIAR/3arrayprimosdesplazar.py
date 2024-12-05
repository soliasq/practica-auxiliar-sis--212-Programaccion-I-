def leerTamanho():
    n=int(input('Ingrese tamanho='))
    return n

def llenarVector(n):
    V=[0]*n
    for i in range(n):
        V[i]=int(input(f'{[i]}:'))
    return V
def mostrarVector(n,V):
    print('\n+_______Elementos del Vector_______')
    print('[ ',end='')
    for i in range(n):
    
        print(V[i],end=' ,')    
    print(']')
def veriPrimo(numero):
    
    if numero < 2:
        return False
    c=0
    for i in range(1, numero+1):

        if numero % i == 0:

            c=c+1
    if c==2:
        return True
    else:
        return False
def ordenarPrimos(n, V):
    primo=[]
    noPrimo=[]
    for i  in range(n):
        if veriPrimo(V[i])==True:
            primo.append(V[i])
        else:
            noPrimo.append(V[i])
    Arrayfina= primo+noPrimo
    return Arrayfina 
n=leerTamanho()
vector=llenarVector(n)
mostrarVector(n,vector)
vectorOrdenado =ordenarPrimos(n, vector)
mostrarVector(n,vectorOrdenado)



