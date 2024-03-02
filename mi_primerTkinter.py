import tkinter

raiz = tkinter.Tk()
mi_frame = tkinter.Frame(raiz)
mi_frame.pack()
mensaje = "Hola mundo"
etiqueta = tkinter.Label(mi_frame,text=mensaje)
etiqueta.pack()
button = tkinter.Button(mi_frame)
button.pack()
raiz.mainloop()