def saludos(nombre, edad):
    print(f'Hola {nombre} y tu edad es {edad}')

saludos('Ruben', 21)

# def saludos(datos):
#     print(f'Hola, tus datos son ')

# saludos('Ruben', 21)

def multiplicador(num1,num2):
    res = num1*num2
    return res

print(multiplicador(3,2))

# Ejercicio 1
# Crea una funcion que te pase un numero indefinido de parámetros y te devuelva el resultado de multiplicarlos
def multiplicar(*num):
    res = 1
    for n in num:
        res *= n
    return res
print(multiplicar(1,5,2))