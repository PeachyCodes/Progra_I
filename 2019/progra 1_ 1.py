"""
                                              Programación I
                                            
    FUNCIONES: Ejercicio 1

    Desarrolle una funcion que reciba tres numeros positivos y devuelva el mayor de los tres
    solo si este es unico (mayor estricto). En caso de no existir el mayor estricto, devolver -1.
    no utilizar operadores lógicos (and,or,not). Desarrollar también un programa para ingresar
    los tres valores, invocar a la función y mostrar el máximo hallado,
    o un mensaje informativo si este no existe.
   _____________________________________________________________________________________________________

                                                                                                        """
#F U N C I O N
def mayorEstrictoDeTres(a,b,c):
    res=-1
    pri=0
    seg=0
    if a > b:
        if a > c:
            pri=a
            if b > c:
                seg=b
            else:
                seg=c
        else:
            pri=c
            seg=a
    else:
        if b > c:
            pri=b
            if a > c:
                seg=a
            else:
                seg=c
        else:
            pri=c
            seg=b
    if pri != seg:
        res=pri
    return res    

# P R O G R A M A 
nro1=int(input("Ingrese el primer numero: "))
nro2=int(input("Ingrese el segundo numero: "))
nro3=int(input("Ingrese el tercer numero: "))
mayor=mayorEstrictoDeTres(nro1,nro2,nro3)
if mayor != -1:
    print("El mayor numero es: ", mayor, "!")
else:
    print("No existe un numero mayor entre los tres! :( ")

"""
   ____________________________________________________________________________________________________

    Estrategia:
                La cantidad de permutaciones de 3 elementos es 3!.
               
                En 3 de las 6 permutaciones posibles, a > b y en las otras 3, a < b.
                A su vez, en ambos casos, existen 2 posibilidades de permutar c .
                En base a esa lógica, se puede diagramar el algoritmo que determina
                cuáles son las 2 primeras posiciones("pri" y "seg").
                Es necesario saberlas para luego verificar que el mayor sea estricto.
                
                La tercera posición no importa, porque permitimos que existan 2 menores iguales. 
                
                El resultado que devuelve la funcion siempre es -1.
                Pero si "pri" y "seg" son distintos, significa que hay un mayor estricto y, 
                sólo en este caso, resultado toma el valor de "pri".
   ____________________________________________________________________________________________________

                                                                                                        """
