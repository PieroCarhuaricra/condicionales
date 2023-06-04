'''Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla si es mayor de edad o no.'''

edad=int(input("ingrese su edad:"))
if edad<=0 or edad>=111:
    print(f'Error')
elif edad>=18 and edad<=110:
    print("mayor")
elif edad>0 and edad<17:
    print(f'usted en menor de edad')
