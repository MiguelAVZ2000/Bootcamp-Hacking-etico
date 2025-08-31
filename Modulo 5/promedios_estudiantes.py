# promedios_estudiantes.py

def calcular_promedios():
    """
    Permite al usuario ingresar notas de estudiantes, calcula el promedio general
    y cuenta aprobados y reprobados.
    """
    print("--- Calculadora de Promedios de Estudiantes ---")
    print("Escribe 'fin' en cualquier momento para terminar el programa y ver los resultados.")
    print("---------------------------------------------")
    total_notas_ingresadas = 0
    suma_total_notas = 0.0
    cantidad_aprobados = 0
    cantidad_reprobados = 0
    while True:
        entrada_nota = input(f"Ingresa la nota del estudiante #{total_notas_ingresadas + 1} (o 'fin' para salir): ")
        # 3. Usar un bucle while para permitir el ingreso repetido de notas.
        # 6. Cuando el usuario escriba fin, el programa debe finalizar el bucle.
        if entrada_nota.lower() == 'fin':
            break
        try:
            # 4. Cada nota debe convertirse a float.
            nota = float(entrada_nota)
            # Opcional: Validación básica de rango de nota (ej. 1.0 a 10.0)
            if not (0.0 <= nota <= 10.0): # Puedes ajustar el rango de notas si es diferente
                print("Nota fuera de un rango razonable (0.0-10.0). Por favor, intenta de nuevo.")
                continue
            # 5. Llevar la cuenta de:
            total_notas_ingresadas += 1
            suma_total_notas += nota
            # Cantidad de aprobados (nota >= 6.0) y reprobados (nota < 6.0)
            if nota >= 6.0:
                cantidad_aprobados += 1
            else:
                cantidad_reprobados += 1
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número para la nota o 'fin' para terminar.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
    print("\n--- Resultados del Análisis ---")
    # 6. Cuando el usuario escriba fin, el programa debe:
    if total_notas_ingresadas > 0:
        # Calcular el promedio general
        promedio_general = suma_total_notas / total_notas_ingresadas
        print(f"Promedio general de notas: {promedio_general:.2f}") # Formatear a 2 decimales
        print(f"Cantidad de estudiantes aprobados (>= 6.0): {cantidad_aprobados}")
        print(f"Cantidad de estudiantes reprobados (< 6.0): {cantidad_reprobados}")
        print(f"Cantidad total de estudiantes ingresados: {total_notas_ingresadas}")
    else:
        print("No se ingresaron notas. No hay datos para calcular.")

    print("---------------------------------------------")
if __name__ == "__main__":
    calcular_promedios()