class Persona:

    lista=[]
    
    def __init__(self,nombre,correo,edad):
        self.nombre=nombre
        self.correo=correo
        self.edad=edad

    def registrar(self):
        Persona.lista.append(self)
        print(f"La persona {self.nombre} ha sido registrada con el correo {self.correo}, con la edad de {self.edad}")

    def actualizar_datos(self,nombre,correo,edad):
        self.nombre=nombre
        self.correo=correo
        self.edad=edad
        print(f"Los datos han sido actualizados")

    #Metodo clase
    def personas_registradas(cls):
        print("Personas registradas")
        for Persona in cls.lista:
            print(f"-{Persona.nombre} - {Persona.correo} - {Persona.edad}")

class Usuario(Persona):
    def __init__(self, nombre, correo,edad):
        super().__init__(nombre, correo,edad)
        self.reservashistorial = []

    def reservar(self, funcion, asientos):
        if asientos <= funcion.asientos_disponibles:
            funcion.asientos_disponibles -= asientos
            self.reservashistorial.append({"funcion": funcion, "asientos": asientos})
            print(f"Reserva realizada para '{funcion.pelicula.titulo}' en la sala {funcion.sala.identificador} con {asientos} asientos.")
        else:
            print("No hay suficientes asientos disponibles.")

    def cancelar_reserva(self, funcion):
        reserva = next((r for r in self.reservashistorial if r["funcion"] == funcion), None)
        if reserva:
            funcion.asientos_disponibles += reserva["asientos"]
            self.reservashistorial.remove(reserva)
            print(f"Reserva cancelada para '{funcion.pelicula.titulo}'.")
        else:
            print("No tienes una reserva para esta función.")

class Empleado(Persona):
    def __init__(self, nombre, correo, edad, rol):
        super().__init__(nombre, correo,edad)
        self.rol = rol

    def agregar_funcion(self, funcion):
        if self.rol in ["Taquillero", "Gerente"]:
            print(f"Función agregada: {funcion.pelicula.titulo} a las {funcion.hora} en la sala {funcion.sala.identificador}, con la clasificación {funcion.pelicula.clasificacion}.")
        else:
            print("No tienes permisos para agregar funciones.")

    def modificar_promocion(self, promocion, nuevo_descuento, nuevas_condiciones):
        if self.rol in ["Taquillero", "Gerente"]:
            promocion.descuento = nuevo_descuento
            promocion.condiciones = nuevas_condiciones
            print(f"Promoción modificada: {promocion.descuento} de descuento en {promocion.condiciones}.")
        else:
            print("No tienes permisos para modificar promociones.")

class Espacio:
    def __init__(self,capacidad,identificador):
        self.capacidad=capacidad
        self.identificador=identificador
    
    def descripcion(self):
        print(f"El edificio tiene tamaño {self.capacidad} y tiene id {self.identificador}")

class Sala(Espacio):
    def __init__(self,capacidad,identificador,tipo):
        super().__init__(capacidad,identificador)
        self.tipo=tipo
        self.disponibilidad=True

    def Consultardisponibilidad(self):
        if self.disponibilidad:
            print("La sala esta disponible")
        else:
            print("La sala esta ocupada")

class ZonaComida(Espacio):
    def __init__(self,productos,precios,cantidad):
        self.productos=productos
        self.precios=precios
        self.cantidad=cantidad

    def mostrarproductos(self):
        print("\nMenu Cine\n")
        for producto,precio,cantidad in zip(self.productos,self.precios,self.cantidad):
            print (f"{producto} - {precio}$ - {cantidad} cantidad")
    
    def AgregarProducto(self,producto,precio,cantidad):
        #append Agregar un elemento al final de la lista
        self.productos.append(producto)
        self.precios.append(precio)
        self.cantidad.append(cantidad)
    
    def EliminarProducto(self,producto):
        #index Devuelve el índice en el que aparece un valor en la lista
        indice=self.productos.index(producto)
        self.productos.pop(indice)
        self.precios.pop(indice)
        self.cantidad.pop(indice)
        #pop Elimina un elemento de la lista en la posición que le indiquemos por parámetro 
        print("Producto eliminado")
    
    def Venta(self, producto, CantidadPro):
        if producto in self.productos:
            indice = self.productos.index(producto)
            if self.cantidad[indice] >= CantidadPro:
                self.cantidad[indice] -= CantidadPro
                print(f"Venta realizada: {CantidadPro} unidades de {producto}.")
            else:
                print(f"No hay suficiente producto de {producto}. Disponible: {self.cantidad[indice]}")
        else:
            print("El producto no existe en el menu.")

class Pelicula:
    def __init__(self, titulo, genero, duracion,clasificacion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.clasificacion = clasificacion
    
    def descripcion(self):
        print(f"La pelicula {self.titulo} es de genero {self.genero} con una duracion de {self.duracion} y clasificacion {self.clasificacion}")

class Funcion:
    def __init__(self, pelicula, sala, hora, asientos_disponibles=None):
        self.pelicula = pelicula
        self.sala = sala
        self.hora = hora
        self.asientos_disponibles = asientos_disponibles or sala.capacidad
    
    def Asientos_disponibles(self):
        print(f"La cantidad de asientos disponibles para la función de '{self.pelicula.titulo}' es de {self.asientos_disponibles}")

class Promocion:
    def __init__(self, descuento, condiciones):
        self.descuento = descuento
        self.condiciones = condiciones

    def mostrar(self):
        print(f"Promoción: {self.descuento}% de descuento. Condiciones: {self.condiciones}")
    
#Pruebas
#Creamos peliculas
Pelicul1=Pelicula("La ouija","Terror",120,"A")
Pelicul2=Pelicula("Los increibles","Animada",120,"B")
#Creamos salas donde se van a transmitir
sala1=Sala(100,"001","Normal")
sala2=Sala(50,"002","VIP")
#Funciones que se van a dar
funcion1=Funcion(Pelicul1,sala1,"12:00 pm")
funcion2=Funcion(Pelicul2,sala2,"3:00 pm")
#Personas 
Persona1=Usuario("Luz","Luz.com",20)
empleado1 = Empleado("Luis Martínez", "luis.martinez@email.com",28, "Taquillero")
empleado2 = Empleado("Fofo", "Fofo.martinez@email.com",28, "Conserje")
#Registro de personas
Persona1.registrar()
empleado1.registrar()
empleado2.registrar()

#Opcion 1 asientos disponibles
funcion1.Asientos_disponibles()
Persona1.reservar(funcion1,10)
funcion1.Asientos_disponibles()
Persona1.cancelar_reserva(funcion1)
funcion1.Asientos_disponibles()

#Opcion 2 asientos excedidos
funcion1.Asientos_disponibles()
Persona1.reservar(funcion1,130)

#Situacion 1. Agrega pelicula personal de Taquilla
funcion3 = Funcion(Pelicul1, sala1, "8:00 pm")
empleado1.agregar_funcion(funcion3)

#Situacion 2. Agrega pelicula personal de Limpieza
funcion4 = Funcion(Pelicul1, sala1, "10:00 pm")
empleado2.agregar_funcion(funcion4)

#Sutuacion 1. Agregar Promociones
promocion1=Promocion(20,"Valido de sabado a domingo")
promocion1.mostrar()
empleado1.modificar_promocion(promocion1, 30, "Válido todos los días antes de las 5 PM.")
promocion1.mostrar()

#Sutuacion 2. Agregar Promociones por empleado 2
empleado2.modificar_promocion(promocion1, 50, "Válido todos los días antes de las 5 PM.")
promocion1.mostrar()

zona=ZonaComida(["Pizza", "Gaseosa", "Popcorn"], [5, 2, 3], [10, 20, 15])
zona.mostrarproductos()
zona.Venta("Pizza", 3)
zona.mostrarproductos()
zona.Venta("Pizza", 8)  # Intento de venta superior al stock
zona.Venta("Helado", 2)  # Producto inexistente


pelicula1 = Pelicula("Matrix", "Ciencia Ficción", 136, "B")
pelicula2 = Pelicula("Titanic", "Drama/Romance", 195, "A")

pelicula1.descripcion()

sala1 = Sala(100,"Sala 1","3DX")
sala2 = Sala(50,"Sala 2","Tradicional")

funcion1 = Funcion(pelicula1, sala1, "18:00",50)
funcion2 = Funcion(pelicula2, sala2, "20:00", 50)

usuario1 = Usuario("Ana Pérez", "ana.perez@email.com", 25)
empleado1 = Empleado("Luis Martínez", "luis.martinez@email.com",28, "Taquillero")

usuario1.registrar()
empleado1.registrar()

Funcion.Asientos_disponibles(funcion1)
usuario1.reservar(funcion1,2)
Funcion.Asientos_disponibles(funcion1)

usuario1.cancelar_reserva(funcion1)
Funcion.Asientos_disponibles(funcion1)
promocion1 = Promocion(20, "Válido de lunes a jueves.")
promocion1.mostrar()
empleado1.modificar_promocion(promocion1, 30, "Válido todos los días antes de las 5 PM.")