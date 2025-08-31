import nmap
import sys

def escanear_red_y_reportar(subred_objetivo):
    """
    Realiza un escaneo de red con Nmap para detectar hosts activos,
    puertos abiertos, servicios y versiones de software.
    Genera un reporte estructurado en la consola.

    Args:
        subred_objetivo (str): La subred a escanear (ej. '192.168.1.0/24').
    """
    print(f"--- Iniciando Escaneo de Subred en: {subred_objetivo} ---")
    print("Esto puede tardar unos minutos, por favor, espera...")

    nm = nmap.PortScanner()
    
    try:
        # Realiza un escaneo con -sV (detección de servicios y versiones)
        # en todos los puertos comunes (-F para fast scan o -p 1-1000 para un rango específico)
        # Usaremos '-p 1-1024' para el ejemplo, pero -F o puertos comunes sería más rápido.
        # Para el propósito del ejercicio y evitar escaneos muy largos, usaremos un rango limitado.
        # '-T4' para un timing agresivo.
        nm.scan(hosts=subred_objetivo, arguments='-sV -T4 -F') 
        # Si deseas escanear más puertos o todos: '-sV -T4 -p 1-65535' (mucho más lento)
        # o '-sV -T4' (escanea los 1000 puertos más comunes por defecto)

    except nmap.PortScannerError as e:
        print(f"[ERROR] Error al ejecutar Nmap: {e}")
        print("Asegúrate de que Nmap esté instalado y en tu PATH.")
        print("En Linux/macOS, es posible que necesites ejecutar el script con 'sudo'.")
        return
    except Exception as e:
        print(f"[ERROR] Ocurrió un error inesperado durante el escaneo: {e}")
        return

    active_hosts_count = 0
    scan_results = {} # Para almacenar los resultados y ordenarlos

    # Itera sobre todos los hosts encontrados en el escaneo
    for host in nm.all_hosts():
        active_hosts_count += 1
        scan_results[host] = []
        
        # Verifica si el host tiene puertos TCP (la mayoría de servicios)
        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                port_info = nm[host]['tcp'][port]
                state = port_info['state']
                
                if state == 'open':
                    service_name = port_info.get('name', 'desconocido')
                    product_version = port_info.get('product', '')
                    version = port_info.get('version', '')

                    service_details = f"- Puerto {port}: {service_name}"
                    if product_version or version:
                        service_details += f" ({product_version} {version})".strip()
                    
                    scan_results[host].append(service_details)

    print("\n--- Resumen del Escaneo de Red ---")
    if not scan_results:
        print("No se encontraron hosts activos o servicios abiertos en la subred especificada.")
    else:
        # Imprime un resumen ordenado por host
        for host, services in sorted(scan_results.items()):
            print(f"Host: {host}")
            if services:
                for service in services:
                    print(f"  {service}")
            else:
                print("  No se encontraron puertos abiertos en este host.")
            print() # Salto de línea para separar hosts

    print(f"Total de hosts activos: {active_hosts_count}")
    print("-----------------------------------")


if __name__ == "__main__":
    print("=== Escáner de Subred y Detección de Servicios ===\n")
    print("Ejemplo de subred: 192.168.1.0/24 o un host específico: 192.168.1.1")
    
    target_network = input("Ingresa la subred o IP objetivo para escanear: ").strip()

    if not target_network:
        print("No se ingresó ninguna subred/IP. Saliendo del programa.")
        sys.exit(1)

    escanear_red_y_reportar(target_network) 