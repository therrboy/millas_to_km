from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Milla to Km")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)  # Le da mas espacio/relleno contra los bordes de los widgets, en "window" lo hace sobre

# Cuadrado 2 de 9: Ingreso numero a convertir, en un cuadro.
input = Entry(width=20)  # Entre viene del modulo tkinter
input.grid(column=1, row=0, padx=5, pady=5)

# Cuadrado 3 de 9: Texto "Millas"
texto_millas = Label(text="Millas", font=("Arial", 24, "bold"))
texto_millas.grid(column=2, row=0, padx=5, pady=5)

# Cuadrado 4 de 9: Texto "Es igual a:"
texto_igual = Label(text="Es igual a:", font=("Arial", 24, "bold"))
texto_igual.grid(column=0, row=1, padx=5, pady=5)

# Cuadrado 5 de 9: Resultado del numero ingresado
texto_resultado = Label(text="", font=("Arial", 24, "bold"))
texto_resultado.grid(column=1, row=1, padx=5, pady=5)

# Cuadrado 6 de 9: Texto "Km"
texto_km = Label(text="Km", font=("Arial", 24, "bold"))
texto_km.grid(column=2, row=1, padx=5, pady=5)

# Cuadrado 8 de 9: Boton para calcular
def click_boton():
    nueva_frase = float(input.get())  # si colocamos aqui el input con el get, alteramos lo anterior y cambia el programa
    km = round(nueva_frase * 1.609)
    texto_resultado.config(text=km)

boton = Button(text="Calcular", command=click_boton, height=2, width=15)  # esta propiedad comando puede tomar una funcion y detectarla
boton.grid(column=1, row=2, padx=5, pady=5)

window.mainloop()