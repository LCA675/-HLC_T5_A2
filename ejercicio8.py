def exponente():
    numero=int(input("Introduza un número ENTERO y POSITIVO: "))
    cuadrado=[]
    for i in range(1, numero+1):
        cuadrado.append(i**2)
        
    print(cuadrado)  

exponente()