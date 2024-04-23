#Equipo3
class ListaPersonalizada:
    def __init__(self):
        self.datos = []

    def agregar(self, elemento):
        self.datos.append(elemento)

    def buscar(self, elemento):
        try:
            indice = self.datos.index(elemento)
            return indice
        except ValueError:
            return -1

    def eliminar(self, elemento):
        try:
            self.datos.remove(elemento)
            return True
        except ValueError:
            return False

    def ordenar(self):
        self.datos.sort()

# Ejemplo de uso:
lista_personalizada = ListaPersonalizada()

# Agregar elementos
lista_personalizada.agregar(5)
lista_personalizada.agregar(2)
lista_personalizada.agregar(8)
lista_personalizada.agregar(3)

# Buscar elemento
indice = lista_personalizada.buscar(5)
if indice != -1:
    print("Elemento encontrado en el índice:", indice)
else:
    print("Elemento no encontrado")

# Eliminar elemento
if lista_personalizada.eliminar(2):
    print("Elemento eliminado exitosamente")
else:
    print("Elemento no encontrado")

# Ordenar elementos
lista_personalizada.ordenar()
print("Lista ordenada:", lista_personalizada.datos)