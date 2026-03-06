from datetime import datetime, date
from EJERCICIO_UN1 import *

# PRUEBA MODULO PERSONAS - 1

usuario1 = Usuario(1, "Samuel", "samuel@email.com", "123456789", "1234")
usuario2 = Usuario(2, "Carlos", "carlos@email.com", "987654321", "abcd")
usuario3 = Usuario(3, "Ana", "ana@email.com", "555123456", "pass1")
usuario4 = Usuario(4, "Luis", "luis@email.com", "444987123", "pass2")
usuario5 = Usuario(5, "María", "maria@email.com", "333222111", "pass3")
usuario6 = Usuario(6, "Jorge", "jorge@email.com", "777888999", "pass4")
usuario7 = Usuario(7, "Laura", "laura@email.com", "666555444", "pass5")
usuario8 = Usuario(8, "Pedro", "pedro@email.com", "111222333", "pass6")
usuario9 = Usuario(9, "Sofía", "sofia@email.com", "999888777", "pass7")
usuario10 = Usuario(10, "Miguel", "miguel@email.com", "222333444", "pass8")

usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5,
            usuario6, usuario7, usuario8, usuario9, usuario10]

for u in usuarios:
    print(f"ID: {u.idPersona} / NOMBRE: {u.nombre} / EMAIL: {u.email} / TELEFONO: {u.telefono} / PUNTOS: {u.puntosFidelidad}")

# PRUEBA USUARIO - 2
usuario1 = Usuario(1, "Samuel", "samuel@email.com", "2221110001", "1234")
usuario2 = Usuario(2, "Carlos", "carlos@email.com", "2221110002", "abcd")
usuario3 = Usuario(3, "Ana", "ana@email.com", "2221110003", "pass1")
usuario4 = Usuario(4, "Luis", "luis@email.com", "2221110004", "pass2")
usuario5 = Usuario(5, "Maria", "maria@email.com", "2221110005", "pass3")
usuario6 = Usuario(6, "Jorge", "jorge@email.com", "2221110006", "pass4")
usuario7 = Usuario(7, "Laura", "laura@email.com", "2221110007", "pass5")
usuario8 = Usuario(8, "Pedro", "pedro@email.com", "2221110008", "pass6")
usuario9 = Usuario(9, "Sofia", "sofia@email.com", "2221110009", "pass7")
usuario10 = Usuario(10, "Miguel", "miguel@email.com", "2221110010", "pass8")

usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5,
            usuario6, usuario7, usuario8, usuario9, usuario10]

# MOSTRAR LOS DATOS (PRUEBA)
for u in usuarios:
    print(f"ID: {u.idPersona} / NOMBRE: {u.nombre} / EMAIL: {u.email} / TELEFONO: {u.telefono} / PUNTOSFIDELIDAD: {u.puntosFidelidad}")

# EMPLEADO - 3

#USUARIOS EXISTENTES
empleado1 = Empleado(usuarios[0].idPersona, usuarios[0].nombre, usuarios[0].email, usuarios[0].telefono, "1234", "E001", "taquillero", "mañana")
empleado2 = Empleado(usuarios[1].idPersona, usuarios[1].nombre, usuarios[1].email, usuarios[1].telefono, "1234", "E002", "admin", "tarde")
empleado3 = Empleado(usuarios[2].idPersona, usuarios[2].nombre, usuarios[2].email, usuarios[2].telefono, "1234", "E003", "limpieza", "noche")

#USUARIOS NUEVOS
empleado4 = Empleado(11,"Juan","juan@cine.com","5550001111","1234","E004","taquillero","mañana")
empleado5 = Empleado(12,"Diana","diana@cine.com","5550002222","1234","E005","limpieza","tarde")
empleado6 = Empleado(13,"Ricardo","ricardo@cine.com","5550003333","1234","E006","seguridad","noche")
empleado7 = Empleado(14,"Valeria","valeria@cine.com","5550004444","1234","E007","admin","mañana")
empleado8 = Empleado(15,"Fernando","fernando@cine.com","5550005555","1234","E008","dulceria","tarde")
empleado9 = Empleado(16,"Patricia","patricia@cine.com","5550006666","1234","E009","taquillero","noche")
empleado10 = Empleado(17,"Hector","hector@cine.com","5550007777","1234","E010","limpieza","mañana")

empleados = [
    empleado1, empleado2, empleado3, empleado4, empleado5,
    empleado6, empleado7, empleado8, empleado9, empleado10
]

for e in empleados:
    print(f" {e.idPersona} / {e.nombre} / {e.rol} / {e.horario} /")

# PRUEBA CLASE ESPACIO - 4

espacio1 = Espacio(1, "Sala Norte", "Planta Baja")
espacio2 = Espacio(2, "Sala Sur", "Planta Baja")
espacio3 = Espacio(3, "Sala Este", "Primer Piso")
espacio4 = Espacio(4, "Sala Oeste", "Primer Piso")
espacio5 = Espacio(5, "Lobby", "Entrada")
espacio6 = Espacio(6, "Zona Espera", "Entrada")
espacio7 = Espacio(7, "Zona VIP", "Segundo Piso")
espacio8 = Espacio(8, "Area Juegos", "Segundo Piso")
espacio9 = Espacio(9, "Area Infantil", "Segundo Piso")
espacio10 = Espacio(10, "Zona Descanso", "Primer Piso")

espacios = [espacio1, espacio2, espacio3, espacio4, espacio5,
            espacio6, espacio7, espacio8, espacio9, espacio10]

for e in espacios:
    print(f"ID: {e.idEspacio} / NOMBRE: {e.nombre} / UBICACION: {e.ubicacion} / DISPONIBLE: {e.disponible}")

# PRUEBA CLASE SALA - 5

sala1 = Sala(1, "Sala 1", "Planta Baja", "2D", 50, False)
sala2 = Sala(2, "Sala 2", "Planta Baja", "3D", 60, False)
sala3 = Sala(3, "Sala 3", "Primer Piso", "IMAX", 80, True)
sala4 = Sala(4, "Sala 4", "Primer Piso", "2D", 40, False)
sala5 = Sala(5, "Sala 5", "Segundo Piso", "3D", 55, False)
sala6 = Sala(6, "Sala 6", "Segundo Piso", "2D", 45, False)
sala7 = Sala(7, "Sala 7", "Segundo Piso", "IMAX", 90, True)
sala8 = Sala(8, "Sala 8", "Planta Baja", "2D", 50, False)
sala9 = Sala(9, "Sala 9", "Primer Piso", "3D", 60, False)
sala10 = Sala(10, "Sala 10", "Segundo Piso", "2D", 35, False)

salas = [sala1, sala2, sala3, sala4, sala5,
         sala6, sala7, sala8, sala9, sala10]

for s in salas:
    print(f"ID: {s.idEspacio} / NOMBRE: {s.nombre} / UBICACION: {s.ubicacion} / TIPO: {s.tipo} / CAPACIDAD: {s.capacidadTotal} / VIP: {s.esVip}")

# PRUEBA CLASE ZONACOMIDA - 6

zona1 = ZonaComida(1, "Dulceria Norte", "Entrada")
zona2 = ZonaComida(2, "Dulceria Sur", "Entrada")
zona3 = ZonaComida(3, "Snack Bar 1", "Primer Piso")
zona4 = ZonaComida(4, "Snack Bar 2", "Primer Piso")
zona5 = ZonaComida(5, "Area Palomitas", "Planta Baja")
zona6 = ZonaComida(6, "Area Bebidas", "Planta Baja")
zona7 = ZonaComida(7, "Zona Nachos", "Segundo Piso")
zona8 = ZonaComida(8, "Zona Helados", "Segundo Piso")
zona9 = ZonaComida(9, "Zona Combos", "Entrada")
zona10 = ZonaComida(10, "Zona Snacks", "Primer Piso")

zonas = [zona1, zona2, zona3, zona4, zona5,
         zona6, zona7, zona8, zona9, zona10]

for z in zonas:
    print(f"ID: {z.idEspacio} / NOMBRE: {z.nombre} / UBICACION: {z.ubicacion}")

# PRUEBA CLASE PELICULA - 7

pelicula1 = Pelicula("Matrix", 136, "B", "Ciencia Ficcion")
pelicula2 = Pelicula("Avatar", 162, "B", "Ciencia Ficcion")
pelicula3 = Pelicula("Toy Story", 81, "A", "Animacion")
pelicula4 = Pelicula("Titanic", 195, "B", "Romance")
pelicula5 = Pelicula("Avengers", 143, "B", "Accion")
pelicula6 = Pelicula("Joker", 122, "C", "Drama")
pelicula7 = Pelicula("Frozen", 102, "A", "Animacion")
pelicula8 = Pelicula("Batman", 176, "B", "Accion")
pelicula9 = Pelicula("Spider Man", 148, "B", "Accion")
pelicula10 = Pelicula("Interstellar", 169, "B", "Ciencia Ficcion")

peliculas = [pelicula1, pelicula2, pelicula3, pelicula4, pelicula5,
             pelicula6, pelicula7, pelicula8, pelicula9, pelicula10]

for p in peliculas:
    print(f"TITULO: {p.titulo} / DURACION: {p.duracion} / CLASIFICACION: {p.clasificacion} / GENERO: {p.genero}")

# PRUEBA FUNCIÓN - 8

funcion1 = Funcion(1, peliculas[0], salas[0], datetime(2026,3,5,16,0), 80)
funcion2 = Funcion(2, peliculas[1], salas[1], datetime(2026,3,5,18,0), 85)
funcion3 = Funcion(3, peliculas[2], salas[2], datetime(2026,3,5,20,0), 90)
funcion4 = Funcion(4, peliculas[3], salas[3], datetime(2026,3,6,16,0), 75)
funcion5 = Funcion(5, peliculas[4], salas[4], datetime(2026,3,6,18,0), 80)
funcion6 = Funcion(6, peliculas[5], salas[5], datetime(2026,3,6,20,0), 95)
funcion7 = Funcion(7, peliculas[6], salas[6], datetime(2026,3,7,16,0), 70)
funcion8 = Funcion(8, peliculas[7], salas[7], datetime(2026,3,7,18,0), 85)
funcion9 = Funcion(9, peliculas[8], salas[8], datetime(2026,3,7,20,0), 90)
funcion10 = Funcion(10, peliculas[9], salas[9], datetime(2026,3,8,18,0), 100)

funciones = [
    funcion1, funcion2, funcion3, funcion4, funcion5,
    funcion6, funcion7, funcion8, funcion9, funcion10
]

for f in funciones:
    print(
        "ID:", f.idFuncion,
        "/ PELICULA:", f.pelicula.titulo,
        "/ SALA:", f.sala.nombre,
        "/ HORARIO:", f.horarioInicio,
        "/ PRECIO:", f.precioBase,
        "/ ASIENTOS LIBRES:", f.calcularAsientosLibres())
    
# PRUEBA PROMOCIONES - 9

promo1 = Promocion("DESC10", "Descuento del 10%", 10, date(2026,12,31))
promo2 = Promocion("DESC15", "Descuento del 15%", 15, date(2026,11,30))
promo3 = Promocion("DESC20", "Descuento del 20%", 20, date(2026,10,31))
promo4 = Promocion("ESTUDIANTE", "Descuento para estudiantes", 25, date(2026,9,30))
promo5 = Promocion("VIP30", "Descuento VIP del 30%", 30, date(2026,8,31))
promo6 = Promocion("FAMILIA", "Promoción familiar", 18, date(2026,7,31))
promo7 = Promocion("MATINEE", "Descuento función matutina", 12, date(2026,6,30))
promo8 = Promocion("CINECLUB", "Descuento miembros CineClub", 22, date(2026,5,31))
promo9 = Promocion("VERANO", "Promoción de verano", 17, date(2026,4,30))
promo10 = Promocion("ESPECIAL", "Promoción especial del mes", 35, date(2026,3,31))

promociones = [
    promo1, promo2, promo3, promo4, promo5,
    promo6, promo7, promo8, promo9, promo10
]

for p in promociones:
    print(
        "CODIGO:", p.codigo,
        "/ DESCRIPCION:", p.descripcion,
        "/ DESCUENTO:", p.porcentajeDescuento,
        "/ FECHA EXPIRACION:", p.fechaExpiracion
    )

# PRUEBA RESERVA - 10

reserva1 = Reserva(1, usuarios[0], funciones[0], ["A1","A2"])
reserva2 = Reserva(2, usuarios[1], funciones[1], ["B1","B2"])
reserva3 = Reserva(3, usuarios[2], funciones[2], ["C1","C2"])
reserva4 = Reserva(4, usuarios[3], funciones[3], ["D1","D2"])
reserva5 = Reserva(5, usuarios[4], funciones[4], ["E1","E2"])
reserva6 = Reserva(6, usuarios[5], funciones[5], ["F1","F2"])
reserva7 = Reserva(7, usuarios[6], funciones[6], ["G1","G2"])
reserva8 = Reserva(8, usuarios[7], funciones[7], ["H1","H2"])
reserva9 = Reserva(9, usuarios[8], funciones[8], ["I1","I2"])
reserva10 = Reserva(10, usuarios[9], funciones[9], ["J1","J2"])

reservas = [
    reserva1, reserva2, reserva3, reserva4, reserva5,
    reserva6, reserva7, reserva8, reserva9, reserva10
]

for r in reservas:
    print(
        "ID:", r.idReserva,
        "/ USUARIO:", r.usuario.nombre,
        "/ FUNCION:", r.funcion.idFuncion,
        "/ ASIENTOS:", r.asientos,
        "/ TOTAL:", r.montoTotal,
        "/ ESTADO:", r.estado
    )

####### PRUEBA DE METODOS #######

# Crear un usuario de prueba
usuario1 = Usuario(1, "Samuel", "samuel@email.com", "123456789", "1234")

# Probar LOGIN
usuario1.login()

# Probar ACTUALIZAR DATOS
usuario1.actualizarDatos(email="samuel_nuevo@email.com")

# Probar CREAR RESERVA
reserva_simple = usuario1.crearReserva()

# Ver historial de reservas
print("Historial de reservas:", usuario1.historialReservas)

# Ver puntos de fidelidad
print("Puntos de fidelidad:", usuario1.puntosFidelidad)

# Probar CANCELAR RESERVA
usuario1.cancelarReserva(reserva_simple)

# Ver historial después de cancelar
print("Historial después de cancelar:", usuario1.historialReservas)

# Probar LOGOUT
usuario1.logout()

####### PRUEBA DE METODOS USUARIO #######

# Crear usuario de prueba
usuario1 = Usuario(11, "Samuel", "samuel@email.com", "123456789", "1234")

# LOGIN
usuario1.login()

# ACTUALIZAR DATOS
usuario1.actualizarDatos(email="samuel_nuevo@email.com")

# CREAR RESERVA
reserva_simple = usuario1.crearReserva()

print("Historial de reservas:", usuario1.historialReservas)
print("Puntos de fidelidad:", usuario1.puntosFidelidad)

# CREAR OBJETOS PARA GENERAR TICKET
from datetime import datetime

pelicula_prueba = Pelicula("Matrix", 136, "B", "Ciencia Ficcion")
sala_prueba = Sala(1, "Sala 1", "Planta Baja", "3D", 60, False)
funcion_prueba = Funcion(1, pelicula_prueba, sala_prueba, datetime(2026,3,5,18,0), 80)

# CREAR RESERVA REAL PARA TICKET
reserva_ticket = Reserva(1, usuario1, funcion_prueba, ["A1","A2"])

# GENERAR TICKET
reserva_ticket.generarTicket()

# CANCELAR RESERVA
usuario1.cancelarReserva(reserva_simple)

print("Historial después de cancelar:", usuario1.historialReservas)

# LOGOUT
usuario1.logout()

####### METODOS EMPLEADO #######

# PRUEBA DE METODOS EMPLEADO

# Crear empleado de prueba
empleado_prueba = Empleado(
    20,
    "Roberto",
    "roberto@cine.com",
    "555999111",
    "admin123",
    "E020",
    "admin",
    "mañana"
)

# LOGIN
empleado_prueba.login()

# ACTUALIZAR DATOS
empleado_prueba.actualizarDatos(telefono="555000000")

# MARCAR ENTRADA
empleado_prueba.marcarEntrada()

# GESTIONAR FUNCIONES (solo admin)
empleado_prueba.gestionarFunciones()

# LOGOUT
empleado_prueba.logout()

### RETOS VERIF ###

# Un usuario puede registrarse, iniciar sesión y gestionar su cuenta
usuarios[0].login()
usuarios[0].actualizarDatos(email="samuel_nuevo@email.com")

# Un usuario puede crear una reserva para una función
reserva_prueba = Reserva(11, usuarios[0], funciones[0], ["K1","K2"])
print("Reserva creada:", reserva_prueba.idReserva)

# El sistema calcula automáticamente el monto total según los asientos
print("Monto total:", reserva_prueba.montoTotal)

# El sistema puede aplicar promociones a una reserva
reserva_prueba.aplicarPromocion(promociones[0])
print("Monto con descuento:", reserva_prueba.montoTotal)

# Confirmar el pago de una reserva
reserva_prueba.confirmarPago()
print("Estado de la reserva:", reserva_prueba.estado)

# Generar ticket de la reserva
reserva_prueba.generarTicket()

# Consultar información de una función
print(funciones[0].obtenerDetallesFuncion())

# Calcular asientos disponibles en una función
print("Asientos disponibles:", funciones[0].calcularAsientosLibres())

# Empleados pueden interactuar con el sistema
empleados[0].marcarEntrada()
empleados[1].gestionarFunciones()

# Cerrar sesión del usuario
usuarios[0].logout()