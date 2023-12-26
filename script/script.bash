import subprocess
import platform

def reiniciar_equipo():
    sistema_operativo = platform.system()

    if sistema_operativo == 'Linux' or sistema_operativo == 'Darwin':
        # Reiniciar en sistemas Unix (Linux, macOS)
        subprocess.run(['sudo', 'reboot'])
    elif sistema_operativo == 'Windows':
        # Reiniciar en sistemas Windows
        subprocess.run(['shutdown', '/r', '/t', '1'])
    else:
        print(f'No se puede reiniciar el equipo en el sistema operativo {sistema_operativo}')

# Llama a la función para reiniciar el equipo
reiniciar_equipo()