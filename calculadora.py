""" Autor: Juan Carlos Ortegón Aguilar """

#Importamos las bibliotecas necesarias
from tkinter import Tk,Text,Button,END,re

#Clase Interfaz
class Interfaz:
    def __init__(self, ventana):

        #Inicializar la ventana con un título y un tamaño determinado
        self.ventana=ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("517x335")

        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla=Text(ventana, state="disabled", width=43, height=1, background="#FFD733", foreground="black", font=("Helvetica",15), padx=10, pady=20, borderwidth=4, relief="groove")

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""
        self.ans=""

        #Crear los botones de la calculadora con sus respectivos valores y colores
        boton1=self.crearBoton("(", color="#c0c0c0")
        boton2=self.crearBoton(")", color="#c0c0c0")
        boton3=self.crearBoton("ans", color="#c0c0c0")
        boton4=self.crearBoton(u"\u232B",escribir=False, color="#c0c0c0")
        boton5=self.crearBoton(7)
        boton6=self.crearBoton(8)
        boton7=self.crearBoton(9)
        boton8=self.crearBoton(u" \u00F7 ", color="#c0c0c0")
        boton9=self.crearBoton(4)
        boton10=self.crearBoton(5)
        boton11=self.crearBoton(6)
        boton12=self.crearBoton(" x ", color="#c0c0c0")
        boton13=self.crearBoton(1)
        boton14=self.crearBoton(2)
        boton15=self.crearBoton(3)
        boton16=self.crearBoton(" - ", color="#c0c0c0")
        boton17=self.crearBoton(0)
        boton18=self.crearBoton(".")
        boton19=self.crearBoton("=",escribir=False, color="#0099ff")
        boton20=self.crearBoton(" + ", color="#c0c0c0")

        #Ubicar los botones con el gestor grid
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17, boton18, boton19, boton20]
        contador=0
        for fila in range(1,6):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna, pady=2)
                contador+=1
        
        return


    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1, color="#e2d7de"):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir), relief="groove", borderwidth=4, background=color)


    #Controla el evento disparado al hacer click en un botón
    def click(self, texto, escribir):
        #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
        if not escribir:
            #Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
            if texto=="=" and self.operacion!="":
                #Reemplazar el valor unicode de la división por el operador división de Python '/'
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                self.operacion=re.sub(u"x", "*", self.operacion)
                self.operacion=re.sub(u"ans", self.ans, self.operacion)
                try:
                    resultado=str(eval(self.operacion))
                    self.ans=resultado
                except:
                    resultado="Error"

                self.operacion=resultado
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)

            #Si se presionó el botón de borrado, limpiar la pantalla dependiendo de la operación que haya
            elif texto==u"\u232B":

                if(self.operacion.__contains__("Error")):
                    self.limpiarPantalla()
                    self.operacion=""

                elif((self.operacion.__contains__("ans") and self.operacion[-1] == "s") or (len(self.operacion) >=1 and self.operacion[-1] == " ")):
                    self.operacion = self.operacion[:-1]
                    self.operacion = self.operacion[:-1]
                    self.operacion = self.operacion[:-1]
                    self.limpiarPantalla()
                    self.mostrarEnPantalla(self.operacion)

                else:
                    self.operacion = self.operacion[:-1]
                    self.limpiarPantalla()
                    self.mostrarEnPantalla(self.operacion)

        #Mostrar texto
        else:
            if(self.operacion.__contains__("Error")):
                self.operacion=""
                self.limpiarPantalla()

            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
            
        return
    

    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return
    

    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return


#Main
if __name__ == "__main__":
    ventana_principal=Tk()
    calculadora=Interfaz(ventana_principal)
    ventana_principal.mainloop()