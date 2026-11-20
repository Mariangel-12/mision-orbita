# ============================================================
# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrante: Mariangel Marin Chinchilla
# Fecha: 18/11/2026   Versión: 1.0
# Descripción: Sistema integrado Misión Órbita.
# ============================================================

# --- Declaración de constantes: datos fijos del sistema ---
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))

# Cada actividad: (nombre, combustible, energía, provisiones, puntos)
ACTIVIDADES = (("Analizar terreno", 0, 8, 0, 10),
               ("Recolectar muestra", 0, 12, 2, 20),
               ("Realizar observación", 0, 5, 0, 8),
               ("Sobrevolar la zona", 15, 3, 0, 25))

RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")
RESULTADOS = ("Regreso exitoso", "Regreso interrumpido", "Tripulación varada",
              "No autorizada", "No planificada")

# Columnas de DESTINOS: (nombre, dias)
DES_NOMBRE = 0
DES_DIAS = 1

# Columnas de ACTIVIDADES: (nombre, combustible, energía, provisiones, puntos)
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4

# Posición de cada recurso en las listas recursos, requeridos y consumo
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3

# Columnas de la matriz bitacora: [numero, actividad, puntos]
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2

# Columnas de la matriz historial: [numero, nombre, destino, resultado, puntos]
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# --- Constantes numéricas de las fórmulas (los nombres los decide el grupo) ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
TRAMOS_VIAJE = 2
RESERVA_COMBUSTIBLE = 10
RESERVA_OXIGENO = 5
ENERGIA_EXPLORACION = 10
RESERVA_PROVISIONES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10

# --- Opciones del menú principal ---
OPCION_PLANIFICAR = 1
OPCION_HISTORIAL = 2
OPCION_SALIR = 3

# ============================================================
# COMPONENTE A: Preparación y autorización
# ============================================================

# Muestra los destinos numerados a partir de 1, recorriendo la tupla DESTINOS
def mostrar_destinos():
    print("Destinos disponibles:")
    numero = 1
    for destino in DESTINOS:
        print(str(numero) + ". " + destino[DES_NOMBRE] + " (" + str(destino[DES_DIAS]) + " días)")
        numero = numero + 1


# Pide la cantidad disponible de cada recurso, en el orden de RECURSOS
def leer_recursos():
    recursos = []
    for recurso in RECURSOS:
        cantidad = int(input("Cantidad disponible de " + recurso + ": "))
        recursos.append(cantidad)
    return recursos


# Calcula lo que la misión necesita para ida, regreso y reservas
def calcular_requeridos(dias_viaje, tripulantes):
    combustible_requerido = dias_viaje * CONSUMO_COMBUSTIBLE_DIA * TRAMOS_VIAJE + RESERVA_COMBUSTIBLE
    oxigeno_requerido = (dias_viaje * CONSUMO_OXIGENO_TRIPULANTE_DIA * TRAMOS_VIAJE
                         * tripulantes + RESERVA_OXIGENO)
    energia_requerida = dias_viaje * CONSUMO_ENERGIA_DIA * TRAMOS_VIAJE + ENERGIA_EXPLORACION
    provisiones_requeridas = (dias_viaje * CONSUMO_PROVISIONES_TRIPULANTE_DIA * tripulantes
                              * TRAMOS_VIAJE + RESERVA_PROVISIONES)
    requeridos = [combustible_requerido, oxigeno_requerido, energia_requerida, provisiones_requeridas]
    return requeridos


# Muestra el resumen de la misión y advierte si el margen de combustible es bajo
def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes, disponibles, requeridos):
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Tripulantes:", tripulantes)

    posicion = 0
    for recurso in RECURSOS:
        print(recurso.capitalize() + ": disponible " + str(disponibles[posicion])
              + " | requerido " + str(requeridos[posicion]))
        posicion = posicion + 1

    margen = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]
    print("Margen adicional de combustible:", margen, "unidades")
    if margen < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


# Devuelve True solo si cada recurso disponible cubre su requerido
def autorizar_lanzamiento(disponibles, requeridos):
    autorizado = True
    for posicion in range(len(RECURSOS)):
        if disponibles[posicion] < requeridos[posicion]:
            autorizado = False
    return autorizado

# Prueba temporal del componente A (se reemplaza al terminar el sistema)
def main():
    mostrar_destinos()
    recursos = leer_recursos()
    requeridos = calcular_requeridos(3, 2)
    mostrar_resumen("Explorador I", "Luna", 3, 2, recursos, requeridos)
    print(autorizar_lanzamiento(recursos, requeridos))


main()