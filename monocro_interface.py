#Código para controlar via puerto serie al Monocromador desarrollado en la cátedra de
# física experimental II de la facultad de ciencias exactas y naturales - UNCuyo por:
#            M. J. V. Ventura,
#            M. Galarza Martinez,
#            L. A. Merenda,
#            G. Portillo,
#            M. Chiarpotti,
#            F. Parizek,
#            D. Illesca,
#            N. Bizzotto.

########################################################################################################################
#Importamos la librerías necesarias y algunas funciones a utilizar.

import serial   #para comunicación serial con arduino
import os       #para control visual desde la consola
import time

def mover(pos,steps_taken):
    #Esta función toma la posición a la que debe moverse y calcula cuantos pasos tiene
    #que hacer el motor en función de la posición actual. Luego escribe en el puerto serie
    #la cantidad de pasos que tiene que hacer el motor y devuelve la posición actual del motor.
    os.system('clear')
    n_step_to_take = str(pos - steps_taken)  # pasos a dar desde la posición actual del motor
    arduino_port.write(n_step_to_take.encode()) #enviamos al puerto serie los pasos a dar
    print(f"Pasos a dar: {n_step_to_take}")
    time.sleep(0.5)
    print(f"Arduino confirma que dio {arduino_port.readline()} pasos")
    steps_taken += int(n_step_to_take)  # Actualizamos la posición actual de la red
    return steps_taken

def wait():
    #Esta función espera a que el usuario del monocromador indique
    #que quiere cambiar de posición para evitar salir al menú y cambiar
    #accidentalmente de posición
    os.system('clear')
    standby = input("Moviendo red a la posición elegida...\n...\nSi desea cambiar de color, ir a modo manual  o salir ingrese \"cam\":  ")

    while standby != "cam":
        standby = input("Si desea cambiar de color, ir a modo manual  o salir ingrese \"cam\":  ")

    print("Volviendo al menú principal... \n...\n")
    time.sleep(0.2)

def retorno(steps_taken):
    #Esta función solo retorna el motor a su posición inicial.

    print("Retornando la red a su posición inicial")
    steps_taken = str(-steps_taken)
    arduino_port.write(steps_taken.encode())
    print(f"Pasos a dar: {steps_taken}")
    time.sleep(0.5)
    print(f"Arduino confirma que dio {arduino_port.read()} pasos")
################################################################################################################


#Iniciamos el programa.
print("""
######################################################################################
###                           Monocromador FCEN-UNCuyo v1.0                        ###
######################################################################################
""")

#Abrimos el puerto para comunicarnos con el arduino,

puerto = "/dev/ttyUSB0"         #Por defecto en GNU/linux, en Windows ("COM3")
velocidad = 115200              #Puede ser: 50, 75, 110, 134, 150, 200, 300, 600,
                                #1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200.
arduino_port = serial.Serial(puerto,velocidad,timeout=1)  #Abrimos el puerto finalmente

#Asegurarse que la velocidad es la misma que la configurada en el arduino
#La configuración default para bit de data, bit de paridad y bits de stop
#es la misma (8N1) por defecto tanto en la libreria serial de python como
#en el serial.begin() de arduino por lo que no es necesaria configurarlo.


#Definimos algunas variables constantes a utilizar

angle_per_step = 5.625 / 64 #ángulo por paso del motor paso a paso 28BYJ-48
n_step_taken = 0  # Iniciamos la variable para llevar cuenta de cuantos pasos se han dado desde la posición inicial.
selection = 0 #iniciamos variable auxiliar de seleccion del menu.

while selection != "Sa":
    selection = input("""\n
Seleccionar un opción del menú:\n
    1)Rojo [Ro]
    2)Naranja [Na]
    3)Amarillo [Am]
    4)Verde [Ve]
    5)Turquesa [Tu]
    6)Azul [Az1]
    7)Azul [Az2]
    8)Violeta [Vi]
    9)Control manual [Cm]
    10)Salir [Sa]
    \nOpción seleccionada:   """)

    #A cada color le va a corresponder una posición en cantidad de pasos desde la posición inicial
    if selection == "Ro":
        position = 0 #valor de prueba hay que calibrar!

        #Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position,n_step_taken)

        #Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()

    elif selection == "Na":
        position = +15  # valor de prueba hay que calibrar!

        # Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position, n_step_taken)

        # Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()

    elif selection == "Am":
        position = +23  # valor de prueba hay que calibrar!

        # Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position, n_step_taken)

        # Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()

    elif selection == "Ve":
        position = +33  # valor de prueba hay que calibrar!

        # Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position, n_step_taken)

        # Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()
    
    elif selection == "Tu":
        position = +43  # valor de prueba hay que calibrar!

        # Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position, n_step_taken)

        # Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()
        
    elif selection == "Az1":
        position = +53  # valor de prueba hay que calibrar!

        # Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position, n_step_taken)

        # Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()
        
    elif selection == "Az1":
        position = +63  # valor de prueba hay que calibrar!

        # Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position, n_step_taken)

        # Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()
        
    elif selection == "Vi":
        position = +69  # valor de prueba hay que calibrar!

        # Movemos el motor y una actualizamos la posición del motor
        n_step_taken = mover(position, n_step_taken)

        # Esperamos a que el usuario quiera otro color, modo manual o salir
        wait()

    elif selection == "Cm":
        #Para el modo manual volvemos el motor a su posición inicial
        retorno(n_step_taken)
        #Y empezamos nuevamente.
        n_step_taken = 0 #la volvemos a cero

        cm = True   #variable auxiliar para control manual
        while cm != False:
            #iniciamos modo manual e ingresamos la cantidad de pasos a dar
            angle_to_take = input("\nModo Manual:\nInserte Giro Horario[+] o AntiHorario[-], y ángulo a mover (Ejemplo: \"+15\") \n ó ingrese\"[s]\" para volver al menu anterior:")
            if angle_to_take != "s":
                #Traducimos de ángulo a pasos del motor
                #Redondeamos a un numero entero de pasos porque no existen pasos intermedios
                position = round(float(angle_to_take) / angle_per_step) + n_step_taken #Angles are in degrees

                #Movemos el motor y actualizamos la posición del motor
                n_step_taken = mover(position,n_step_taken)

                #Falta stand by
                # Esperamos a que el usuario quiera otro color, modo manual o salir
                wait()

            else:
                cm = False

    elif selection == "Sa":
        #retornamos la red a su posición inicial.
        retorno(n_step_taken)
        print("\nGracias por utilizar Monocromador v1.0")
        time.sleep(1.5)

    else:
        print("Opción incorrecta o no renocida")

    #Limpiamos la pantalla cada vez que mostramos el menú
    os.system('clear')

