print('\n')
print('Ejercicio 3: Numeros primos')
print('\n')
print('Ingrese un numero entero positivo:')
num=int(input())
print('\n')

contador=0

for i in range(2,num):
    if num % i ==0:
        contador +=1

if contador > 0:
    print("el "+str(num)+" no es primo")
else: 
    print("el "+str(num)+" es primo")