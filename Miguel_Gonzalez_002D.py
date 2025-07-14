productos = {"8475HP":["HP",15.6,"8GB",'DD',"1T",'INTEL CORE i5',"Nvidia GTX1050"],
             "2175HD":["lenovo",14,"4GB","SSD","512GB","Intel CORE i5","Nvidia GTX1050"],
             "JjfFHD":["Asus",14,"16GB","SSD","256GB","Intel CORE i5","Nvidia RTX2080Ti"],
             "fgdxFHD":["HP",15.6,"8GB",'DD',"1T",'INTEL CORE i3',"integrada"],
             "GF75HD":["Asus",15.6,"8GB",'DD',"1T",'INTEL CORE i7',"Nvidia GTX1050"],
             "123FHD":["lenovo",14,"6GB",'DD',"1T","ADM Ryzen 5","integrada"],
             "342FHD":["lenovo",15.6,"8GB",'DD',"1T","ADM Ryzen 7""Nvidia GTX1050"],
             "UWU131HD":["Dell",15.6,"8GB",'DD',"1T","ADM Ryzen 3""Nvidia GTX1050"],
             }

stock = {"8475HD":[387990,10],"2175HD":[327990,4],"JjfFHD":[424990,1],
         "fgdxFHD":[664990,2],"123FHD":[290890,32],"342FHD":[444990,7],
         "GF75HD":[749990,2],"UWU131HD":[349990,1],"FS1230HD":[249990,0]
         }

def numero_positivo_entero(numero:int):
    while True:
        try:
            valor = int(input(numero))
            if valor <= 0:
                print("Solo debe ingresar numero mayor a 0")
                continue
            return valor
        except ValueError:
            print("No debe ingresar el numero escrito o en decimal")

def valida_texto(texto:str):
    while True:
        letra = input(texto).strip().upper().lower()
        if not letra:
            print("No debe tener espacio el texto")
            continue
        return letra
    
def buscar_productos(marca:str):
    for i in productos:
        for m in marca:
            if i == m:
                return True
    return None

def stock_marca(marca:str):
    while True:
        precio = input(marca)
        if precio == "HP":
            return marca == 31
        elif precio == "levono":
            return marca ==20
        elif precio == "Asus":
            return marca == 10
        elif precio == " Dell":
            return marca== 5
        else:
            print("Producto no encontrado")

def precio_maximo(numero:int):
    while True:
        try:
            valor = int(input(numero))
            if valor < 750000:
                print("EL precio solo es hasta los 750000")
                continue
            return valor
        except valor:
            print("No debe ser escrito el numero")

def precio_minimo(stock:int):
    while True:
        try:
            valor = int(input(stock))
            if valor > 20000:
                print("EL precio minimo debe ser de 200000")
                continue
            return valor
        except ValueError:
             print("No debe ser escrito el numero")

def menu():
    while True:
        print("***MENU PRINCIPAL***")
        print("[1]- Stock marca")
        print("[2]- Busqueda por precio")
        print("[3]- Actualizar precio")
        print("[4]- Saliendo")
        
        opcion = numero_positivo_entero("Ingrese donde desee ir: ")

        if opcion == 1:
            productos = valida_texto("Ingrese la marca que busca: ")
            if buscar_productos(productos):
                print(stock_marca(productos))
        elif opcion == 2:
            precio_mini = precio_minimo("Ingrese el precio minimo: ")
            precio_max = precio_maximo("Ingrese su precio maximo: ")
            print(f"Los notebooks entre los precios consultados son:{stock}")
            print(f"{stock}")
        elif opcion == 3:
            print()
        elif opcion == 4:
            print("Usted esta saliendo del programa")
            break
        else:
            print("Debe seleccionar una opcion valida")

menu()





