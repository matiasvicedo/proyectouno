import tkinter as tk
  
# Ventana principal
frame = tk.Tk()
frame.title("Liberar CUIT")
frame.geometry('400x200')

#metodo
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "El s_org_id es: "+inp)
  
#creacion del textbox
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
#imprime en pantalla  
inputtxt.pack()
  
#Cracion del boton
printButton = tk.Button(frame,
                        text = "Aceptar", 
                        command = printInput)
#imprime en pantalla
printButton.pack()
  
#Texto en pantalla
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()


# prueba
