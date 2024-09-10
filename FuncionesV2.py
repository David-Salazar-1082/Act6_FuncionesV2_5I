print("Mas sobre funciones")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def resta_ab(a1,b1):
    r=a1-b1
    return r

def multi_ab(a2,b2):
    m=a2*b2
    return m

def div_ab(a3,b3):
    d=a3/b3
    return d
#Llamadas a funciones
print("Calculando suma")
n1=int(input("Ingresa el primer Numero "))
n2=int(input("Ingresa el segundo Numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es {suma}")

print("Calculando resta")
n1=int(input("Ingresa el primer Numero "))
n2=int(input("Ingresa el segundo Numero "))
resta=resta_ab(n1,n2)
print(f"La resta de {n1} - {n2} es {resta}")

print("Calculando multiplicacion")
n1=int(input("Ingresa el primer Numero "))
n2=int(input("Ingresa el segundo Numero "))
multi=multi_ab(n1,n2)
print(f"La multiplicacion de {n1} * {n2} es {multi}")

print("Calculando division")
n1=int(input("Ingresa el primer Numero "))
n2=int(input("Ingresa el segundo Numero "))
div=div_ab(n1,n2)
print(f"La suma de {n1} / {n2} es {div}")