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

# --- Ciclo del menú: se repite mientras la exploración pueda continuar ---
while continuar_exploracion:
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una actividad: "))

    if opcion == OPCION_FINALIZAR:
        print("Exploración finalizada por la tripulación.")
        continuar_exploracion = False
    elif opcion >= OPCION_ANALIZAR and opcion <= OPCION_OBSERVAR:
        # Primero se asignan los datos de la actividad elegida
        if opcion == OPCION_ANALIZAR:
            nombre_actividad = "Analizar terreno"
            energia_actividad = ENERGIA_ANALIZAR_TERRENO
            provisiones_actividad = PROVISIONES_ANALIZAR_TERRENO
            puntos_actividad = PUNTOS_ANALIZAR_TERRENO
        elif opcion == OPCION_RECOLECTAR:
            nombre_actividad = "Recolectar muestra"
            energia_actividad = ENERGIA_RECOLECTAR_MUESTRA
            provisiones_actividad = PROVISIONES_RECOLECTAR_MUESTRA
            puntos_actividad = PUNTOS_RECOLECTAR_MUESTRA
        else:
            nombre_actividad = "Realizar observación"
            energia_actividad = ENERGIA_OBSERVACION
            provisiones_actividad = PROVISIONES_OBSERVACION
            puntos_actividad = PUNTOS_OBSERVACION

        # Luego se verifica si alcanzan ambos recursos
        if energia_disponible >= energia_actividad and provisiones_disponibles >= provisiones_actividad:
            energia_disponible = energia_disponible - energia_actividad
            provisiones_disponibles = provisiones_disponibles - provisiones_actividad
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad
            if opcion == OPCION_RECOLECTAR:
                muestras_recolectadas = muestras_recolectadas + 1
            print("Actividad realizada:", nombre_actividad + ". Puntos obtenidos:", puntos_actividad)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuar_exploracion = False
    else:
        print("Opción no válida.")      