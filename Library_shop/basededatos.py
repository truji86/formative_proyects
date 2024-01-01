import sqlite3


class Conexion:

  def __init__(self, ruta):
    self.ruta = ruta
    self.conexion = sqlite3.connect(ruta)
    self.cursor = self.conexion.cursor()

  def CrearTablaUsuario(self):
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS Usuario (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT,
      email TEXT,
      password TEXT
    )""")

  def CrearTablaLibros(self):
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS Libro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        genero TEXT,
        disponible INTEGER,
        precio REAL
        )""")

#CRUD
  #Create
  def CrearLibro(self, titulo, autor, genero, disponible, precio):
    self.cursor.execute("""INSERT INTO Libro (titulo, autor, genero, disponible, precio) VALUES (?, ?, ?, ?, ?)""", (titulo, autor, genero, disponible, precio), )
    self.conexion.commit()
    return "Libro registrado"

  def CrearUsuario(self, nombre, email, password):

    usuarios = self.VerUsuarios()
    for usuario in usuarios:
      if usuario[2] == email:
        return "Esta dirección de correo ya esta asociada a un usuario."
    self.cursor.execute(
        " INSERT INTO Usuario (nombre, email, password) VALUES (?, ?, ?)",
        (nombre, email, password),
    )
    self.conexion.commit()
    return "Usuario creado exitosamente"
  #Read
  def VerLibros(self):
    self.cursor.execute("SELECT * FROM Libro")
    info_libro = self.cursor.fetchall()
    return info_libro

  def VerLibrosDisponibles(self):
    self.cursor.execute("SELECT * FROM Libro WHERE disponible > 1")
    info_librodispo = self.cursor.fetchall()
    return info_librodispo

  def VerLibrosPorAutor(self, autor):
    self.cursor.execute("SELECT * FROM Libro WHERE autor = ?", (autor,))
    info_libroaut = self.cursor.fetchall()
    return info_libroaut

  def VerUsuarios(self):
    self.cursor.execute("SELECT * FROM Usuario")
    info_usuario = self.cursor.fetchall()
    return info_usuario

  def BuscarLibroPorID(self, id):
    self.cursor.execute("SELECT * FROM Libro WHERE id = ?", (id, ))
    info_libro = self.cursor.fetchall()
    return info_libro

  #Update
  def CambiarLibros(self, disponible, id):
    self.cursor.execute("UPDATE Libro SET disponible = ? WHERE id = ?",
                        (disponible, id))
    if self.cursor.rowcount == 1:
      self.conexion.commit()
      return True
    else:
      return False

  #Delete (desde la sustraccion)
  def VenderLibro(self, id, email):
    self.cursor.execute("SELECT * FROM Libro WHERE id = ?", (id, ))
    info_libro = self.cursor.fetchall()
    if info_libro[0][4] > 0:
      self.cursor.execute("SELECT * FROM Usuario WHERE email = ?", (email, ))
      info_usuario = self.cursor.fetchall()
      if info_usuario[0][2] == email:
        self.cursor.execute("UPDATE Libro SET disponible = disponible - 1 WHERE id = ?",
                            (id, ))
        self.conexion.commit()
        return True
      else:
        return False

  def CambiarMonto(self, id):
    self.cursor.execute("SELECT * FROM Libro WHERE id = ?", (id, )) 
    info_libro = self.cursor.fetchall()
    if info_libro[0][4] > 0:
      self.cursor.execute("UPDATE Libro SET disponible = disponible - 1 WHERE id = ?",
                          (id, ))
      self.conexion.commit()
      return True  

  #Desconectar de BD
  def CerrarConexion(self):
    self.conexion.close()
    return "Conexion cerrada"
  
  