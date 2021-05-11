# Martucci Flavio 4inf3
import tkinter as tk


def menuPrincipale():
    testoLotto = tk.Label(finestra, text='Lotto', bg="white", font=("Helvetica",50))
    testoLotto.grid(row=0, column=0, sticky="N")

    bottoneAvviaPartita = tk.Button(text="Nuova partita")
    bottoneAvviaPartita.grid(row=1, column=0, sticky="N")




finestra = tk.Tk()
finestra.title("Gioco lotto - Martucci")
finestra.geometry("800x600")
finestra.configure(background="white")
finestra.grid_columnconfigure(0, weight=1)

menuPrincipale()

# e = tk.Entry()
# e.insert(0,"")
# e.pack()


finestra.mainloop()

