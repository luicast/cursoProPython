def mayusculas(fun):
    def envoltura(texto):
        return fun(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"

print(mensaje(input("digita un texto: ")))