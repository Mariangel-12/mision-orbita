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

# ============================================================
# COMPONENTE B: Viaje de ida
# ============================================================

# Consumo de un día de viaje, en el orden de RECURSOS
def calcular_consumo_diario(tripulantes):
    consumo_combustible = CONSUMO_COMBUSTIBLE_DIA
    consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA
    consumo_energia = CONSUMO_ENERGIA_DIA
    consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA
    consumo = [consumo_combustible, consumo_oxigeno, consumo_energia, consumo_provisiones]
    return consumo


# Resta a cada recurso su consumo diario multiplicado por los días del viaje.
# Como la misión ya fue autorizada, los recursos siempre alcanzan.
def viajar_al_destino(recursos, dias_viaje, tripulantes):
    consumo = calcular_consumo_diario(tripulantes)
    for posicion in range(len(RECURSOS)):
        recursos[posicion] = recursos[posicion] - consumo[posicion] * dias_viaje
    return recursos


# Devuelve True solo si cada recurso cubre el consumo de un día
def recursos_alcanzan(recursos, consumo):
    alcanzan = True
    for posicion in range(len(RECURSOS)):
        if recursos[posicion] < consumo[posicion]:
            alcanzan = False
    return alcanzan


# Simula el trayecto día a día. Se detiene si algún recurso no alcanza
# y devuelve los días completados. Los mensajes de llegada o interrupción
# los muestra la función que la llama.
def simular_trayecto(recursos, dias, tripulantes):
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True

    while dias_completados < dias and puede_continuar:
        if recursos_alcanzan(recursos, consumo):
            for posicion in range(len(RECURSOS)):
                recursos[posicion] = recursos[posicion] - consumo[posicion]
            dias_completados = dias_completados + 1
            print("Día " + str(dias_completados)
                  + " | Combustible: " + str(recursos[COMBUSTIBLE])
                  + " | Oxígeno: " + str(recursos[OXIGENO])
                  + " | Energía: " + str(recursos[ENERGIA])
                  + " | Provisiones: " + str(recursos[PROVISIONES]))
        else:
            # No se descuenta nada ese día y el ciclo termina por su condición
            puede_continuar = False

    return dias_completados


# Muestra la cantidad restante de cada recurso
def mostrar_recursos(recursos):
    print("Recursos restantes:")
    for posicion in range(len(RECURSOS)):
        print("- " + RECURSOS[posicion].capitalize() + ": " + str(recursos[posicion]) + " unidades")

# ============================================================
# COMPONENTE C: Exploración con bitácora
# ============================================================

# Muestra las actividades numeradas y, al final, la opción para finalizar
def mostrar_menu_actividades():
    numero = 1
    for actividad in ACTIVIDADES:
        print(str(numero) + ". " + actividad[ACT_NOMBRE])
        numero = numero + 1
    print(str(len(ACTIVIDADES) + 1) + ". Finalizar exploración")


# Cuenta cuántas veces aparece una actividad en la bitácora
def contar_actividad(bitacora, nombre_actividad):
    contador = 0
    for fila in bitacora:
        if fila[BIT_ACTIVIDAD] == nombre_actividad:
            contador = contador + 1
    return contador


# Suma los puntos de todas las filas de la bitácora
def calcular_puntos(bitacora):
    total_puntos = 0
    for fila in bitacora:
        total_puntos = total_puntos + fila[BIT_PUNTOS]
    return total_puntos


# Repite el menú de actividades hasta que la tripulación finalice o falten recursos.
# Modifica la lista recursos y devuelve la bitácora de actividades realizadas.
def explorar(recursos):
    print("=== EXPLORACIÓN ===")
    bitacora = []
    opcion_finalizar = len(ACTIVIDADES) + 1
    continuar_exploracion = True

    while continuar_exploracion:
        mostrar_menu_actividades()
        opcion = int(input("Seleccione una actividad: "))

        if opcion == opcion_finalizar:
            print("Exploración finalizada por la tripulación.")
            continuar_exploracion = False
        elif opcion >= 1 and opcion <= len(ACTIVIDADES):
            actividad = ACTIVIDADES[opcion - 1]
            # Se verifica que alcancen los tres recursos que consume la actividad
            if (recursos[COMBUSTIBLE] >= actividad[ACT_COMBUSTIBLE]
                    and recursos[ENERGIA] >= actividad[ACT_ENERGIA]
                    and recursos[PROVISIONES] >= actividad[ACT_PROVISIONES]):
                recursos[COMBUSTIBLE] = recursos[COMBUSTIBLE] - actividad[ACT_COMBUSTIBLE]
                recursos[ENERGIA] = recursos[ENERGIA] - actividad[ACT_ENERGIA]
                recursos[PROVISIONES] = recursos[PROVISIONES] - actividad[ACT_PROVISIONES]
                # El número de la fila es la posición en que se realizó la actividad
                bitacora.append([len(bitacora) + 1, actividad[ACT_NOMBRE], actividad[ACT_PUNTOS]])
                print("Actividad realizada: " + actividad[ACT_NOMBRE]
                      + ". Puntos obtenidos: " + str(actividad[ACT_PUNTOS]))
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                continuar_exploracion = False
        else:
            print("Opción no válida.")

    return bitacora


# Muestra el resumen de la exploración y los recursos que quedan
def mostrar_resumen_exploracion(bitacora, recursos):
    print("Actividades realizadas:", len(bitacora))
    print("Muestras recolectadas:", contar_actividad(bitacora, "Recolectar muestra"))
    print("Puntos científicos:", calcular_puntos(bitacora))
    mostrar_recursos(recursos)

# ============================================================
# COMPONENTE D: Regreso y supervivencia
# ============================================================

# Hay combustible para volver si alcanza para los días de viaje (sin la reserva de 10)
def puede_regresar(recursos, dias_viaje):
    combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    alcanza = recursos[COMBUSTIBLE] >= combustible_regreso
    return alcanza


# Días completos que resiste cada recurso vital, en el orden de RECURSOS_VITALES
def calcular_supervivencia(recursos, tripulantes):
    consumo = calcular_consumo_diario(tripulantes)
    dias_oxigeno = recursos[OXIGENO] // consumo[OXIGENO]
    dias_energia = recursos[ENERGIA] // consumo[ENERGIA]
    dias_provisiones = recursos[PROVISIONES] // consumo[PROVISIONES]
    dias_por_recurso = [dias_oxigeno, dias_energia, dias_provisiones]
    return dias_por_recurso


# Devuelve los nombres de los recursos cuyo valor es igual al mínimo (puede haber empate)
def obtener_limitantes(dias_por_recurso, minimo):
    limitantes = []
    for posicion in range(len(RECURSOS_VITALES)):
        if dias_por_recurso[posicion] == minimo:
            limitantes.append(RECURSOS_VITALES[posicion])
    return limitantes


# Evalúa el regreso: si hay combustible simula el viaje, si no, calcula la supervivencia.
# Devuelve el resultado de la misión como texto.
def regresar(recursos, dias_viaje, tripulantes):
    print("=== REGRESO ===")

    if puede_regresar(recursos, dias_viaje):
        # Caso A: la nave inicia el regreso
        dias_completados = simular_trayecto(recursos, dias_viaje, tripulantes)
        if dias_completados == dias_viaje:
            print("La tripulación regresó exitosamente a la Tierra.")
            mostrar_recursos(recursos)
            resultado = RESULTADOS[0]
        else:
            print("El regreso se interrumpió en el día " + str(dias_completados + 1) + ".")
            # El combustible nunca aparece aquí porque puede_regresar ya verificó que alcanza
            consumo = calcular_consumo_diario(tripulantes)
            for posicion in range(len(RECURSOS)):
                if recursos[posicion] < consumo[posicion]:
                    print("Recurso insuficiente: " + RECURSOS[posicion])
            print("La tripulación no completó el regreso.")
            resultado = RESULTADOS[1]
    else:
        # Caso B: tripulación varada, se estima cuántos días puede sobrevivir
        print("La tripulación quedó varada en el destino.")
        dias_por_recurso = calcular_supervivencia(recursos, tripulantes)
        for posicion in range(len(RECURSOS_VITALES)):
            print("Días por " + RECURSOS_VITALES[posicion] + ": " + str(dias_por_recurso[posicion]))
        minimo = min(dias_por_recurso)
        limitantes = obtener_limitantes(dias_por_recurso, minimo)
        print("Supervivencia estimada: " + str(minimo) + " días")
        print("Recurso(s) limitante(s): " + ", ".join(limitantes))
        resultado = RESULTADOS[2]

    return resultado

# Prueba temporal del componente D (se reemplaza al terminar el sistema)
def main():
    resultado = regresar([46, 18, 18, 8], 3, 2)
    print("Resultado:", resultado)

    resultado = regresar([46, 18, 10, 8], 3, 2)
    print("Resultado:", resultado)

    resultado = regresar([16, 18, 24, 10], 3, 2)
    print("Resultado:", resultado)


main()