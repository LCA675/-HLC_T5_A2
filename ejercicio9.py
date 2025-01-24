num=(int(input("Adivina un número entre el 1 y el 50: ")))
import random
numero = random.randint(1, 50)
while num!=numero:
    print("Número incorrecto, vuelva a intentarlo")
    if (num>numero):
        print("El número a adivinar es menor")
    else:
        print("El número a adivinar es mayor")
    num=int(input("Adivina un número entre el 1 y el 50: "))
print("Ha adivinado el número!!!")
    