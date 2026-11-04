# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV 3
# Integrantes: Mariangel Marin Chinchilla 
# Fecha: 03/11/2026   Versión: 1.0
# Descripción: Simula las actividades de exploración científica
#              en el destino mediante un menú que se repite.
# ============================================================
# --- Declaración de constantes ---
# Opciones del menú
OPCION_ANALIZAR = 1
OPCION_RECOLECTAR = 2
OPCION_OBSERVAR = 3
OPCION_FINALIZAR = 4

# Consumo y puntos de cada actividad, según la tabla del enunciado
ENERGIA_ANALIZAR_TERRENO = 8
PROVISIONES_ANALIZAR_TERRENO = 0
PUNTOS_ANALIZAR_TERRENO = 10
ENERGIA_RECOLECTAR_MUESTRA = 12
PROVISIONES_RECOLECTAR_MUESTRA = 2
PUNTOS_RECOLECTAR_MUESTRA = 20
ENERGIA_OBSERVACION = 5
PROVISIONES_OBSERVACION = 0
PUNTOS_OBSERVACION = 8

# --- Entrada de datos ---
energia_disponible = int(input("Energía disponible al llegar al destino: "))
provisiones_disponibles = int(input("Provisiones disponibles al llegar al destino: "))

# --- Inicialización de contadores, acumulador y variable de control ---
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
continuar_exploracion = True