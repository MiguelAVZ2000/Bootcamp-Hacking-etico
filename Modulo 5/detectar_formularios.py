import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def detectar_formularios(url):
    """
    Conecta a una URL, detecta formularios HTML y extrae información relevante
    sobre ellos y sus campos de entrada.

    Args:
        url (str): La URL de la página web a analizar.
    """
    print(f"--- Iniciando detección de formularios en: {url} ---")

    try:
        response = requests.get(url, timeout=5) 
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')

        if not forms:
            print("No se encontraron formularios en esta página.")
            return

        print(f"Se encontraron {len(forms)} formulario(s).")
        print("------------------------------------------")

        for i, form in enumerate(forms, 1): 
            print(f"\n📝 Formulario detectado #{i}:")
            
            method = form.get('method', 'GET').upper()
            print(f"  Método: {method}")

            action = form.get('action', '[sin acción definida]')
            absolute_action_url = urljoin(url, action)
            print(f"  Acción: {absolute_action_url}")

            print("  Campos:")
            fields = form.find_all(['input', 'textarea', 'select'])

            if fields:
                for field in fields:
                    name = field.get('name', '[sin nombre]')
                    
                    if field.name == 'input':
                        field_type = field.get('type', 'text')
                    else:
                        field_type = field.name
                    
                    print(f"    * name: {name} | type: {field_type}")
            else:
                print("    (No se encontraron campos de entrada en este formulario)")
    except requests.exceptions.MissingSchema:
        print("[ERROR] La URL no tiene un esquema válido (ej. http:// o https://).")
        print("        Por favor, ingresa la URL con el esquema completo.")
    except requests.exceptions.ConnectionError:
        print(f"[ERROR] Error de conexión: No se pudo conectar a '{url}'. Asegúrate de que la URL es correcta y tienes conexión a internet.")
    except requests.exceptions.Timeout:
        print(f"[ERROR] Tiempo de espera agotado al conectar a '{url}'. La página tardó demasiado en responder.")
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] Error HTTP al solicitar '{url}': {e}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Ocurrió un error en la solicitud a '{url}': {e}")
    except Exception as e:
        print(f"[ERROR] Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    print("=== Detección de Formularios HTML y Campos de Entrada ===\n")
    url_a_analizar = input("Ingresa la URL a analizar (ej. https://example.com): ").strip()
    
    if url_a_analizar and not (url_a_analizar.startswith('http://') or url_a_analizar.startswith('https://')):
        url_a_analizar = 'http://' + url_a_analizar
    
    if url_a_analizar:
        detectar_formularios(url_a_analizar) 
    else:
        print("No se ingresó ninguna URL. El programa ha terminado.")