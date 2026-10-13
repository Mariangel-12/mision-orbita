# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Mariangel Marin Chinchilla
# Fecha: 13/10/2026   Versión: 1.0
# Descripción: Verifica si se autoriza el lanzamiento de la misión
#              según combustible, oxígeno, energía y provisiones.
# ============================================================

# --- Declaración de constantes ---
RESERVA_COMBUSTIBLE = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# --- Procesamiento ---
# El combustible debe cubrir ida, regreso y reserva desde el inicio
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# --- Decisión: todas las condiciones deben cumplirse a la vez ---
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")