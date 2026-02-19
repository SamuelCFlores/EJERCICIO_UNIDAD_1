# EJERCICIO 1: SISTEMA DE RESERVAS DE UN CINE

# MODULO DE PERSONAS (HERENCIA)

#PERSONA (CLASE BASE - ABSTRACTA)
#ATRIBUTOS: idPersona: int, nombre: string, Email:string, telefono: string
#METODOS: __init__(login(), logout() , actualizarDatos())
 

class Persona:

    def __init__(self, idPersona, nombre, email, telefono, contraseña):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.contraseña = contraseña
        self.logueado = False   # Estado de sesión

    def login(self):
        if self.logueado:
            print("Ya hay una sesión iniciada.")
            return

        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        if usuario == self.nombre and contraseña == self.contraseña:
            self.logueado = True
            print(f"{self.nombre} ha iniciado sesión.")
        else:
            print("Credenciales incorrectas.")

    def logout(self):
        if not self.logueado:
            print("No se puede cerrar sesión porque no hay sesión iniciada.")
        else:
            self.logueado = False
            print(f"{self.nombre} ha cerrado sesión.")

    def actualizarDatos(self, nombre=None, email=None, telefono=None, contraseña=None):
        if not self.logueado:
            print("Debe iniciar sesión para actualizar los datos.")
            return

        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono
        if contraseña:
            contraseña_filtro = input("Ingrese su contraseña actual para actualizar los datos: ")
            if contraseña_filtro == self.contraseña:
                self.contraseña = contraseña
                print("Contraseña actualizada exitosamente.")
            else:
                print("Contraseña incorrecta. No se actualizará la contraseña.")

        print(f"{self.nombre} ha actualizado sus datos.")


# USUARIO HEREDA DE PERSONA
#ATRIBUTOS: puntosFidelidad: int, historialReservas: list<reserva>
#METODOS: crearReserva(), consultarPromociones(), cancelarReserva()


class Usuario(Persona):

    def __init__(self, idPersona, nombre, email, telefono, contraseña):
        super().__init__(idPersona, nombre, email, telefono, contraseña)
        self.puntosFidelidad = 0
        self.historialReservas = []

    def crearReserva(self):
        if not self.logueado:
            print("Debe iniciar sesión para crear una reserva.")
            return None
        
        funcion = input("Ingrese la función / película: ")
        hora = input("Ingrese la hora de la función: ")
        asiento = input("Ingrese el número de asiento: ")

        reserva = {
            "funcion": funcion,
            "hora": hora,
            "asiento": asiento
        }

        self.historialReservas.append(reserva)
        self.puntosFidelidad += 10

        print(f"Reserva creada para {self.nombre}.")
        return reserva
    
    def cancelarReserva(self, reserva):
        if not self.logueado:
            print("Debe iniciar sesión para cancelar una reserva.")
            return

        if reserva in self.historialReservas:
            self.historialReservas.remove(reserva)
            self.puntosFidelidad -= 10
            print(f"Reserva cancelada para {self.nombre}.")
        else:
            print("No se encontró la reserva en el historial.")
    

# EMPLEADO HEREDA DE PERSONA
#ATRIBUTOS: idEmpleado: string, rol: Enum(Taquillero, admin, limpieza), horario: string
#METODOS: marcarEntrada(), gestionarFunciones() (solo admin)

class Empleado(Persona):

    def __init__(self, idPersona, nombre, email, telefono, contraseña, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono, contraseña)
        self.idEmpleado = idEmpleado
        self.rol = rol
        self.horario = horario
        
    def marcarEntrada(self):
        print(f"{self.nombre} ha marcado su entrada.")
        
    def gestionarFunciones(self):
        if self.rol == "admin":
            print(f"{self.nombre} está gestionando las funciones del cine.")
        else:
            print("Acceso denegado. Solo los administradores pueden gestionar funciones.")


# 2. Módulo de Infraestructura

# Espacio (Clase Base)
# Atributos: idEspacio: int, nombre: String, ubicacion: String.
# Métodos: verificarDisponibilidad(), limpiarEspacio().

class Espacio:

    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio = idEspacio
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.disponible = True

    def verificarDisponibilidad(self):
        return self.disponible

    def limpiarEspacio(self):
        self.disponible = False
        print(f"El espacio {self.nombre} ha sido retirado temporalmente del uso.")


# Sala (Hereda de Espacio)
# Atributos: tipo: Enum(2D, 3D, IMAX), capacidadTotal: int, esVip: boolean.
# Métodos: ajustarAforo(), obtenerTipoSala().

class Sala(Espacio):

    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal, esVip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo = tipo
        self.capacidadTotal = capacidadTotal
        self.esVip = esVip
        self.aforoActual = capacidadTotal

    def ajustarAforo(self, nuevoAforo):
        if nuevoAforo <= self.capacidadTotal:
            self.aforoActual = nuevoAforo
            print("Aforo ajustado correctamente.")
        else:
            print("El aforo no puede superar la capacidad total.")

    def obtenerTipoSala(self):
        return self.tipo


# ZonaComida (Hereda de Espacio)
# Atributos: listaProductos: List<Producto>, stockActual: Map<String, int>.
# Métodos: venderProducto(), actualizarInventario().

class ZonaComida(Espacio):

    def __init__(self, idEspacio, nombre, ubicacion):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos = []
        self.stockActual = {}

    def venderProducto(self, producto, cantidad):
        if producto in self.stockActual and self.stockActual[producto] >= cantidad:
            self.stockActual[producto] -= cantidad
            print("Producto vendido correctamente.")
        else:
            print("No hay suficiente stock del producto.")

    def actualizarInventario(self, producto, cantidad):
        if producto in self.stockActual:
            self.stockActual[producto] += cantidad
        else:
            self.stockActual[producto] = cantidad
        print("Inventario actualizado.")


# 3. Logica de Funciones y Peliculas

# Pelicula
# Atributos: titulo: String, duracion: int (minutos), clasificacion: String, genero: String.
# Métodos: obtenerSinopsis(), esAptaParaTodoPublico().

class Pelicula:

    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def obtenerSinopsis(self):
        return f"{self.titulo} es una película de género {self.genero} con duración de {self.duracion} minutos."

    def esAptaParaTodoPublico(self):
        return self.clasificacion.upper() == "A"

# Funcion
# Atributos: idFuncion: int, pelicula: Pelicula, sala: Sala, horarioInicio: DateTime, precioBase: float.
# Métodos: calcularAsientosLibres(), obtenerDetallesFuncion().

class Funcion:

    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion = idFuncion
        self.pelicula = pelicula
        self.sala = sala
        self.horarioInicio = horarioInicio
        self.precioBase = precioBase
        self.asientosOcupados = []

    def calcularAsientosLibres(self):
        return self.sala.aforoActual - len(self.asientosOcupados)

    def obtenerDetallesFuncion(self):
        return {
            "pelicula": self.pelicula.titulo,
            "sala": self.sala.nombre,
            "horario": self.horarioInicio,
            "precio": self.precioBase,
            "asientos_libres": self.calcularAsientosLibres()
        }

# 4. Gestion Comercial

# Promocion
# Atributos: codigo: String, descripcion: String, porcentajeDescuento: float, fechaExpiracion: Date.
# Métodos: esValida(usuario: Usuario), aplicarDescuento(monto: float).

from datetime import date

class Promocion:

    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = fechaExpiracion

    def esValida(self, usuario):
        return date.today() <= self.fechaExpiracion

    def aplicarDescuento(self, monto):
        return monto - (monto * self.porcentajeDescuento / 100)

# Reserva
# Atributos: idReserva: int, usuario: Usuario, funcion: Funcion, asientos: List<String>,
# montoTotal: float, estado: Enum (PENDIENTE, PAGADA, CANCELADA).
# Métodos: confirmarPago(), generarTicket(), aplicarPromocion(promo: Promocion).

class Reserva:

    PENDIENTE = "PENDIENTE"
    PAGADA = "PAGADA"
    CANCELADA = "CANCELADA"

    def __init__(self, idReserva, usuario, funcion, asientos):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = funcion.precioBase * len(asientos)
        self.estado = Reserva.PENDIENTE

        for asiento in asientos:
            self.funcion.asientosOcupados.append(asiento)

    def confirmarPago(self):
        self.estado = Reserva.PAGADA

    def generarTicket(self):
        print("========== TICKET ==========")
        print(f"Reserva ID: {self.idReserva}")
        print(f"Película: {self.funcion.pelicula.titulo}")
        print(f"Sala: {self.funcion.sala.nombre}")
        print(f"Asientos: {', '.join(self.asientos)}")
        print(f"Total a pagar: ${self.montoTotal}")
        print(f"Estado: {self.estado}")
        print("============================")


    def aplicarPromocion(self, promo):
        if promo.esValida(self.usuario):
            self.montoTotal = promo.aplicarDescuento(self.montoTotal)
        else:
            return None
