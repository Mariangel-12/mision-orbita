# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV 3
# Integrantes: Mariangel Marin Chinchilla 
# Fecha: 04/11/2026   Versión: 1.0
# Descripción: Evalúa el regreso a la Tierra o la supervivencia
#              de la tripulación si queda varada en el destino.
# ============================================================

# --- Declaración de constantes ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# --- Entrada de datos ---
tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje_ida = int(input("Días del viaje de ida: "))
combustible_disponible = int(input("Combustible disponible: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
energia_disponible = int(input("Energía disponible: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))

# --- Procesamiento: necesidades del regreso y consumos diarios ---
# En este ejercicio no se suma la reserva de emergencia de combustible
combustible_regreso = dias_viaje_ida * CONSUMO_COMBUSTIBLE_DIA
consumo_oxigeno_dia = tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA
consumo_provisiones_dia = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA

# --- Decisión: ¿hay combustible para iniciar el regreso? ---
if combustible_disponible >= combustible_regreso:
    # --- Caso A: la nave inicia el regreso y se simula día a día ---
    dias_completados = 0
    regreso_continua = True

    while dias_completados < dias_viaje_ida and regreso_continua:
        # Se verifica, antes de consumir, que los cuatro recursos alcancen
        if (combustible_disponible >= CONSUMO_COMBUSTIBLE_DIA
                and oxigeno_disponible >= consumo_oxigeno_dia
                and energia_disponible >= CONSUMO_ENERGIA_DIA
                and provisiones_disponibles >= consumo_provisiones_dia):
            combustible_disponible = combustible_disponible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno_disponible = oxigeno_disponible - consumo_oxigeno_dia
            energia_disponible = energia_disponible - CONSUMO_ENERGIA_DIA
            provisiones_disponibles = provisiones_disponibles - consumo_provisiones_dia
            dias_completados = dias_completados + 1
            print("Día", dias_completados, "| Combustible:", combustible_disponible,
                  "| Oxígeno:", oxigeno_disponible, "| Energía:", energia_disponible,
                  "| Provisiones:", provisiones_disponibles)
        else:
            # No se descuenta nada ese día y el ciclo termina por su condición
            regreso_continua = False

    # --- Resultado del regreso ---
    if dias_completados == dias_viaje_ida:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible_disponible, "unidades")
        print("Oxígeno restante:", oxigeno_disponible, "unidades")
        print("Energía restante:", energia_disponible, "unidades")
        print("Provisiones restantes:", provisiones_disponibles, "unidades")
    else:
        print("El regreso se interrumpió en el día " + str(dias_completados + 1) + ".")
        # El combustible siempre alcanza (se verificó al inicio), por eso no se evalúa
        if oxigeno_disponible < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxígeno")
        if energia_disponible < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")
        if provisiones_disponibles < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")
        print("La tripulación no completó el regreso.")
else:
    # --- Caso B: tripulación varada, se estima la supervivencia ---
    print("La tripulación quedó varada en el destino.")

    # Días completos que resiste cada recurso (división entera)
    dias_oxigeno = oxigeno_disponible // consumo_oxigeno_dia
    dias_energia = energia_disponible // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones_disponibles // consumo_provisiones_dia
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)

    # El menor valor se obtiene con condicionales (no se permite min())
    supervivencia_dias = dias_oxigeno
    if dias_energia < supervivencia_dias:
        supervivencia_dias = dias_energia
    if dias_provisiones < supervivencia_dias:
        supervivencia_dias = dias_provisiones

    # Se arma la lista de recursos limitantes, con coma entre ellos si hay empate
    recurso_limitante = ""
    separador = ""
    if dias_oxigeno == supervivencia_dias:
        recurso_limitante = recurso_limitante + separador + "oxígeno"
        separador = ", "
    if dias_energia == supervivencia_dias:
        recurso_limitante = recurso_limitante + separador + "energía"
        separador = ", "
    if dias_provisiones == supervivencia_dias:
        recurso_limitante = recurso_limitante + separador + "provisiones"

    print("Supervivencia estimada:", supervivencia_dias, "días")
    print("Recurso(s) limitante(s):", recurso_limitante)