"""
                                              Programación I
                                            
    FUNCIONES: Ejercicio 6
    
    Escribir dos funciones para imprimir por pantalla cada uno de los siguientes patrones de asteriscos
    donde la cantidad de filas se recibe como parametro:
    
                                **********                          **
                                **********                          ****
                                **********                          ******
                                **********                          ********
                                **********                          **********  
   _____________________________________________________________________________________________________

                                                                                                        """
#F U N C I O N
def asterix1(x):
    res=[]
    a="**********"
    for i in range (x):
        res.append(a)
    return res

def asterix2(x):
    res=[]
    a="**"
    for i in range (x):
        res.append(a)
        a="{0}**".format(a)
    return res
        
# P R O G R A M A 
filas=int(input("Ingrese la cantidad de filas de asteriscos: "))
res1=asterix1(filas)
res2=asterix2(filas)
print("------------------------------------------------")
for i in range (0,len(res1)):
    print(res1[i])
print(" ")
for i in range (0,len(res2)):
    print(res2[i])

"""
   ____________________________________________________________________________________________________

    Estrategia:
            Las funciones crean listas de strings, que luego se imprimen en el programa con un ciclo
                
   ____________________________________________________________________________________________________

                                                                                                        """