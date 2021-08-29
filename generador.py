import random
import sys
system=sys.platform
if system == 'linx':
    print(system)
    pass

else:
    print('instala linux por favor :v')
def funcion():
    try:
        while True:
            print('ESTE ES UN SIMPLE GENRADOR RANDOM CON PYTHON\n')
            ingreso_numero=input('Ingresa el Numero ---> : ')
            aleatorio=random.randint(int(ingreso_numero),10)
            print(aleatorio,' Este es el numero ^-^')
            if int(ingreso_numero) == aleatorio:
                print(ingreso_numero,' --> este es el numero ingresado que  resulto ganador')
            elif int(ingreso_numero) != aleatorio:
                print('lo sentimos, pero el numero no es el correcto')
    except ValueError:
        #pass
        print('Introduce un valor correcto')
funcion()