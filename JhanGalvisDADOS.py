#Este codigo fue creado en la version 3.8.5 de python
#Autor: Jhan Galvis
#Correo: Jhangalvis422@gmail.com
#No Copyright, Puedes usar este codigo a tu antojo. 
from random import choices
def Tirardados():
    Dados = choices([1, 2, 3, 4, 5, 6], k=2)
    Suma_Dados = Dados[0] + Dados[1]
    print("\nSacaste un:",Dados[0],"En el primer dado")
    print("Sacaste un:",Dados[1],"En el segundo dado")
    print("\nTienes",Suma_Dados,"Puntos")
def De_Nuevo():
    Val = input("\n¿Quieres volver a tirar los dados?(Si/No): ")
    if Val.capitalize() == "No":
        print("\nQue lastima :c, Jugaremos otro día")
        return False
    elif Val.capitalize() == 'Si':
        return True
    else:
        print("\nERROR, Ingresaste un dato invalido, recuerda responder (Si o No)")
        return De_Nuevo()
print("\n¡Jueguemos el juego de los dados!")
Y = True



while Y:
    Tirardados()
    Y = De_Nuevo()
#Hola para los que revisen mi tarea, espero sus comentarios y calificaiones. Gracias 