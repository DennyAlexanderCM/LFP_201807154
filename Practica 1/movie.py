class Movie:
    def __init__(self, nombre, año, genero):
        self.nombre = nombre
        self.año = año
        self.genero = genero
        self.actores = []
    
    def getNombre(self):
        return self.nombre
    
    def getAnio(self):
        return self.año
    
    def getGenero(self):
        return self.genero
    
    def getActores(self):
        return self.actores
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setAnio(self, anio):
        self.año = anio
    
    def setGenero(self, genero):
        self.genero = genero
    
    def setActores(self, actores):
        self.actores = actores
    
    def addActor(self, actor):
        self.actores.append(actor)
    
    def actorsClearList(self):
        self.actores.clear()