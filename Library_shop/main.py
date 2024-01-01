from basededatos import Conexion

nuevaconexionU = Conexion("Usuarios.db") # Crea una instancia de la clase Conexion
nuevaconexion = Conexion("Libreria.db") # Crea una instancia de la clase Conexion
nuevaconexionU.CrearTablaUsuario()
nuevaconexion.CrearTablaLibros()

menu=0
while menu != "4":
  print("Sistema Libreria, bienvenido")
  menu = input("Elija una opcion\n1-Crear usuario\n2-Ver usuarios\n3-iniciar sesion\n4-Salir\n")
  if (menu == "1"):
    nombre=input("Ingrese nombre: ")
    while len(nombre)==0:
        nombre = input("Ingrese un nombre valido, debe contener...: ")
    mail = input("Ingrese mail: ")
    while "@gmail.com" not in mail:
        mail = input("Ingrese mail correcto: ")
    contraseña = input("Ingrese contraseña: ")
    print( nuevaconexionU.CrearUsuario(nombre, mail, contraseña))
  elif (menu == "2"):
    resultados = nuevaconexionU.VerUsuarios()
    if len(resultados) > 0:
      print(resultados)
    else:
      print("no hay usuarios")
  elif (menu == "3"):
    resultados = nuevaconexionU.VerUsuarios()
    if len(resultados) > 0:
      mail = input("Ingrese mail: ")
      contraseña = input("Ingrese contraseña: ")
      encontrado = None
      for usuario in resultados:
        if mail == usuario[2] and contraseña == usuario[3]:
          encontrado = usuario
          break
        if encontrado is None:
          print("No se encontró")
      else:
        print("Bienvenido usuario ", encontrado)
    
      opcion = 0
      while opcion != "6":
            opcion = input(
                "Elija una opcion:\n 1-Crear libro\n 2-Ver libros disponibles\n 3-Buscar por autor\n 4-Ver libros disponibles\n 5-Vender Libro\n 6-Salir del menu de ventas\n"
            )
            if (opcion == "1"):
                nombre = input("Ingrese el nombre: ")
                autor = input("Ingrese autor: ") 
                genero = input("Ingrese genero: ")
                disponible = int(input("Ingrese cantidad de libros: "))
                precio = float(input("Ingrese precio: "))
                nuevaconexion.CrearLibro(nombre, autor, genero, disponible, precio)
            elif (opcion == "2"):
              resultados = nuevaconexion.VerLibrosDisponibles()
              if len(resultados) > 0:
                for resultado in resultados:
                  print(f"Id {resultado[0]} Nombre de libro: {resultado[1]} Autor: {resultado[2]} Genero: {resultado[3] } Ejemplares disponibles: {resultado[4]} Precio: ${resultado[5]}  \n")
              else:
                print("No hay libros disponibles")
            elif (opcion == "3"):
              autor = input("Ingrese autor: ")
              while len(autor) == 0:
                autor = input("Ingrese autor correcto: ")
              resultados = nuevaconexion.VerLibrosPorAutor(autor)
              if len(resultados) > 0:
                for resultado in resultados:
                  print(f"Id {resultado[0]} Nombre de libro {resultado[1]} Autor {resultado[2]} Genero {resultado[3] } Disponible(cant. ejemplares): {resultado[4]} Precio: ${resultado[5]} \n")
              else:
                print("no hay libros disponibles")        
            elif (opcion == "4"):
              resultados = nuevaconexion.VerLibros()
              if len(resultados) > 0:
                for resultado in resultados:
                  print(f"Id {resultado[0]} Nombre de libro {resultado[1]} Autor {resultado[2]} Genero {resultado[3] } Disponible(cant. ejemplares): {resultado[4]} Precio: ${resultado[5]} \n")
              else:
                print("no hay libros disponibles")
            elif (opcion == "5"):
              id = int(input("Ingrese el id del libro a buscar: "))
              resultados = nuevaconexion.BuscarLibroPorID(id)
              print(f"Hay {resultados [0][4]} libros") 
              cantidad = 10000
              while (cantidad > resultados[0][4]):
                cantidad = int(input("Ingrese cantidad de libros a comprar: "))
              cantidadARestar = resultados[0][4] - cantidad
              nuevaconexion.CambiarLibros(cantidadARestar, id)
              print(f"Venta exitosa. Hay {cantidadARestar} libros en stock")
              montoVenta = cantidad * resultados[0][5]
              print(f"El monto total de la venta es: ${montoVenta}")
            elif (opcion == "6"):
              nuevaconexion.CerrarConexion()
  
    elif (menu == "4"):
      print("Gracias por usar el programa")
    else:
      print("Opcion no valida")