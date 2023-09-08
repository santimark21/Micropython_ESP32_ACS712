from machine import Pin # Para definir los pines
from machine import ADC # Declaracion de la conversion ADC
from time import sleep_ms # libreria de tiempo Sleep
from machine import lightsleep # libreria para el lightsleep


pin = Pin(34)


adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)

while True:
    val1=adc.read()
    val2=5*val1/4095
    print('Voltage: ',val2)
    sleep_ms(2000)

    print('Going into Light Sleep Mode')
    sleep_ms(500)
    lightsleep(10000)     #10000ms sleep time
