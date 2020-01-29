"""
                                              Programación I
                                            
    FUNCIONES: Ejercicio 4

    Una persona desea llevar el control de los gastos realizados al viajar en el suterráneo dentro
    de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes
    (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro
    la cantidad de viajes realizados en un determinado mes y devuelve el total gastado en viajes.
    Realizar tambien un programa para verificar el comportamiento de la funcion.
    
    1 a 20 --------------Averiguar valor actualizado.
    21 a 30 -------------20% desc sobre tarifa máxima.
    31 a 40 -------------30% desc sobre tarifa máxima.
    Mas de 40 -----------40% desc sobre tarifa máxima.
   _____________________________________________________________________________________________________

                                                                                                        """
#F U N C I O N

def viajero(a,b):
    res=0
    a20=20*a
    a30desc20=10*((a/100)*80)
    a40desc30=10*((a/100)*70)
    if b<=20:
        res=a*b
    elif b<=30:
        res=a20+((b-20)*((a/100)*80))
    elif b<=40:
        res=a20+a30desc20+((b-30)*((a/100)*70))
    else:
        res=a20+a30desc20+a40desc30+((b-40)*((a/100)*60))
    return res
    

# P R O G R A M A 
valor=0
viajes=0
while valor<=0:
    valor=float(input("Ingrese el valor del viaje: "))
while viajes<=0:
    viajes=float(input("Ingrese la cantidad de viajes: "))
total=viajero(valor, viajes)
print("El total es: ", total)

"""
   ____________________________________________________________________________________________________

    Estrategia:
               En la cadena de if/else se va filtrando el resultado en cadena de menores e iguales,
               y, dependiendo del rango en el que se encuentre, el algoritmo que define el resultado
               se actualiza.
               Asimismo, en el programa se verifica la positividad de los valores.
   ____________________________________________________________________________________________________

                                                                                                        """
