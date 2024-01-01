from bd import conexion

opcion = 0

conexion = conexion()
conexion.CrearTablaEstudiantes()
conexion.CrearTablaCursos()
conexion.CrearTablaCalificaciones()

while opcion != "8":
  print("Menu de opciones del calificador")
  opcion = input(
      "1- Agregar estudiante\n2- Agregar curso\n3- Agregar calificacion\n4- Ver calificacion de un estudiante\n5- Ver calificaciones de un curso\n6- Ver estudiantes por calificacion\n7- Borrar calificacion\n8- Salir\n"
    )
  if opcion == "1":
    print("Agregar estudiante")
    result_A = conexion.MostrarEstudiantes()
    if len(result_A) > 0:
        for resultado in result_A:
          print(f"Id {resultado[0]}- Estudiante: {resultado[1]}, Fecha de nacimiento: {resultado[2]}")
    nombre = input("Ingrese el nombre del estudiante: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante: ")
    while nombre == "" or fecha_nacimiento == "":
      print("Los campos no pueden estar vacios")
      nombre = input("Ingrese el nombre del estudiante: ")
      fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante: ")
    result_B = conexion.AgregarEstudiante(nombre, fecha_nacimiento)
    if result_B == True:
      conexion.AgregarEstudiante(nombre, fecha_nacimiento)
    else:
      print(f"Estudiante {nombre} agregado correctamente")
    
  elif opcion == "2":
    print("Agregar curso")
    result_B = conexion.MostrarCursos()
    if len(result_B) > 0:
        for resultado in result_B:
          print(f"Id {resultado[0]} Curso: {resultado[1]}")
    nombre_curso = input("Ingrese el nombre del curso: ")
    while nombre_curso == "":
      print("El campo no puede estar vacio")
      nombre_curso = input("Ingrese el nombre del curso: ")
    result_C = conexion.AgregarCurso(nombre_curso)
    if result_C == True:
      conexion.AgregarCurso(nombre_curso)
    else:
      print("Curso agregado correctamente")

  elif opcion == "3":
    print("Agregar calificacion")
    result_A = conexion.MostrarEstudiantes()
    if len(result_A) > 0:
        for resultado in result_A:
          print(f"Id {resultado[0]} Estudiante: {resultado[1]}")
    result_B = conexion.MostrarCursos()
    if len(result_B) > 0:
        for resultado in result_B:
          print(f"Id {resultado[0]} Curso: {resultado[1]}")
    id_estudiante = input("Ingrese el ID del estudiante: ")
    id_curso = input("Ingrese el ID del curso: ")
    calificacion = float(input("Ingrese la calificacion: "))
    while calificacion < 0 or calificacion > 10:
      print("La calificacion debe ser un numero entre 0 y 10")
      calificacion = float(input("Ingrese la calificacion: "))
    result_C = conexion.AgregarCalificacion(id_estudiante, id_curso, calificacion)
    if result_C == True:
      conexion.AgregarCalificacion(id_estudiante, id_curso, calificacion)
    else:
      print(f"Calificacion agregada: {calificacion} para el estudiante {id_estudiante} en el curso {id_curso}")
  
  elif opcion == "4":
    print("Ver calificacion de un estudiante")
    result_A = conexion.MostrarEstudiantes()
    if len(result_A) > 0:
        for resultado in result_A:
          print(f"Estudiante: {resultado[1]}")
    nombre = input("Ingrese el nombre completo del estudiante: ")  
    listado_calA = conexion.VerCalificacionesDeUnEstudiante(nombre)
    if len(listado_calA) > 0:
      for resultado in listado_calA:
        print(f"En el curso {resultado[0]}, calificacion: {resultado[1]}")
    else:
        print("No hay calificaciones para este estudiante")
    
  elif opcion == "5":
    print("Ver calificaciones de un curso")
    result_B = conexion.MostrarCursos()
    if len(result_B) > 0:
        for resultado in result_B:
          print(f"Curso: {resultado[1]}")
    nombre_curso = input("Ingrese nombre del curso: ")
    while nombre_curso == "":
      print("El campo no puede estar vacio")
      nombre_curso = input("Ingrese nombre del curso: ")
    listado_calB = conexion.VerCalificacionesDeUnCurso(nombre_curso)
    print("Listado con las notas de mayor a menor:")
    if len(listado_calB) > 0:
      for resultado in listado_calB:
        print(f"Estudiante: {resultado[0]}, calificacion: {resultado[2]}")
    else:
      print("No hay calificaciones para este curso")
      
  elif opcion == "6":
    print("Ver estudiantes por calificacion")
    calificacion = input(f"Ingrese la calificacion: ")
    listado_calC = conexion.BusquedaEstudiantesPorCalificacion(calificacion)
    if len(listado_calC) > 0:
      for resultado in listado_calC:
        print(f"Estudiante: {resultado[0]}")
    else:
      print("No hay estudiantes con esa calificacion")
           
  elif opcion == "7":
    print("Borrar calificacion")
    result_A = conexion.MostrarEstudiantes()
    if len(result_A) > 0:
      for resultado in result_A:
        print(f"Id {resultado[0]} Estudiante: {resultado[1]}")
    result_B = conexion.MostrarCursos()
    if len(result_B) > 0:
       for resultado in result_B:
        print(f"Id {resultado[0]} Curso: {resultado[1]}")
    result_C = conexion.MostrarCalificaciones()
    if len(result_C) > 0:
       for resultado in result_C:
        print(f"ID Estudiante: {resultado[1]}, Calificacion: {resultado[3]}")
    id_estudiante = input("Ingrese el ID del estudiante: ")
    id_curso = input("Ingrese el ID del curso: ")
    calificacion = float(input("Ingrese la calificacion: "))
    conexion.BorrarCalificacionDeUnAlumno(id_estudiante, id_curso, calificacion)
    print(f"Calificacion del estudiante ID {id_estudiante} ,borrada")
    
  elif opcion == "8":
    print("Saliendo...")
    conexion.CerrarConexion()  
    break
else:
  print("Opcion incorrecta")

    