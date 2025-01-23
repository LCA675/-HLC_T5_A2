num1=float(input("Introduzca un número: "))
num2=float(input("Introduzca un segundo número: "))
num3=float(input("Introduza un tercer número: "))
if (num1==num2==num3):
    print("Todos los números son iguales, no hay mayor")
elif(num1==num2!=num3):
    print("Hay empate entre los dos primeros")
elif (num1==num3!=num2):
    print("Hay empate entre el primero y el tercero")
elif(num2==num3!=num1):
    print("Hay empate entre el segundo y el tercero")
elif(num1>num2 and num1>num3):
    print("El número mayor es el primero")
elif(num2>num1 and num2>num3):
    print("El número mayor es el segundo")
elif(num3>num2 and num3>num1):
    print("El número mayor es el tercero")
