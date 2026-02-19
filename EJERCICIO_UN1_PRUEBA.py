
from datetime import datetime, date
from EJERCICIO_UN1 import *


# PRUEBA MODULO PERSONAS 

usuario = Usuario(1, "Samuel", "samuel@email.com", "123456789", "1234")
usuario.login()

usuario.actualizarDatos(email="nuevo@email.com")
reserva_simple = usuario.crearReserva()

usuario.cancelarReserva(reserva_simple)
usuario.logout()


# PRUEBA EMPLEADO 

empleado = Empleado(2, "Carlos", "carlos@email.com", "987654321", "admin123", "EMP01", "admin", "8am-4pm")
empleado.login()
empleado.marcarEntrada()
empleado.gestionarFunciones()
empleado.logout()


# PRUEBA MODULO INFRAESTRUCTURA 

sala1 = Sala(1, "Sala 1", "Planta Baja", "2D", 50, False)
print("Disponibilidad sala:", sala1.verificarDisponibilidad())
sala1.ajustarAforo(40)

zona = ZonaComida(2, "Dulceria", "Entrada")
zona.actualizarInventario("Palomitas", 20)
zona.venderProducto("Palomitas", 2)
zona.limpiarEspacio()


# PRUEBA MODULO PELICULAS Y FUNCIONES 

pelicula = Pelicula("Matrix", 136, "B", "Ciencia Ficción")
print(pelicula.obtenerSinopsis())
print("Apta para todo público:", pelicula.esAptaParaTodoPublico())

funcion = Funcion(
    1,
    pelicula,
    sala1,
    datetime.now(),
    80.0
)

print(funcion.obtenerDetallesFuncion())



# PRUEBA MODULO GESTION COMERCIAL 

promo = Promocion("DESC10", "Descuento del 10%", 10, date(2030, 1, 1))

reserva = Reserva(
    1,
    usuario,
    funcion,
    ["A1", "A2"]
)

print("Asientos libres:", funcion.calcularAsientosLibres())

reserva.aplicarPromocion(promo)
reserva.confirmarPago()
reserva.generarTicket()
