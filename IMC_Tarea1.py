
print('Bienvenido al menu de indice de masa muscular!\n')

a = '1'
while(a == '1'):

    print('Ingrese su altura(m):')
    altura=float(input())
    print('\n')

    print('Ingrese su peso (kg):')
    peso=float(input())
    print('\n')

    imc= peso/altura**2

    if(imc>=18.5 and imc <=24.9):

        print('su IMC es: ',round(imc,2) ,'(normal)\n')
        

    elif(imc<18.5):

     print('su IMC es bajo: ',round(imc,2) ,'(bajo)\n')

    else: print('su IMC es: ',round(imc,2) ,'(alto)\n')

    print('Desea calcular su IMC de nuevo?, introduzca el numero 1 si lo desea, 2 para salir')
    a=input()
