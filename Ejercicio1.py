'''Escribir un programa que indique cuál es el mayor de dos
números enteros.'''
numero1=int(input("ingrese primer numero:"))
numero2=int(input("ingrese segundo numero:"))
if numero1>numero2:
    print("el numero ",numero1," Es mayor")
    print(f'el numero {numero1} es mayor {numero2}')
else:
    print("el numero ",numero2," es mayor")    