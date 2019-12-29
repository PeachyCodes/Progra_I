"""
                                              Programación I
                                            
    FUNCIONES: Ejercicio 5
    
    Un comercio de electrodomésticos necesita para su linea de cajas un programa que le indique al
    cajero el cambio que deje entregarle al cliente. Para eso se ingresan dos numeros enteros,
    correspondiente al total de la compra y al dinero recibido.
    Informar cuantos billetes de cada demonimacion deben ser entrgados al cliente como vuelto,
    de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de 500,
    100, 50, 20, 10, 5 y 1. Emitir un mensaje de error si el dinero recibido fuera insuficiente.
    
   _____________________________________________________________________________________________________

                                                                                                        """
#F U N C I O N
def vueltex(a,b):
    res=b-a
    return res

def billetex(x):
    lista=[]
    if x>=500:
        x500=x//500
        x=x-(x500*500)
    else:
        x500=0
    lista.append(x500)    
    if x>=100:
        x100=x//100
        x=x-(x100*100)
    else:
        x100=0
    lista.append(x100)
    if x>=50:
        x50=x//50
        x=x-(x50*50)
    else:
        x50=0
    lista.append(x50)
    if x>=10:
        x10=x//10
        x=x-(x10*10)
    else:
        x10=0
    lista.append(x10)
    if x>=5:
        x5=x//5
        x=x-(x5*5)
    else:
        x5=0
    lista.append(x5)
    if x>=1:
        x1=x//1
    else:
        x1=0
    lista.append(x1)   
    return lista

# P R O G R A M A
total=int(input("Ingrese el total de la compra: "))
dinero=int(input("Ingrese el dinero recibido: "))
while dinero<total:
    print("ERROR: el dinero ingrasado es menor que el total")
    dinero=int(input("Ingrese el dinero recibido: "))
vuelto=vueltex(total,dinero)
print("El vuelto es: $", vuelto)
billetes=billetex(vuelto)
divisas=[500,100,50,10,5,1]
for i in range (0,len(divisas)):
    if billetes[i] != 0:
        if billetes[i] > 1:
            print(billetes[i],"billetes de ",divisas[i])
        else:
            print(billetes[i],"billete de ",divisas[i])
    else:
        i=i+1
    
"""
   ____________________________________________________________________________________________________

    Estrategia:
                Creé un funcion que calcula el vuelto.
                Luego creé otra funcion que crea una lista con la cantidad minima de billetes necesaria.
                En la lista se almacena, aunque sean vacíos, la cantidad de billetes de cada cantidad.
                La lista respeta el orden de mayor a menor. Para impirmir, se ignoran los valores vacios,
                pero no dejan de ser necesarios para darle orden al programa.
                Si no hay vuelto, devuelve mensaje. Pero si lo hay, se va imprimiento en un if/else
                pasa que solo los valores naturales se impriman.
   ____________________________________________________________________________________________________

                                                                                                        """