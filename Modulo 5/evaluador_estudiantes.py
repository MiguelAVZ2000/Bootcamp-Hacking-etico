# evaluador_estudiantes.py

def evaluar_estudiante(nombre, promedio):
    """
    Evalúa si un estudiante aprobó o reprobó basado en su promedio.
    Nota mínima de aprobación: 6.0

    Args:
        nombre (str): El nombre del estudiante.
        promedio (float): El promedio final del estudiante.

    Returns:
        bool: True si el estudiante aprobó, False si reprobó.
    """
    if promedio >= 6.0:
        print(f"{nombre} ha APROBADO con un promedio de {promedio:.2f}.")
        return True
    else:
        print(f"{nombre} ha REPROBADO con un promedio de {promedio:.2f}.")
        return False

def main():
    """
    Programa principal para ingresar y evaluar estudiantes.
    """
    print("--- Evaluador de Estudiantes ---")
    print("Ingresa 'fin' en el nombre del estudiante para terminar y ver el resumen.")
    print("--------------------------------")

    total_estudiantes_evaluados = 0
    cantidad_aprobados = 0
    cantidad_reprobados = 0

    while True:
        nombre_estudiante = input("\nIngresa el nombre del estudiante (o 'fin' para salir): ").strip()

        if nombre_estudiante.lower() == 'fin':
            break

        if not nombre_estudiante:
            print("El nombre del estudiante no puede estar vacío. Intenta de nuevo.")
            continue

        try:
            promedio_str = input(f"Ingresa el promedio final de {nombre_estudiante}: ").strip()
            promedio_final = float(promedio_str)

            if not (0.0 <= promedio_final <= 10.0): # Asumiendo notas de 0 a 10
                print("Promedio fuera de un rango razonable (0.0-10.0). Intenta de nuevo.")
                continue

            total_estudiantes_evaluados += 1
            
            # Llamar a la función evaluar_estudiante y actualizar contadores
            if evaluar_estudiante(nombre_estudiante, promedio_final):
                cantidad_aprobados += 1
            else:
                cantidad_reprobados += 1

        except ValueError:
            print("Entrada inválida para el promedio. Por favor, ingresa un número.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    print("\n--- Resumen Final ---")
    print(f"Total de estudiantes evaluados: {total_estudiantes_evaluados}")
    print(f"Cantidad de aprobados: {cantidad_aprobados}")
    print(f"Cantidad de reprobados: {cantidad_reprobados}")
    print("---------------------")

if __name__ == "__main__":
    main()