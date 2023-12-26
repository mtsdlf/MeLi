from http.server import BaseHTTPRequestHandler, HTTPServer
import psutil
import json
import subprocess

class DiskUsageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/device_list':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            device_info = self.get_device_info()
            self.wfile.write(json.dumps(device_info).encode('utf-8'))
        elif self.path == '/run_script':
            # Lógica para ejecutar script local
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            try:
                # Ejemplo de ejecución de un script local en el mismo directorio
                script_output = subprocess.check_output(['bash', 'script.bash'], text=True)
                self.wfile.write(f'Script Output: {script_output}'.encode('utf-8'))
            except subprocess.CalledProcessError as e:
                self.wfile.write(f'Error running script: {str(e)}'.encode('utf-8'))
        elif self.path.startswith('/'):
            device_name = self.path[1:].replace('/', '')  # Elimina barras diagonales
            usage_percentage = self.get_disk_usage(device_name)

            if usage_percentage is not None:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                response_data = {'device': device_name, 'usage_percentage': usage_percentage}
                self.wfile.write(json.dumps(response_data).encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Device {device_name} not found'.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Not Found'.encode('utf-8'))

    def get_device_info(self):
        partitions = psutil.disk_partitions()
        device_info = [{'device': partition.device, 'usage_percentage': self.get_disk_usage(partition.device)} for partition in partitions]
        return device_info

    def get_disk_usage(self, device_name):
        try:
            usage = psutil.disk_usage(device_name)
            return usage.percent
        except Exception as e:
            print(f'Error getting disk usage for {device_name}: {str(e)}')
            return None

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DiskUsageHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()