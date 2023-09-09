#Desarrollar una funcion que solicite la carga del dia, mes y año y
#almavene dichos datos en una tupla que luego debe retornar.
#la segunda funcion a implementar debe recibir una tupla
#con la fecha y mosgrarla por pantalla.
def cargar_fecha():
    dd=int(input("Ingresa numero de dia:"))
    mm=int(input("Ingrese numero de mes:"))
    aa=int(input("Ingrese numero de año:"))
    return (dd,mm,aa)


def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")


# bloque principal
fecha=cargar_fecha()
imprimir_fecha(fecha)
