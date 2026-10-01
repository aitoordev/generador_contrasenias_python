import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
simbolos = ["@" , "$" , "#" , "?"]
contraseña =""

print("#### GENERADOR DE CONTRASEÑAS ####")
print("------------------------------------")
print("[1-] Generar contraseña")
print("[2-] Salir")
print("------------------------------------")

opcion = int(input("Que opcion quieres?: "))


junto = letras + numeros + simbolos

if opcion == 1:
    decidir = int(input("Numeros para la contraseña: "))
    for i in range(decidir):
        contraseña += random.choice(junto)

elif opcion == 2:
    exit()


print (f"Tu contraseña es {contraseña}")
