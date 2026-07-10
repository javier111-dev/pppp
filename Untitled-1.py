
vehiculos = {
    "V001": ["Toyota", "Corolla", "Sedán", "B", True, "Toyota"],
    "V002": ["Hyundai", "Tucson", "SUV", "B", True, "Hyundai"],
    "V003": ["Kia", "Rio", "Hatchback", "B", False, "Kia"],
    "V004": ["Tesla", "Model 3", "Sedán", "E", True, "Tesla"],
    "V005": ["Chevrolet", "Montana", "Pickup", "D", False, "Chevrolet"]
    }

inventario = {
    "V001": [18500000, 4],
    "V002": [23990000, 3],
    "V003": [14990000, 6],
    "V004": [38990000, 2],
    "V005": [27990000, 1]
    }

def buscar_codigo(codigo,vehiculos):
    if codigo in vehiculos:
        return True
    return False

def actualizar_precio(codigo,nuevoprecio,inventario, vehiculos):
    if buscar_codigo(codigo, vehiculos):
        inventario[codigo][0]= nuevoprecio

def validar_codigo(codigo, vehiculos):
    return codigo.strip() != " " and codigo.strip not in vehiculos

def validar_marca(marca):
    return marca.strip() != " "

def validar_modelo(modelo):
    return modelo.strip() != " "

def validar_tipo(tipo):
    return tipo.strip() != " "

def validar_combustible(combustible):
    return combustible.strip == "b" or combustible.strip()=="d" or combustible.strip()=="e"

def validar_automatico(automatico):
    opcion=automatico.strip().lower()
    return automatico =="si" or automatico == "no"

def validar_texto(texto):
    return texto.strip() != " "

def stock_tipo(vehiculos,tipo,inventario):
    total=0
    for codigo in vehiculos:
        if vehiculos [codigo][2].lower()== tipo.lower():
            total += inventario[codigo][1]
     
    print(f"el total de vehiculos para este tipo es: {total}")

def agregar_vehiculo(vehiculos, inventario, codigo, marca, modelo, tipo, combustible, automatico, fabricante, precio, stock):
    if buscar_codigo(codigo,vehiculos):
        return False
    
    es_automatico=False
    if automatico.strip().lower()=="si":
        es_automatico=True

    vehiculos[codigo]=[combustible.strip().upper(marca, modelo, tipo,), es_automatico, fabricante]
    inventario[codigo]=[precio,stock]
    return True

def leer_opcion():
    while True:
        try:
            opcion=int(input("ingrese una opcion valida: "))

            if opcion >= 1 and opcion <= 6:
                return opcion
                break
            else:
                print("opcion fuera del ranfo")
        except ValueError:
            print("error: la opcion debe ser entero y positivo")

def validar_precio(precio):
    return int(precio) > 0

def validar_stock(stock):
    return int(stock)>=0

def vahiculoporprecio(minimo,maximo,vehiculos, inventario):
    encontrados=[]

    for codigo in inventario:
        precio=inventario[codigo][0]
        stock=inventario[codigo][1]

        if precio > minimo and precio < maximo and stock >0:
            marca=vehiculos[codigo][0]
            modelo=vehiculos[codigo][1]
            encontrados.append(f"{marca}-- {codigo}- {modelo}")

    if len(encontrados)> 0:
        encontrados.sort()
        print("vehiculos encontrados: ")
        print(encontrados)
    else:
        print("no hay nada por este rango de precio")


def menu():
    print("--- menu principal----")
    print("1. stock por tipo de vehiculo")
    print("2. buscar vehiculo por rango de precio")
    print("3. actualizar precio")
    print("4. agregar vehiculo")
    print("5. eliminar vehiculo ")
    print("6. salir")


def eliminar_vehiculo(vehiculos, inventario, codigo):
    if buscar_codigo(codigo,vehiculos):
        vehiculos.pop(codigo)
        inventario.pop(codigo)
        return True
    return False

while True:
    menu()
    opcion=leer_opcion()

    if opcion==1:
        tipo=input("seleccione el tipo de vehiculo: ")
        stock_tipo(vehiculos,tipo,inventario)
    elif opcion == 2:
        while True:
            try:
                minimo=int(input("ingrese un monto como minimo"))
                maximo=int(input("ingrese un monto como maximo: "))
                break
            except ValueError:
                print("el numero debe entero y positivo")
        vahiculoporprecio(minimo,maximo,vehiculos, inventario)
    elif opcion == 3:
        continuar="si"

        while continuar=="si":
            codigo=input("ingrese el codigo del vehiculo: ").lower()
            try:
                nuevoprecio=int(input("ingrese el nuevo precio: "))

                if actualizar_precio(codigo,nuevoprecio,inventario, vehiculos):
                    print("precio actualizado. ")
                else:
                    print("el codigo no existe: ")
            except ValueError:
                print("el numero debe ser entero y positivo")
            continuar=input("\ndesea continuar (si/no)?")
    elif opcion== 4:
        codigo=input("ingrese el codigo: ")
        while not validar_codigo(codigo):
            print("el codigo no puede estar vacio")
            codigo =input("ingrese el codigo")

        marca=input("ingrese la marca")       
        while not validar_marca(marca):
            print("la marca no puede estar vacia: ")
            marca=input("ingrese la marca: ")

        modelo=input("ingrese el modelo: ")
        while not validar_modelo(modelo):
            print("el modelo no puede estar vacio")
            modelo=input("ingrese un modelo ")

        tipo=input("ingrese un tipo de vehiculo")
        while not validar_tipo(tipo):
            print("no cooresponde a ningun tipo")
            tipo=input("ingrese el tipo de vehiculo")
        
        combustible=input("seleccione un tipo de combustible: ")
        while not validar_combustible(combustible):
            print("no existe ese tipo de combustible")
            combustible=input("seleccione nuevamente el combustible: ")

        automatico=("es automatico (si-no): ")
        while not validar_automatico(automatico):
            print("no puede estar vacio: ")
            automatico=input("ingrese nuevamente ")
        
        fabricante=input("ingrese el fabricante: ")
        while not validar_texto():
            print("no puede estar en blanco")
            fabricante=input("ingrese el fabricante ")
        
        while True:
            try:
                stock=int(input("ingrese el stock: "))
                if validar_stock(stock):
                    break
                else:
                    print("el stock debe ser mayo o igual a cero: ")
            except ValueError:
                print("el numero debe ser mayor o igual q cero")
        if agregar_vehiculo(vehiculos, inventario, codigo, marca, modelo, tipo, combustible, automatico, fabricante, precio, stock)
            print("vehiculo agregado con exito. ")
        else:
            print("el codigo ya existe")
    
    elif opcion== 5:
        if buscar_codigo(codigo, vehiculos):
            inventario.pop(el)

        