# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrante: Mariangel Marin Chinchilla
# Fecha: 10/10/2026   Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

# --- Declaración de constantes ---
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
OXIGENO_POR_DIA = 2
RESERVA_OXIGENO = 5
ENERGIA_POR_DIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_POR_DIA = 1
RESERVA_PROVISIONES = 3
TRAMOS_VIAJE = 2  # ida y regreso

# --- Entrada de datos ---
nombre_mision = input("Nombre de la misión: ")
tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días estimados hasta el destino: "))

# --- Procesamiento ---
combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
oxigeno_requerido = dias_viaje * TRAMOS_VIAJE * OXIGENO_POR_DIA * tripulantes + RESERVA_OXIGENO
energia_requerida = dias_viaje * ENERGIA_POR_DIA * TRAMOS_VIAJE + ENERGIA_EXPLORACION
provisiones_requeridas = dias_viaje * PROVISIONES_POR_DIA * tripulantes * TRAMOS_VIAJE + RESERVA_PROVISIONES

# --- Salida de resultados ---
print("Misión:", nombre_mision)
print("Tripulantes:", tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")