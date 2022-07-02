import os

def clear_cache():

    os.system('rmdir /s /q Cache')

    os.system('mkdir Cache')