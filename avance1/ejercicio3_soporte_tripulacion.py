# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Mariangel Marin Chinchilla
# Fecha: 12/10/2026   Versión: 1.0
# Descripción: Verifica si la nave tiene oxígeno y provisiones
#              suficientes para mantener a la tripulación.
# ============================================================

# --- Entrada de datos ---
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# --- Decisión: ambos recursos deben alcanzar (condición doble con and) ---
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")