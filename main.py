from http.server import BaseHTTPRequestHandler, HTTPServer
import psutil
import json

class DiskUsageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/storage_list':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            storage_list = self.get_storage_list()
            self.wfile.write(json.dumps(storage_list).encode('utf-8'))
        elif self.path.startswith('/'):
            device_name = self.path[1:]
            usage_percentage = self.get_disk_usage(device_name)

            if usage_percentage is not None:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f'Disk usage for {device_name}: {usage_percentage}%'.encode('utf-8'))
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

    def get_storage_list(self):
        partitions = psutil.disk_partitions()
        storage_list = [partition.device for partition in partitions]
        return storage_list

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