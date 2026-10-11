# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Mariangel Marin Chinchilla 
# Fecha: 10/10/2026   Versión: 1.0
# Descripción: Verifica si la nave tiene combustible suficiente
#              para la misión y advierte si el margen es bajo.
# ============================================================

# --- Declaración de constantes ---
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))

# --- Procesamiento ---
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# --- Salida de resultados (siempre se muestra) ---
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# --- Decisión: advertencia si el margen es bajo ---
if combustible_adicional < MARGEN_MINIMO:
    print("Advertencia: el margen adicional de combustible es bajo.")