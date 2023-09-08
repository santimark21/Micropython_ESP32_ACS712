from machine import Pin # Para definir los pines
from machine import ADC # Declaracion de la conversion ADC
from time import sleep # libreria de tiempo Sleep
from machine import deepsleep # libreria para el deepsleep
import math


def circuit(adc,sensibility,Vrms):
    Vprom = 0
    Vprom2 = 0
    Vn = []
    sumita = 0
    sumita2 = 0
    for i in range(3501):
        val1=adc.read()
        val2=3.3*val1/4095
        #Vn.append(val2)
        Vprom = Vprom + val2
#         sleep(0.00025)


    Vprom2 = Vprom/3500
    print('Voltaje prom: ',Vprom2)
    #Vprom = 0


    # Calculo de la corriente RMS

    # for de la sumatoria para 200 muestras
    for j in range(3501):
        val1=adc.read()
        Vn=3.3*val1/4095
        sumita = (Vn - Vprom2)**2
        sumita2 = sumita2 + sumita
        led_pin.value(not led_pin.value())
    #valor interno de la raiz
    divisao = sumita2/3500

    #Raiz cuadrada
    raiz = math.sqrt(divisao)

    # Corriente RMS
    Irms = raiz/sensibility

    print('Corriente RMS: ',Irms)
    Vprom = 0
    sumita = 0

        
    # potencia aparente
    Papp = Vrms*Irms
    print('Potencia aparente: ',Papp)


# // MAIN \\

# declaracion de los pines de la esp32 para usar
pin = Pin(34)
ON_BOARD_PIN = 2

#inicializacion de los pines
led_pin = Pin(ON_BOARD_PIN, Pin.OUT)

#lectura del ADC de la ESP32
adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)

# valores necesarios para la ejecucion

Vrms = 120.0
Sensibility = 0.066

circuit(adc,Sensibility,Vrms)


print('ya tiene el voltaje, la corriente y la potencia compae, me voy a mimir')
#sleep for 1 second (1000 milliseconds)
deepsleep(2000)

    
