# Martucci Flavio 4inf3
from datetime import date
import tkinter as tk
import codicefiscale


def cancellaElementi():
    for widget in finestra.winfo_children():
        widget.destroy()

# Inserimento username
def graficaInserimentoUsername():
    cancellaElementi()
    testo = tk.Label(finestra, text='Inserisci il tuo username:', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    inputUsername = tk.Entry()
    inputUsername.configure(font=("Helvetica", 12))
    inputUsername.insert(0,"")
    inputUsername.place(x=DIMENSIONE_FINESTRA_X/2, y=200, height=40, width=300, anchor="center")

    bottoneInvioCodicefiscale = tk.Button(text="Conferma", command=lambda:inserimentoUsername(inputUsername))
    bottoneInvioCodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

def inserimentoUsername(inputUsername):
    global dati_utente
    dati_utente["username"] = inputUsername.get()
    graficaInserimentoCodiceFiscale()

# Inserimento codice fiscale
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
    global dati_utente
    if inputCoodicefiscale.get():
        codice_fiscale = inputCoodicefiscale.get()
        valido = controllaValiditaCodiceFiscale(codice_fiscale)
        if valido:
            dati_utente["codice_fiscale"] = inputCoodicefiscale.get()
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
    giorno_codice = int(dataNascita[0:2])
    mese_codice = int(dataNascita[3:5])
    anno_codice = int(dataNascita[6:8])
    data_attuale = date.today()

    if anno_codice <= int(str(data_attuale.year)[2:4]):   # se le ultime due cifre dell'anno preso dal codice fiscale sono minori o uguali a quelle dell'anno attuale
        anno = int(f"20{anno_codice}")
    else:
        anno = int(f"19{anno_codice}")
    if (data_attuale.year - anno) > 18:
        return True
    elif (data_attuale.year - anno) == 18:
        if data_attuale.month >= mese_codice:
            if data_attuale.day >= giorno_codice:
                return True
    return False

def menuSceltaGiocata():
    cancellaElementi()
    testo = tk.Label(finestra, text='Scegli il tipo di giocata che si desidera effettuare:', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")


def menuPrincipale():
    testoLotto = tk.Label(finestra, text='Lotto', bg="white", font=("Helvetica",50,"bold"))
    testoLotto.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")

    bottoneAvviaPartita = tk.Button(text="Nuova partita", height=3, width=20, bg="lightgreen", font=("Helvetica",20, "bold"), command=graficaInserimentoUsername)
    bottoneAvviaPartita.place(x=DIMENSIONE_FINESTRA_X/2, y=300, anchor="center")



DIMENSIONE_FINESTRA_X = 800
DIMENSIONE_FINESTRA_Y = 600

finestra = tk.Tk()
finestra.title("Gioco lotto - Martucci")
finestra.geometry(f"{DIMENSIONE_FINESTRA_X}x{DIMENSIONE_FINESTRA_Y}")
finestra.configure(background="white")
finestra.grid_columnconfigure(0, weight=1)

dati_utente = {
    "username" : "",
    "codice_fiscale" : "",
    "giocata_scelta" : "",
    "giocata_secca" : "",
    "ruota_scelta" : "",
    "importo_giocato" : 0,
    "numeri_scelti" : "",
    "vincita_totale" : 0
}

def mainGioco():
    menuPrincipale()

    print(dati_utente)
    finestra.mainloop()


mainGioco()
