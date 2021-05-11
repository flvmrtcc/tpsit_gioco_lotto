# Martucci Flavio 4inf3
# from gioco_lotto import inserimentoCodiceFiscale
from os import remove
import tkinter as tk
import codicefiscale


def cancellaElementi():
    for widget in finestra.winfo_children():
        widget.destroy()

def graficaInserimentoCodiceFiscale():
    cancellaElementi()
    testo = tk.Label(finestra, text='Inserisci il codice fiscale:', bg="white", font=("Helvetica",25))
    testo.place(x=400, y=120, anchor="center")
    inputCoodicefiscale = tk.Entry()
    inputCoodicefiscale.insert(0,"")
    inputCoodicefiscale.place(x=400, y=200, anchor="center")
    
    bottoneInvioCodicefiscale = tk.Button(text="Conferma", command=lambda:inserimentoCodiceFiscale(inputCoodicefiscale))
    bottoneInvioCodicefiscale.place(x=400, y=230, anchor="center")

def inserimentoCodiceFiscale(inputCoodicefiscale):
    if inputCoodicefiscale.get():
        codice_fiscale = inputCoodicefiscale.get()
        valido = controllaValiditaCodiceFiscale(codice_fiscale)
        if valido:
            print(str(codice_fiscale) + "preso")
        else:
            print("inserire un codice valido")
            # codice_fiscale = input("Inserisci il codice fiscale:")
        # return codice_fiscale

def controllaValiditaCodiceFiscale(codice_fiscale):
    if(codicefiscale.isvalid(codice_fiscale)):
        return True
    else:
        return False




def menuPrincipale():
    testoLotto = tk.Label(finestra, text='Lotto', bg="white", font=("Helvetica",50))
    testoLotto.place(x=400, y=120, anchor="center")
    # testoLotto.grid(row=0, column=0, sticky="N")

    bottoneAvviaPartita = tk.Button(text="Nuova partita", command=graficaInserimentoCodiceFiscale)
    bottoneAvviaPartita.place(x=400, y=300, anchor="center")
    # bottoneAvviaPartita.grid(row=1, column=0, sticky="N")




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

