def detectar_tipo_dato(entrada):
    try:
        float(entrada)
        return "numérico"
    except ValueError:
        if entrada.lower() in ['true', 'false']:
            return "booleano"
        else:
            return "cadena"

# Ejemplo de uso
dato = input("Ingrese un dato: ")
tipo = detectar_tipo_dato(dato)
print("El dato ingresado es de tipo:", tipo)

