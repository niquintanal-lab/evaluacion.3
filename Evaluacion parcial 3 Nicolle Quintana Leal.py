# Evalucion parcial 3. Nicolle Quinatana
# Sistema Rápido de Trazabilidad de Muestras de Laboratorio
muestras_lab = []

# 1. Registro de datos
while True:
    print("\n--- Bienvenido al sistema de trazabilidad de muestras---")
    print("\n--- MENU ---")
    print("1. Registrar nueva muestra")
    print("2. Buscar y gestionar muestra")
    print("3. Salir")
    
    opcion = input("Seleccione una opcion: ").strip()
    
    # 2. Registro de muestra nueva
    if opcion == "1":
        codigo = input("Código de la muestra: ").strip().upper()
        paciente = input("Nombre del paciente: ").strip()
        temperatura = float(input("Temperatura (°C): "))
        
        # 3. Estado en la cadena de frio 
        if temperatura < 2 or temperatura > 8:
            estado = "RECHAZADA"
        else:
            estado = "PENDIENTE"
            
        # 4. Formateo de la linea 
        nueva_muestra = f"{codigo} - {paciente} - {estado}"
        muestras_lab.append(nueva_muestra)
        print("Muestra registrada con éxito")
        
    # 5. Gestion de la muestra 
    elif opcion == "2":
        codigo_buscar = input("Código a buscar: ").strip().upper()
        
        encontrado = False
        for i in range(len(muestras_lab)):
            partes = muestras_lab[i].split(" - ")
            
            if partes[0] == codigo_buscar:
                encontrado = True
                print(f"Muestra encontrada: {muestras_lab[i]}")
                
                print("a) Actualizar estado")
                print("b) Desechar muestra")
                accion = input("Seleccione acción: ").strip().lower()
                
                if accion == "a":
                    nuevo_estado = input("Nuevo estado: ").strip().upper()

                    # 5.1 Modificacion 
                    muestras_lab[i] = f"{partes[0]} - {partes[1]} - {nuevo_estado}"
                    print("Estado actualizado")
                    
                elif accion == "b":

                    # 5.2 Eliminacion 
                    muestras_lab.remove(muestras_lab[i])
                    print("Muestra eliminada")
                break
                
        if not encontrado:
            print("El código no existe")
            
    # 6 fin y salida del programa
    elif opcion == "3":
        print("Saliendo del programa")
        break
        
    else:
        print("Opción no válida")