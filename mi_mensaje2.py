import tkinter

raiz = tkinter.Tk()
mi_frame = tkinter.Frame(raiz)
mi_frame.pack()
mensaje = "Adoro el Yogurt Congelado de fresas"
etiqueta = tkinter.Label(mi_frame,text=mensaje)
mensaje = "Adoro el Yogurt Congelado de fresas y cereal"
etiqueta = tkinter.Label(mi_frame,text=mensaje)
etiqueta.pack()

raiz.mainloop()