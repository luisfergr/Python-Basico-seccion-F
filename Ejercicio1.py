print('\n')
print('Ejercicio 1: Triangulo Rectangulo')
print('\n')
print('Ingrese un numero entero positivo:')
num=int(input())
print('\n')

for i in range(1,num+1):
    for j in range(i):
        print("*", end="")
    print()
    
