"""
                                              Programación I
                                            
    FUNCIONES: Ejercicio 3
    
    Para un numero entero N recibido como parámetro, escribir un programa que utilice una funcion
    para devolver la suma de los cuadrados de aquellos numeros entre 1 y N que esten
    separados entre si por cuatro unidades.(1**2 + 5**2 + 9**2 + 13**2...)
    
   _____________________________________________________________________________________________________

                                                                                                        """
#F U N C I O N E S

def SumaCuadrados4(b):
    s=0
    for i in range (0, len(b)):
        n=(b[i])**2
        s=s+n
    return s   

# P R O G R A M A

#1)Controla que el numero este en el rango
n=0
while n<1 or n>100:
    n=int(input("Ingrese un numero (1,100): "))
#2)Genera lista de numeros a exponer
exp=[]
for i in range(1,n+1,4):
    exp.append(i)
#3)Imprime la enumeración de todos los cuadrados a sumar
for i in range (len(exp)):
    n=exp[i]
    print(i+1,")",n,"** 2 =",n**2)
#4)Imprime el cociente de la suma de los cuadrados
secuencia=SumaCuadrados4(exp)
print("La suma es: ",secuencia)

"""
   ____________________________________________________________________________________________________

    Estrategia:
                Se crea una lista de numeros a elevar y se aplica la función para acumular los cuadrados.
                El paso 3) es extra y solo sirve para el control y claridad del proceso.
   ____________________________________________________________________________________________________

                                                                                                        """