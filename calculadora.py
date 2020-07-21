from tkinter import *

root=Tk()

miFrame=Frame(root)
miFrame.pack()

operacion=""
resultado=0
reset_pantalla=False

#------------------------------ PANTALLA ---------------------------
numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#00ffff",justify="right")

#------------------------------ INGRESO TECLADO ---------------------------

def numero_pulsado(num):
    global operacion
    global reset_pantalla

    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False
    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#------------------------------ SUMA ---------------------------

def suma(num):
    global operacion
    global resultado
    global reset_pantalla

    resultado+=int(num)
    operacion="suma"
    reset_pantalla=True
    numeroPantalla.set(resultado)
    
#------------------------------ RESTA ---------------------------
contador_rest=0
num1=0

def resta(num):
    global operacion
    global resultado
    global reset_pantalla
    global contador_rest
    global num1

    if contador_rest==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_rest==1:
            resultado=int(resultado)-int(num)
        
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    
    contador_rest+=1
    operacion="resta"    
    reset_pantalla=True
#------------------------------ MULTIPLICACION ----------------------------
contador_mult=0

def multiplicacion(num):
    global operacion
    global resultado
    global num1
    global contador_mult
    global reset_pantalla

    if contador_mult==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_mult==1:
            resultado=num1*int(num)
        else:
            restultado=int(resultado)*int(num)
        
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    
    contador_mult+=1
    operacion="multiplicacion"
    reset_pantalla=True

#------------------------------ DIVION ---------------------------

contador_div=0

def division(num):
    global operacion 
    global resultado
    global num1
    global contador_div
    global reset_pantalla

    if contador_div==0:
        num1=float(num)
        resultado=num1
    else:
        if contador_div==1:
            resultado=num1/float(num)
        else:
            resultado=float(resultado)/float(num)
        
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    
    contador_div+=1
    operacion="division"
    reset_pantalla=True

#------------------------------ IGUAL ---------------------------

def igual():
    global operacion
    global resultado
    global contador_rest
    global contador_mult
    global contador_div

    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0
    elif operacion=="resta":
         numeroPantalla.set(int(resultado)-+int(numeroPantalla.get()))
         resultado=0
         contador_rest=0
    elif operacion=="multiplicacion":
          numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
          resultado=0
          contador_mult=0
    elif operacion=="division":
          numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))
          resultado=0
          contador_div=0

#------------------------------ LIMPIAR PANTALLA ---------------------------

def limpiar_pantalla():
    global resultado
    pantalla.delete(0,END)
    resultado=0

#------------------------------ FILA 1 ---------------------------
boton7=Button(miFrame,text="7",width=3,command=lambda:numero_pulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=3,command=lambda:numero_pulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=3,command=lambda:numero_pulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=3, command=lambda:division(numeroPantalla.get()))
botonDiv.grid(row=2,column=4)
#------------------------------ FILA 2 ---------------------------
boton4=Button(miFrame,text="4",width=3,command=lambda:numero_pulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=3,command=lambda:numero_pulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=3,command=lambda:numero_pulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="*",width=3,command=lambda:multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3,column=4)
#------------------------------ FILA 3 --------------------------
boton1=Button(miFrame,text="1",width=3,command=lambda:numero_pulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=3,command=lambda:numero_pulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=3,command=lambda:numero_pulsado("3"))
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text="-",width=3,command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4,column=4)
#------------------------------ FILA 4 ---------------------------
boton0=Button(miFrame,text="0",width=3,command=lambda:numero_pulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",",width=3,command=lambda:numero_pulsado("."))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=",width=3,command=lambda:igual())
botonIgual.grid(row=5,column=3)
botonSum=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5,column=4)
#------------------------------ FILA 5 ---------------------------

botonBorrar=Button(miFrame,text="Limpiar Pantalla",command=lambda:limpiar_pantalla())
botonBorrar.grid(row=6,column=1,columnspan=4)
root.mainloop()