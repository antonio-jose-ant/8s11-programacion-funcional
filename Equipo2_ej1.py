def busqueda_binaria(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1
   
    while bajo <= alto:
        medio = (bajo + alto) // 2
       
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
           
    return -1

def buscar_en_intervalo(arr, objetivo, tipo_intervalo):
    if tipo_intervalo == 'cerrado':
        return busqueda_binaria(arr, objetivo)
    elif tipo_intervalo == 'abierto':
        return busqueda_binaria_abierta(arr, objetivo)
    elif tipo_intervalo == 'semi-abierto':
        return busqueda_binaria_semi_abierta(arr, objetivo)
    else:
        raise ValueError("Tipo de intervalo inválido")

def busqueda_binaria_abierta(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1
   
    while bajo < alto:
        medio = (bajo + alto) // 2
       
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
           
    return -1

def busqueda_binaria_semi_abierta(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1
   
    while bajo <= alto:
        medio = (bajo + alto) // 2
       
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
           
    return -1

# Ejemplo de uso:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = 3
tipo_intervalo = 'semi-abierto'
resultado = buscar_en_intervalo(arr, objetivo, tipo_intervalo)
print("Índice del elemento objetivo:", resultado)
