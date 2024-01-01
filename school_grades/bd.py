import sqlite3


class conexion():

  def __init__(self):
    self.conexion = sqlite3.connect('calificaciones.db')
    self.cursor = self.conexion.cursor()

  #1. Creación de la Base de Datos:
  def CrearTablaEstudiantes(self):
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS estudiantes (
        id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        fecha_nacimiento DATE NOT NULL
      )
    """)
    self.conexion.commit()

  def CrearTablaCursos(self):
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS cursos (
        id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_curso TEXT NOT NULL)
    """)
    self.conexion.commit()

  def CrearTablaCalificaciones(self):
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS calificaciones (
        id_calificacion INTEGER PRIMARY KEY AUTOINCREMENT,
        id_estudiante INTEGER NOT NULL,
        id_curso INTEGER NOT NULL,
        calificacion INTEGER NOT NULL,
        FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
        FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
        )
      """)
    self.conexion.commit()

  def AgregarEstudiante(self, nombre, fecha_nacimiento):  
    self.cursor.execute("""
      INSERT INTO estudiantes (nombre, fecha_nacimiento)
      VALUES (?, ?)
    """, (nombre, fecha_nacimiento))
    self.conexion.commit()

  def AgregarCurso(self, nombre_curso):
    self.cursor.execute("""
      INSERT INTO cursos (nombre_curso)
      VALUES (?)
    """, (nombre_curso,))
    self.conexion.commit()
    
  #2. Operación de Agregar Calificación:
  def AgregarCalificacion(self, id_estudiante, id_curso, calificacion):
    self.cursor.execute("""
      INSERT INTO calificaciones (id_estudiante, id_curso, calificacion)
      VALUES (?, ?, ?)
    """, (id_estudiante, id_curso, calificacion))
    self.conexion.commit() 

  def MostrarEstudiantes(self):
    self.cursor.execute("""
      SELECT * FROM estudiantes
    """)
    return self.cursor.fetchall()

  def MostrarCursos(self):
    self.cursor.execute("""
      SELECT * FROM cursos
    """)
    return self.cursor.fetchall()

  def MostrarCalificaciones(self):
    self.cursor.execute("""
      SELECT * FROM calificaciones
      ORDER BY id_calificacion DESC
    """)
    
    return self.cursor.fetchall()  

  #3. Operación de Ver Calificaciones de un Estudiante:
  def VerCalificacionesDeUnEstudiante(self, nombre):
    self.cursor.execute("""
      SELECT c.nombre_curso, cal.calificacion
      FROM calificaciones cal
      INNER JOIN cursos c ON cal.id_curso = c.id_curso
      INNER JOIN estudiantes e ON cal.id_estudiante = e.id_estudiante
      WHERE e.nombre = ?
    """, (nombre,))
    return self.cursor.fetchall()

  #4. Operación de Ver Calificaciones en un Curso
  def VerCalificacionesDeUnCurso(self, nombre_curso):
    self.cursor.execute("""
      SELECT e.nombre, c.nombre_curso, cal.calificacion
      FROM calificaciones cal
      INNER JOIN cursos c ON cal.id_curso = c.id_curso
      INNER JOIN estudiantes e ON cal.id_estudiante = e.id_estudiante
      WHERE c.nombre_curso = ?
      ORDER BY calificacion DESC
    """, (nombre_curso,))
    return self.cursor.fetchall()

  #5. Operación de Búsqueda de Estudiantes por Calificación:
  def BusquedaEstudiantesPorCalificacion(self, calificacion):
    self.cursor.execute("""
      SELECT e.nombre, c.nombre_curso, cal.calificacion
      FROM calificaciones cal
      INNER JOIN cursos c ON cal.id_curso = c.id_curso
      INNER JOIN estudiantes e ON cal.id_estudiante = e.id_estudiante
      WHERE cal.calificacion = ?
    """, (calificacion,))
    return self.cursor.fetchall()  
    

  #6. Operación de Eliminación de Calificación:
  def BorrarCalificacionDeUnAlumno(self, id_estudiante, id_curso, calificacion):
      self.cursor.execute("""
        DELETE FROM calificaciones 
        WHERE id_estudiante = ? AND id_curso = ? AND calificacion = ?
      """, (id_estudiante, id_curso, calificacion))
      self.conexion.commit()
    
  def CerrarConexion(self):
    self.conexion.close()

  
    
