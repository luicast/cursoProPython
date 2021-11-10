def crearSet(set1,set2):
    print(f"set 1: {set1}\n")
    print(f"set 2: {set2}\n")

def operaciones(opcion:int, set1, set2):
    if opcion == 1:
        setUnion = set1 | set2
        crearSet(set1, set2)
        print(f"la union de los sets es {setUnion}\n")
        mensaje()
    elif opcion == 2:
        setIneter = set1 & set2
        crearSet(set1, set2)
        print(f"la interseccion de los sets es {setIneter}\n")
        mensaje()
    elif opcion == 3:
        setdif = set1 - set2
        crearSet(set1, set2)
        print(f"la diferencia de los sets es {setdif}\n")
        mensaje()
    elif opcion == 4:
        setdifsime = set1 ^ set2
        crearSet(set1, set2)
        print(f"la diferencia simetricas de los sets es: {setdifsime}\n")
        mensaje()
    else:
        print("opcion incorrecta\n")
        mensaje()



def mensaje():
    msj = input("desea realizar otra conversion [y/n]: ")
    if msj == "y":
        run()
    else:
        print("gracias por usar este servicio")


def run():
    menu = """
    OPERACIONES CON LOS SETS
    
    1 - UNINON
    2 - INTERSECCION
    3 - DIFERENCIA
    4 - DIFERENCIA SIMETRICA 

    eliga una opcion:"""
    opcion = int(input(menu))
    mySet1 = {1,2,3,4}
    mySet2 = {4,5,6,7}
    operaciones(opcion, mySet1, mySet2)


if __name__ == "__main__":
    run()