import msvcrt
from functions import *
movies = []


def run():
    print("""
Lenguajes formales y de programación
Sección B+
Carné: 201807154
Desarrollador: Denny Alexander Chalí Miza\n
Presiona cualquier tecla para continuar...\n""")

    #Esperar hasta que se presione una tecla
    msvcrt.getch()
    end = False
    selection = 0

    while not end:
        print("\n------------ Menú ------------\n  1. Cargar archivo\n  2. Gestionar películas\n  3. Filtrar\n  4. Gráfica\n  5. salir")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            contentFile = leerArchivo()
            if contentFile != None:
                analizador(contentFile, movies)
            else:
                print("Datos no cargados")

        elif selection == 2:
            gestionar(movies)

        elif selection == 3:
            filtrar(movies)
            
        elif selection == 4:
            graficar(movies)
                
        elif selection == 5:
            print("Finalizando programa...")
            end = True
        else:
            print("Error, ingrese una opción correcta.") 

if __name__ == '__main__':
    run()