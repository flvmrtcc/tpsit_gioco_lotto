# Martucci Flavio 4inf3
from datetime import date
import tkinter as tk
import codicefiscale


def cancellaElementi():
    for widget in finestra.winfo_children():
        widget.destroy()

def graficaInserimentoCodiceFiscale():
    cancellaElementi()
    testo = tk.Label(finestra, text='Inserisci il tuo codice fiscale:', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    inputCoodicefiscale = tk.Entry()
    inputCoodicefiscale.configure(font=("Helvetica", 12))
    inputCoodicefiscale.insert(0,"SDYSTO40S06G159X")
    inputCoodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=200, height=40, width=300, anchor="center")
    
    bottoneInvioCodicefiscale = tk.Button(text="Conferma", command=lambda:inserimentoCodiceFiscale(inputCoodicefiscale))
    bottoneInvioCodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

def inserimentoCodiceFiscale(inputCoodicefiscale):
    if inputCoodicefiscale.get():
        codice_fiscale = inputCoodicefiscale.get()
        valido = controllaValiditaCodiceFiscale(codice_fiscale)
        if valido:
            if verficaSeMaggiorenne(codice_fiscale):
                print("è maggiorenne")
                menuSceltaGiocata()
            else:
                print("non è maggiorenne")
                exit()
        else:
            testoErrore = tk.Label(text="Inserisci un codice fiscale valido", bg="white", fg="red", font=("Helvetica",11))
            testoErrore.place(x=DIMENSIONE_FINESTRA_X/2, y=350, anchor="center")

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


def menuSceltaGiocata():
    cancellaElementi()
    testo = tk.Label(finestra, text='Scegli il tipo di giocata che si desidera effettuare:', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")


def menuPrincipale():
    testoLotto = tk.Label(finestra, text='Lotto', bg="white", font=("Helvetica",50,"bold"))
    testoLotto.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")

    bottoneAvviaPartita = tk.Button(text="Nuova partita", height=3, width=20, bg="lightgreen", font=("Helvetica",20, "bold"), command=graficaInserimentoCodiceFiscale)
    bottoneAvviaPartita.place(x=DIMENSIONE_FINESTRA_X/2, y=300, anchor="center")



finestra = tk.Tk()
DIMENSIONE_FINESTRA_X = 800
DIMENSIONE_FINESTRA_Y = 600

finestra.title("Gioco lotto - Martucci")
finestra.geometry(f"{DIMENSIONE_FINESTRA_X}x{DIMENSIONE_FINESTRA_Y}")
finestra.configure(background="white")
finestra.grid_columnconfigure(0, weight=1)

menuPrincipale()





finestra.mainloop()

