import funciones as fu

while True:
    fu.limpiarpantalla()
    fu.printv("SISTEMA VENTABOOKS")
    fu.printa("******************")
    print("1) Guardar Libro")
    print("2) Buscar Libro")
    print("3) Certificados de libros")
    print("0) Salir")
    opcion = int(input("Seleccione : "))

    if opcion==0:
        fu.printa("ADIOS")
        break
    elif opcion==1:
        fu.printv("GUARDAR")
    elif opcion==2:
        fu.printv("BUSCAR")
    elif opcion==3:
        fu.printv("CERTIFICADOS")
    else:
        fu.printr("NO VALIDO")