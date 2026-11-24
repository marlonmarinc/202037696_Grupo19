power_sdm = {
    "0x00": {
        "phase": "L1", 
        "data_format": "Float32", 
        "alarm_threshold": 250
    },
    "0x06": {
        "phase": "L1", 
        "data_format": "Float32", 
        "alarm_threshold": 100
    },
    "0x46": {
        "phase": "System", 
        "data_format": "Float32", 
        "alarm_threshold": 52
    }
}

def consultar_registro():
    print("==================================================")
    print("   SISTEMA DE AUDITORIA MODBUS - SDM630")
    print("==================================================")
    
    max_intentos = 3
    intentos = 0

    while intentos < max_intentos:
        print(f"\n[Intento {intentos + 1} de {max_intentos}]")
        # Normalizamos desde el inicio con .strip().lower() para evitar errores por mayúsculas
        busqueda = input("Ingrese la dirección hexadecimal (ej. 0x00) o escriba 'salir': ").strip().lower()
        
        if busqueda == 'salir':
            print("Saliendo del sistema de consulta...")
            break
            
        registro = power_sdm.get(busqueda)
        
        if registro:
            print("\n[ÉXITO] Registro encontrado:")
            print(f"  - Dirección Hex:   {busqueda}")
            print(f"  - Fase:            {registro.get('phase')}")
            print(f"  - Formato de Dato: {registro.get('data_format')}")
            print(f"  - Umbral de Alarma:{registro.get('alarm_threshold')}")
            break
        else:
            intentos += 1
            print(f"[ERROR CONTROLADO] La dirección '{busqueda}' no se encuentra en el alcance de la guía.")
            if intentos < max_intentos:
                print(f"Te quedan {max_intentos - intentos} intentos.")
            else:
                print("\n[BLOQUEO DE SEGURIDAD] Límite de intentos alcanzado.")

if __name__ == "__main__":
    consultar_registro()