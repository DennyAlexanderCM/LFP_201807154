from tkinter import filedialog
import graphviz
from graphviz import nohtml
from movie import Movie

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opción: "))
            correcto=True
        except ValueError:
            print('¡Error, introduce un numero entero!')
    return num 

def leerArchivo():
    #obtenemos la direccion local del archivo
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("lfp","*.lfp"),("Todos los archivos","*.*")))
    if root != "":
        try:
            #encoding utf-8
            file = open(root,'r',encoding='utf-8')
            contentFile = file.read()
            file.close()

            return contentFile
        
        except:
            print("Ha ocurrido un error")
            file.close()
        
    return None

def analizador(contentFile, movies:list):
    errores_detectados = False
    #quitamos los espacios al incio y al final de la cadena
    data = contentFile.strip()
    #creamos una lista con cada fila
    lines = data.split("\n")
    n = 0
    #recorremos la lista de lineas
    for line in lines:
        n += 1
        aux = line.split(";")
        if len(aux) == 4:
            try:
                nameMovie = aux[0].strip()
                movie = verificarRepetido(nameMovie, movies)
                if not(movie):
                    movie = Movie(nameMovie, aux[2].strip(), aux[3].strip())
                    actores = aux[1].split(",")
                    for actor in actores:
                        movie.addActor(actor.strip())
                    movies.append(movie)
                else:
                    movie.setAnio(aux[2].strip())
                    movie.setGenero(aux[3].strip())
                    actores = aux[1].split(",")
                    movie.actorsClearList()
                    for actor in actores:
                        movie.addActor(actor.strip())
            except:
                errores_detectados = True
                print("¡Ha ocurrido un error")
        else:
            errores_detectados = True
            print("Datos erroneos en la línea: " + str(n))
    
    if errores_detectados:
        print("Archivo Cargado con errores detectados")
    else:
        print("Archivo Cargado correctamente")

def verificarRepetido(pelicula, movies:list):
    for movie in movies:
        if movie.getNombre() == pelicula:
            return movie
    
    return None
    
def gestionar(movies:list):
    end = False
    selection = 0
    while not end:
        print("\n--------- Gesionar películas ---------\n 1. Mostrar películas\n 2. Mostrar actores\n 3. Regresar")
        selection = pedirNumeroEntero()
        if selection ==1:
            mostrarPeliculas(movies)
        elif selection == 2:
            mostrarActores(movies)
        elif selection == 3:
            end = True
        else:
            print("Error, ingrese una opción correcta.")

def mostrarPeliculas(movies:list):
    i = 1
    print("\n--------- Películas Cargadas ---------")
    for movie in movies:
        movie:Movie
        print(str(i) + ". " + movie.getNombre()+ " | Año: " + movie.getAnio() +" | Género: " + movie.getGenero()+"\n")
        i += 1

def mostrarActores(movies:list):
    print("\n-------- Seleccione película --------")
    i = 0
    for movie in movies:
        i += 1
        print(str(i) + ". " + movie.getNombre())

    num = pedirNumeroEntero()
    if num <= i and num > 0:
        movie:Movie = movies[num -1]
        actors = movie.getActores()
        i += 1
        print("\n"+movie.getNombre()+ " | Año: " + movie.getAnio() +" | Género: " + movie.getGenero())
        print("Actores: ")
        j = 1
        for actor in actors:
            print("\t" + str(j) +". "+actor)
            j += 1
    else:
        print("¡Ingrese una opción correcta!")
    

def filtrar(movies):
    end = False
    selection = 0

    while not end:
        print("\n---------- Filtrar por ----------\n  1. Actor\n  2. Año\n  3. Género\n  4. Regresar")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            filtrarActor(movies)

        elif selection == 2:
            filtrarAnio(movies)

        elif selection == 3:
            filtrarGenero(movies)
                
        elif selection == 4:
            end = True
        else:
            print("Error, ingrese una opción correcta.")

def filtrarActor(movies:list):
    print("\n-------- Seleccione actor --------")
    i = 0
    actores = []
    for movie in movies:
        for actor in movie.getActores():
            if not(actor in actores):
                actores.append(actor)
                i += 1
                print(str(i) + ". " + actor)

    num = pedirNumeroEntero()
    if num <= i and num > 0:
        seleccionado = actores[num-1]
        print("\nActor: " + seleccionado)
        print("Peliculas: ")
        j = 1
        for movie in movies:
            if seleccionado in movie.getActores():
                print("\t"+ str(j)+". " + movie.getNombre())
                j += 1
    else:
        print("¡Ingrese una opción correcta!")

def filtrarAnio(movies):
    print("\n-------- Seleccione año --------")
    i = 0
    anios = []
    for movie in movies:
        if not(movie.getAnio() in anios):
            anios.append(movie.getAnio())
            i += 1
            print(str(i) + ". " + movie.getAnio())

    num = pedirNumeroEntero()
    if num <= i and num > 0:
        seleccionado = anios[num -1]
        print("\nPeliculas del año: " + seleccionado)
        j = 1
        for movie in movies:
            if movie.getAnio()== seleccionado:
                print(str(j)+". "+ movie.getNombre())
                j+=1
    else:
        print("¡Ingrese una opción correcta!")

def filtrarGenero(movies):
    print("\n-------- Seleccione Género --------")
    i = 0
    generos = []
    for movie in movies:
        if not(movie.getGenero() in generos):
            generos.append(movie.getGenero())
            i += 1
            print(str(i) + ". " + movie.getGenero())

    num = pedirNumeroEntero()
    if num <= i and num > 0:
        seleccionado = generos[num -1]
        print("\nPeliculas genero: " + seleccionado)
        j = 1
        for movie in movies:
            if movie.getGenero() == seleccionado:
                print(str(j)+ ". "+ movie.getNombre())
                j+= 1
    else:
        print("¡Ingrese una opción correcta!")

def graficar(movies:list):
    g = graphviz.Digraph('g', filename='Movies',
                        node_attr={'shape': 'record', 'height': '.1'})
    g.attr(rankdir='LR')

    actores = []
    for movie in movies:
        for actor in movie.getActores():
            if not(actor in actores):
                actores.append(actor)

    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled', color='white', margin= "40")
        for movie in movies:
            movie:Movie
            c.node(movie.getNombre(), nohtml(r'{ {<f0> '+ movie.getNombre() +' | {'+ movie.getGenero() +' | '+ movie.getAnio() +' } }}'), color = "blue")

    with g.subgraph(name='cluster_1') as c:
        c.attr(style='filled', color='white', margin = "40")
        for actor in actores:

            c.node(actor, nohtml('<f0>'+ actor))

    for movie in movies:
        movie:Movie
        movie_actors = movie.getActores()
        for actor in movie_actors:
            g.edge(movie.getNombre(), actor)   
        #g.edge('peli1:f0', 'actor2:f0')
   
    g.view()