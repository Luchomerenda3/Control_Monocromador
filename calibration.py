import serial


puerto = "/dev/ttyUSB0"         #Por defecto en GNU/linux, en Windows ("COM3")
velocidad = 115200              #Puede ser: 50, 75, 110, 134, 150, 200, 300, 600,
                                #1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200.
arduino_port = serial.Serial(puerto,velocidad,timeout=1)  #Abrimos el puerto finalmente

cal = 0
while cal != "sal":

    cal = input("Enter steps to do, enter \"sal\" to exit:  ")
    if cal != "sal":
        arduino_port.write(cal.encode())
    else:
        print("bye bye bitches")