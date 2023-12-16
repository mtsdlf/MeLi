# Disk Usage HTTP Server

Este proyecto implementa un servidor HTTP simple en Python utilizando el módulo `http.server` para proporcionar información sobre el uso de disco para dispositivos de almacenamiento conectados al host.

## Características

- **Endpoint individual para cada dispositivo de almacenamiento:** Puedes obtener el porcentaje de uso de disco para cada dispositivo accediendo a su endpoint correspondiente.

- **Endpoint para obtener la lista de sistemas de almacenamiento:** Un endpoint especial `/storage_list` proporciona una lista en formato JSON de todos los dispositivos de almacenamiento conectados.

## Requisitos

- Python 3.x
- Módulo `psutil`

## Uso

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/disk-usage-http-server.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd disk-usage-http-server
    ```

3. Instala las dependencias:

    ```bash
    pip install psutil
    ```

4. Ejecuta el servidor:

    ```bash
    python disk_server.py
    ```

5. Accede a los endpoints desde tu navegador o utilizando herramientas como `curl` o `httpie`.

## Endpoints

- **Obtener porcentaje de uso de disco para un dispositivo específico:**
    - Endpoint: `http://localhost:8000/nombre_del_dispositivo`
    - Ejemplo: `http://localhost:8000/sda1`

- **Obtener la lista de todos los sistemas de almacenamiento:**
    - Endpoint: `http://localhost:8000/storage_list`

## Contribuciones

Si encuentras errores o deseas realizar mejoras, ¡no dudes en abrir un problema o enviar una solicitud de extracción!

## Licencia

Este proyecto está bajo la Licencia MIT -