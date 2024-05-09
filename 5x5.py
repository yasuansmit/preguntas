matriz1 = [["☐","☐","☐","☐","☐"],
           ["☐","☐","☐","☐","☐"],
           ["☐","☐","☐","☐","☐"],
           ["☐","☐","☐","☐","☐"],
           ["☐","☐","☐","☐","☐"],
           ["☐","☐","☐","☐","☐"]]
correcto = "😀"
incorrecto = "☠️"
ls_pregunta = ["Que es python? \n\n1. juego\n2. Lenguaje de progamacion \n3. Marca de auto \n4. de la anteriores "
               ,"Que es Html?\n\n1. Lenguaje de programacion\n2. Marca de gaseoasa \n3. Navegador \n3. Es un perroC,",
               "Donde que da la Luis amigo Centro regional?? \n1. En turbo\n2. En carepa\n3. En Bolivia\n4.En apartado ",
               "Quien es dulfran? \n1. Un astranaouta \n2. El mejor profe de la Luis Amigo \n3.Un simple profesor\n4. Un señor",
               "Para que su utiliza la funcion <FOR>\n1. Para ciclos \n2. para limpiar \n3.Para escribir \n3.Para nada"
               ]
ls_respuesta = ["2", "1", "4","2","1"]
def fnt_pintarMatriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j], end = "   ")
        print("\n\n")
contador = 0
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        import os
        os.system("cls")
        fnt_pintarMatriz()
        print()
        print(ls_pregunta [contador])
        print()
        r = input("- >")
        if r == ls_respuesta[contador]:
            matriz1[i][j] = correcto
        else:
            matriz1[i][j] = incorrecto
        contador += 1