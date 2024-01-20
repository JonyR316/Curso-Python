"""
Desarrollar una clase que represente un punto en el plano y tenga los siguientes metodos: inicializar 
los valores de x e y que llegan como parametros, imprimir en que cuadrante se encuentra dicho punto 
(concepto matematico,primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)
"""

class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def imprimir(self):
        print("( X:",self.x,",","Y:",self.y,")")

    def cuadrante(self):
        if self.x > 0 and self.y >0:
           print("Este es el cuadrante 1")
        else:
            if self.x < 0 and self.y >0:
                print("Este es el cuadrante 2")
            else:
                if self.x < 0 and self.y < 0:
                    print("Este es el cuadrante 3")
                else:
                    if self.x > 0 and self.y < 0:
                        print("Este es el cuadrante 4")
                    else:
                        print("Se encuentra en algun eje")


punto1=Punto(9,6)
punto1.imprimir()
punto1.cuadrante()

punto2=Punto(-9,6)
punto2.imprimir()
punto2.cuadrante()

punto3=Punto(-9,-6)
punto3.imprimir()
punto3.cuadrante()

punto4=Punto(9,-6)
punto4.imprimir()
punto4.cuadrante()