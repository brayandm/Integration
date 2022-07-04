import os

# Funcion para borrar el cache de los errores
def clear_cache():

    # Borrando toda la carpeta cache
    os.system('rmdir /s /q cache')

    # Breando la carpeta cache
    os.system('mkdir cache')