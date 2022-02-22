"""
Archivo que se ejecuta luego de crear mi plantilla de Cookiecutter y que me inicializa un repositorio en git para
mi creación. 
"""

import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
# subprocess.call(['pip', 'install', '-r', 'requirements.txt']) Comentado porque no funciona

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")