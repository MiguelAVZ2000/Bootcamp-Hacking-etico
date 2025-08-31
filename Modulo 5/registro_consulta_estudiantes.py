# registro_consulta_estudiantes.py

def main():
    """
    Programa principal para registrar estudiantes y sus notas, y luego consultar estadísticas.
    """
    print("--- Registro y Consulta de Estudiantes ---")
    print("Ingresa 'fin' en el nombre del estudiante para terminar el registro.")
    print("------------------------------------------")

    # 2. Usa un diccionario para almacenar esta información (nombre: nota).
    estudiantes = {}

    while True:
        # 1. El programa debe permitir ingresar nombres de estudiantes y sus notas finales.
        nombre_estudiante = input("\nIngresa el nombre del estudiante (o 'fin' para terminar): ").strip()

        # 3. Finaliza la entrada cuando el usuario escriba "fin" como nombre.
        if nombre_estudiante.lower() == 'fin':
            break

        if not nombre_estudiante:
            print("El nombre del estudiante no puede estar vacío. Intenta de nuevo.")
            continue

        try:
            nota_str = input(f"Ingresa la nota final de {nombre_estudiante}: ").strip()
            nota_final = float(nota_str)

            # Opcional: Validación básica de rango de nota (ej. 0.0 a 10.0)
            if not (0.0 <= nota_final <= 10.0):
                print("Nota fuera de un rango razonable (0.0-10.0). Intenta de nuevo.")
                continue

            estudiantes[nombre_estudiante] = nota_final

        except ValueError:
            print("Entrada inválida para la nota. Por favor, ingresa un número.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    print("\n--- Resumen de Estudiantes Registrados ---")

    if not estudiantes:
        print("No se registraron estudiantes.")
        return

    cantidad_aprobados = 0
    cantidad_reprobados = 0
    suma_notas = 0.0
    nombres_aprobados = [] # Para la parte opcional

    # 4. Recorre el diccionario para:
    for nombre, nota in estudiantes.items():
        suma_notas += nota
        if nota >= 6.0: # Considerando 6.0 como nota mínima de aprobación.
            cantidad_aprobados += 1
            nombres_aprobados.append(nombre) # Opcional: Listar nombres de aprobados
        else:
            cantidad_reprobados += 1

    total_estudiantes = len(estudiantes)
    promedio_general = suma_notas / total_estudiantes

    # Mostrar cuántos estudiantes aprobaron y reprobaron.
    print(f"Total de estudiantes registrados: {total_estudiantes}")
    print(f"Estudiantes aprobados (>= 6.0): {cantidad_aprobados}")
    print(f"Estudiantes reprobados (< 6.0): {cantidad_reprobados}")
    
    # Calcular y mostrar el promedio general.
    print(f"Promedio general de notas: {promedio_general:.2f}")

    # Listar los nombres de quienes aprobaron.
    if nombres_aprobados:
        print("\nNombres de estudiantes que aprobaron:")
        for nombre in nombres_aprobados:
            print(f"- {nombre}")
    else:
        print("\nNo hay estudiantes aprobados.")

    print("------------------------------------------")

if __name__ == "__main__":
    main()