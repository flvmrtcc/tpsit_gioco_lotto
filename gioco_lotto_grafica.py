# Martucci Flavio 4inf3
from datetime import date
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
            if verficaSeMaggiorenne(codice_fiscale):
                print("è maggiorenne")
            else:
                print("non è maggiorenne")
                exit()
        else:
            print("inserire un codice valido")

def controllaValiditaCodiceFiscale(codice_fiscale):
    if(codicefiscale.isvalid(codice_fiscale)):
        return True
    else:
        return False


def verficaSeMaggiorenne(codice_fiscale):
    dataNascita = codicefiscale.get_birthday(codice_fiscale)
    giorno_codice = dataNascita[0:2]
    mese_codice = dataNascita[3:5]
    anno_codice = dataNascita[6:8]
    if int(anno_codice) < 25:   # 2025
        anno = f"20{anno_codice}"
    else:
        anno = f"19{anno_codice}"
    print(giorno_codice + " " + mese_codice + " " + anno)
    data_attuale = date.today()

    if (data_attuale.year - int(anno)) > 18:
        return True
    elif (data_attuale.year - int(anno)) == 18:
        if data_attuale.month >= int(mese_codice):
            if data_attuale.day >= int(giorno_codice):
                return True
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





finestra.mainloop()

