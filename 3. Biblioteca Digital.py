from datetime import datetime, timedelta
class Material:
    def __init__(self,titulo,estado):
        self.titulo = titulo
        self.estado=estado
    pass

class Libro(Material):
    def __init__(self, titulo,autor, genero, estado="Disponible"):
        super().__init__(titulo,estado)
        self.autor=autor
        self.genero=genero
    
    def __str__(self):
        return f"Libro: '{self.titulo}' por {self.autor} (Género: {self.genero}) - Estado: {self.estado}"


class Revista(Material):
    def __init__(self, titulo,edición, periodicidad, estado="Disponible"):
        super().__init__(titulo,estado)
        self.edición=edición
        self.periodicidad=periodicidad
    
    def __str__(self):
        return f"Revista: '{self.titulo}' Ed. {self.edicion} ({self.periodicidad}) - Estado: {self.estado}"
    
class MaterialDigital(Material):
    def __init__(self,titulo,archivo,enlace,estado="disponible"):
        super().__init__(titulo)
        self.archivo=archivo
        self.enlace=enlace
#Todo lo que viene de la clase Material
    def __str__(self):
        return f"Material Digital: '{self.titulo}' (Tipo: {self.archivo}) - Enlace: {self.enlace} - Estado: {self.estado}"

# Clases de Personas
# -----------------------
class Persona:
    lista = []
    
    def __init__(self, nombre, correo, edad,rol):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.rol=rol
        Persona.lista.append(self)
    def registrar(self):
        
        Persona.lista.append(self)
        print(f"La persona {self.nombre} ha sido registrada con el correo {self.correo}, con la edad de {self.edad}")

    @classmethod
    def personas_registradas(cls):
        print("Personas registradas")
        for persona in cls.lista:
            print(f"- {persona.nombre} - {persona.correo} - {persona.edad}")

    def actualizar_datos(self, nombre, correo, edad):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        print("Los datos han sido actualizados")


class Usuario(Persona):
    def __init__(self, nombre, correo,edad):
        super().__init__(nombre, correo, edad,rol="Usuario")
        self.materiales_Prestados=[]
        self.penalizaciones = []  

    def consultar_catalogo(self, catalogo):
        materiales = catalogo.obtener_catalogo()
        print("Catálogo completo:")
        for mat in materiales:
            print(mat)

    def agregar_penalizacion(self, penalizacion):
        self.penalizaciones.append(penalizacion)
        print(f"Se ha registrado una penalización de ${penalizacion.monto} para {self.nombre}.")

class Bibliotecario(Persona):
    def __init__(self, nombre, correo, edad):
        super().__init__(nombre, correo, edad, rol="Bibliotecario")

        
    def agregar_material(self, sucursal, material):
        sucursal.agregar_material(material)
        print(f"Se ha agregado '{material.titulo}' a la sucursal {sucursal.nombre}.")

    def gestionar_prestamo(self, usuario, material, sucursal):
        if material in sucursal.catalogo and material.estado == "disponible":
            prestamo = Prestamo(usuario, material)
            usuario.materiales_prestados.append(prestamo)
            material.estado = "prestado"
            print(f"Préstamo realizado: {usuario.nombre} ha tomado '{material.titulo}'.")
            return prestamo
        else:
            print("El material no está disponible en la sucursal.")
            return None

    def transferir_material(self, material, sucursal_origen, sucursal_destino):
        if material in sucursal_origen.catalogo:
            sucursal_origen.remover_material(material)
            sucursal_destino.agregar_material(material)
            print(f"Material '{material.titulo}' transferido de {sucursal_origen.nombre} a {sucursal_destino.nombre}.")
        else:
            print("El material no se encuentra en la sucursal origen.")
#Todo lo que viene de la clase Persona
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []  # Lista de objetos Material

    def agregar_material(self, material):
        self.catalogo.append(material)

    def remover_material(self, material):
        if material in self.catalogo:
            self.catalogo.remove(material)
        else:
            print("El material no se encuentra en el catálogo de la sucursal.")

    def buscar_materiales_disponibles(self):
        return [material for material in self.catalogo if material.estado == "disponible"]


class Prestamo:
    def __init__(self, usuario, material, fecha_prestamo=None, fecha_devolucion=None):
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = fecha_prestamo or datetime.now()
        self.fecha_devolucion = fecha_devolucion  # Se asigna cuando se devuelve el material

    def devolver_material(self):
        self.fecha_devolucion = datetime.now()
        self.material.estado = "disponible"
        print(f"Material '{self.material.titulo}' devuelto por {self.usuario.nombre}.")

    def calcular_dias_retraso(self, dias_permitidos=14):
        if self.fecha_devolucion:
            dias_prestamo = (self.fecha_devolucion - self.fecha_prestamo).days
        else:
            dias_prestamo = (datetime.now() - self.fecha_prestamo).days
        retraso = dias_prestamo - dias_permitidos
        return max(retraso, 0)

class penalizacion:
    def __init__(self, usuario, monto, fecha_penalizacion=None):
        self.usuario = usuario
        self.monto = monto
        self.fecha_penalizacion = fecha_penalizacion or datetime.now()

    def __str__(self):
        fecha = self.fecha_penalizacion.strftime('%Y-%m-%d')
        return f"Penalización para {self.usuario.nombre}: ${self.monto} (Fecha: {fecha})"


class Catalogo:
    def __init__(self, sucursales):
        self.sucursales = sucursales  # Lista de objetos Sucursal

    def obtener_catalogo(self):
        catalogo_total = []
        for sucursal in self.sucursales:
            catalogo_total.extend(sucursal.catalogo)
        return catalogo_total

    def buscar_materiales(self, criterio, valor):
        resultados = []
        for sucursal in self.sucursales:
            for material in sucursal.catalogo:
                # Búsqueda en función del tipo de material y el criterio
                if isinstance(material, Libro):
                    if criterio == "autor" and material.autor == valor:
                        resultados.append(material)
                    elif criterio == "genero" and material.genero == valor:
                        resultados.append(material)
                    elif criterio == "titulo" and material.titulo == valor:
                        resultados.append(material)
                elif isinstance(material, Revista):
                    if criterio == "edicion" and material.edicion == valor:
                        resultados.append(material)
                    elif criterio == "titulo" and material.titulo == valor:
                        resultados.append(material)
                elif isinstance(material, MaterialDigital):
                    if criterio == "tipo_archivo" and material.tipo_archivo == valor:
                        resultados.append(material)
                    elif criterio == "titulo" and material.titulo == valor:
                        resultados.append(material)
        return resultados

    def buscar_materiales_disponibles(self):
        disponibles = []
        for sucursal in self.sucursales:
            disponibles.extend(sucursal.buscar_materiales_disponibles())
        return disponibles

# -----------------------
# Ejemplo de Uso
# -----------------------
if __name__ == "__main__":
    # Crear sucursales
    sucursal1 = Sucursal("Central")
    sucursal2 = Sucursal("Norte")

    # Crear algunos materiales
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela")
    revista1 = Revista("National Geographic", "2023-04", "Mensual")
    digital1 = MaterialDigital("Aprende Python", "pdf", "http://descarga.com/python.pdf")

    # Agregar materiales a sucursales
    sucursal1.agregar_material(libro1)
    sucursal1.agregar_material(revista1)
    sucursal2.agregar_material(digital1)

    # Crear Catálogo con las sucursales
    catalogo = Catalogo([sucursal1, sucursal2])

    # Crear usuarios y bibliotecarios
    usuario1 = Usuario("Ana Pérez", "ana@mail.com", 28)
    bibliotecario1 = Bibliotecario("Carlos López", "carlos@mail.com", 35)

    # Registrar personas
    usuario1.registrar()
    bibliotecario1.registrar()
    Persona.personas_registradas()

    # Usuario consulta el catálogo
    usuario1.consultar_catalogo(catalogo)

    # Bibliotecario realiza un préstamo
    prestamo1 = bibliotecario1.gestionar_prestamo(usuario1, libro1, sucursal1)

    # Simular devolución y cálculo de retraso
    if prestamo1:
        # Supongamos que pasan 16 días...
        prestamo1.fecha_prestamo -= timedelta(days=16)
        prestamo1.devolver_material()
        dias_retraso = prestamo1.calcular_dias_retraso()
        if dias_retraso > 0:
            # Se establece una penalización, por ejemplo, $1 por día de retraso
            monto = dias_retraso * 1
            penalizacion1 = penalizacion(usuario1, monto)
            usuario1.agregar_penalizacion(penalizacion1)
            print(penalizacion1)

    # Bibliotecario transfiere un material entre sucursales
    bibliotecario1.transferir_material(digital1, sucursal2, sucursal1)

    # Buscar materiales disponibles en todas las sucursales
    disponibles = catalogo.buscar_materiales_disponibles()
    print("\nMateriales disponibles en todas las sucursales:")
    for mat in disponibles:
        print(mat)

    # Búsqueda en el catálogo (por ejemplo, buscar por autor)
    resultados = catalogo.buscar_materiales("autor", "Gabriel García Márquez")
    print("\nBúsqueda por autor 'Gabriel García Márquez':")
    for r in resultados:
        print(r)