"""
                                              Programación I
                                            
    FUNCIONES: Ejercicio 7
    
    Desarrollar una funcion que reciba como parametros dos numeros enterios y devuelva el numero
    que resulte de concatenar ambos valores. Por ejemplo, se recibe 1234 y 567 y debe devolver 1234567.
    No se permite usar facilidades de Python no vistas en clase.
   _____________________________________________________________________________________________________

                                                                                                        """
#F U N C I O N
def unidos (a,b):
    a=str(a)
    b=str(b)
    x=int(a+b)
    return x
        
# P R O G R A M A 
nro1=int(input("Ingrese un número: "))
nro2=int(input("Ingrese un segundo número: "))
res=unidos(nro1,nro2)
print("El numero unido es: ", res)

"""
   ____________________________________________________________________________________________________

    Estrategia:
            Manipular las funciones str e int para unir ambos valores y no sumarlos algebraicamente.
   ____________________________________________________________________________________________________

                                                                                                        """