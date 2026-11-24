# Se solicita la presión al usuario para probar valores límite específicos
presion_float = float(input("Ingrese la presión inicial en Bar (ej. 1.8, 3.0, 5.0, 6.2): "))
presion = round(presion_float, 1)
print(f"Presión inicial: {presion} Bar")

# ESCENARIO 2: Control y auditoría de presión
for lectura in range(10):
    print(f"\nLectura {lectura + 1}/10 - Presión actual: {presion:.1f} Bar")

    # Evaluaciones en jerarquía estricta de seguridad
    if presion >= 6.0:
        print("CRÍTICO: Ruptura inminente. Abortando.")
        break
    elif presion < 2.0:
        print("Acción: Inyectando presión a la red")
        presion += 0.5
    elif 2.0 <= presion <= 4.5:
        print("Acción: Flujo nominal estabilizado")
        presion += 0.1
    else:
        print("Acción: Purga de emergencia abierta")
        presion -= 0.8
