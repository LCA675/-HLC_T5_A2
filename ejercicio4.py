def chequeo():
    fallos=0
    contraseña_correcta="secreta123"
    while (fallos<3):
        contraseña=(input("Introduzca su contraseña: "))
        if (contraseña==contraseña_correcta):
            print("Bienvenido!!")
            break
        elif (contraseña !=contraseña_correcta):
            fallos=fallos+1
            print("Contraseña incorrecta")
        if (fallos==3):
            print("Ha fallado su contraseña 3 veces. Su cuenta ha sido bloqueada")

chequeo()