def chequearcaracter():
    word=input("Introduza un texto:")
    for char in word:
        if "@"==char:
            print("El texto introducido contiene el carácter @")
        if "#"==char:
            print("El texto introducido contiene el carácter #")
        if "$"==char:
            print("El texto introducido contiene el carácter $")
        if "%"==char:
            print("El texto introducido contiene el carácter %")

chequearcaracter()
