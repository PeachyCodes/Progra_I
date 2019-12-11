"""
                                              Programación I
                                            
    FUNCIONES: Ejercicio 2
    
    Desarrollar una funciòn que reciba tres numeros enteros positivos y verifique si corresponden
    a una fecha gregoriana válida (dia, mes, año). Devolver True o False según la fecha sea
    correcta o no. Realidar tambien un programa para verificar el comportamiento de la funcion.
    
   _____________________________________________________________________________________________________

                                                                                                        """
#F U N C I O N E S

def positivo():
    n=int(input(":"))
    while n < 1:
        print("Ingrese un dato válido!")
        n=int(input(":"))
    return n
    
def Gregorio(a,b,c):
    boole=True
    añobi=False
    if c%4 == 0 and (c%100 == 0 and c%400 == 0):
        añobi=True
    if b <= 12 and (a <= 31):
        if (a == 30 and b%2 == 1) or (a == 31 and b%2 == 0):
            boole=False
        if b == 2 and (a >= 28):
            boole=False
        if b == 2 and (añobi==True and a >= 29):
            boole=False
    else:
        boole=False
    return boole

# P R O G R A M A

print("Ingrese dia")
dia=positivo()
print("Ingrese mes")
mes=positivo()
print("Ingrese año")
año=positivo()
f=dia,mes,año
fecha=Gregorio(dia,mes,año)
if fecha == False:
    print("La fecha ", f, "no es correcta.")
else:
    print("La fecha ", f, "es gregoriana! :)")

"""
   ____________________________________________________________________________________________________

    Estrategia:
                Se verifica el ingreso de un numero mayor igual a 1, en los 3 casos.
                En la funcion Gregorio, primero se define si el año es biciesto y luego
                se verifican las siguientes condiciones, en este orden.
                        -Que el dia sea menor/igual a 31 y que el mes sea menor/igual a 12.
                        -Que a cada dia, ya sea 30 0 31, le corresponda el mes.
                        -Si es Febrero, que el dia sea hasta el 28 ,o 29 solo en año biciesto.
                Si todas las condiciones se cumplen, el boole no se afecta y devuelve True.
                Pero si alguna de las condiciones no se cumple, el boole cambia a False.
                El programa imprime el mensaje que corresponda en casa caso, según la consigna.
                        
    ______________________________________________________________________________________________

                                                                                                        """