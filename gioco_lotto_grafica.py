# Martucci Flavio 4inf3
from datetime import date, datetime
import tkinter as tk
import codicefiscale
import numpy as np
import os


def cancellaElementi():
    for widget in finestra.winfo_children():
        widget.destroy()

# Inserimento username
def graficaInserimentoUsername():
    cancellaElementi()
    testo = tk.Label(finestra, text='Inserisci il tuo username:', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    inputUsername = tk.Entry()
    inputUsername.configure(font=("Helvetica", 12), bg="lightgray")
    inputUsername.insert(0,"")
    inputUsername.place(x=DIMENSIONE_FINESTRA_X/2, y=200, height=40, width=300, anchor="center")

    bottoneInvioUsername = tk.Button(text="Conferma", command=lambda:inserimentoUsername(inputUsername))
    bottoneInvioUsername.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

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
    inputCoodicefiscale.configure(font=("Helvetica", 12), bg="lightgray")
    inputCoodicefiscale.insert(0,"SDYSTO40S06G159X")
    inputCoodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=200, height=40, width=300, anchor="center")
    
    bottoneInvioCodicefiscale = tk.Button(text="Conferma", command=lambda:inserimentoCodiceFiscale(inputCoodicefiscale))
    bottoneInvioCodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

def inserimentoCodiceFiscale(inputCoodicefiscale):
    global dati_utente
    if inputCoodicefiscale.get():
        codice_fiscale = inputCoodicefiscale.get()
        valido = codicefiscale.isvalid(codice_fiscale)
        if valido:
            dati_utente["codice_fiscale"] = inputCoodicefiscale.get()
            if verficaSeMaggiorenne(codice_fiscale):
                graficaSceltaGiocata()
            else:
                exit()
        else:
            testoErrore = tk.Label(text="Inserisci un codice fiscale valido", bg="white", fg="red", font=("Helvetica",11))
            testoErrore.place(x=DIMENSIONE_FINESTRA_X/2, y=350, anchor="center")



def verficaSeMaggiorenne(codice_fiscale):
    dataNascita = codicefiscale.get_birthday(codice_fiscale)    # data di nascita ricavata dal codice fiscale
    giorno_codice = int(dataNascita[0:2])
    mese_codice = int(dataNascita[3:5])
    anno_codice = dataNascita[6:8]
    data_attuale = date.today()                 # data corrente

    if int(anno_codice) <= int(str(data_attuale.year)[2:4]):   # se le ultime due cifre dell'anno preso dal codice fiscale sono minori o uguali a quelle dell'anno attuale
        anno = int(f"20{anno_codice}")
    else:
        anno = int(f"19{anno_codice}")
    
    if (data_attuale.year - anno) > 18:     # controlli per verificare che sia maggiorenne (confronti della data di nascita con la data corrente)
        return True
    elif (data_attuale.year - anno) == 18:
        if data_attuale.month > mese_codice:
            return True
        elif data_attuale.month == mese_codice:
            if data_attuale.day >= giorno_codice:
                return True
    return False                            # se non è maggiorenne la funzione restituisce False, altrimenti True

# Scelta giocata
def graficaSceltaGiocata():
    cancellaElementi()
    testo = tk.Label(finestra, text='Scegli il tipo di giocata da effettuare: ', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    
    bottoneSceltaGiocata = tk.Button(text="Estratto", command=lambda:sceltaGiocata("Estratto"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2-200, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="Ambo", command=lambda:sceltaGiocata("Ambo"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2-100, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="Terno", command=lambda:sceltaGiocata("Terno"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")
    
    bottoneSceltaGiocata = tk.Button(text="Quaterna", command=lambda:sceltaGiocata("Quaterna"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2+100, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="Cinquina", command=lambda:sceltaGiocata("Cinquina"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2+200, y=250, anchor="center")

def sceltaGiocata(tipoGiocata):
    dati_utente["giocata_scelta"] = tipoGiocata
    # print(tipoGiocata)
    graficaSceltaGiocataSecca()


def graficaSceltaGiocataSecca():
    cancellaElementi()
    testo = tk.Label(finestra, text='Vuoi effettuare una giocata secca?', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    
    bottoneSceltaGiocata = tk.Button(text="Sì", command=lambda:sceltaGiocataSecca(True))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2-50, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="No", command=lambda:sceltaGiocataSecca(False))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2+50, y=250, anchor="center")

def sceltaGiocataSecca(giocataSecca):
    dati_utente["giocata_secca"] = giocataSecca
    if giocataSecca:
        graficaSceltaRuota()
    else:
        graficaSceltaNumeriDaGiocare()

def graficaSceltaRuota():
    cancellaElementi()
    testo = tk.Label(finestra, text='Scegli la ruota su cui puntare: ', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    
    bottoneSceltaRuota = tk.Button(text="Torino", command=lambda:sceltaRuota("Torino"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-200, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Milano", command=lambda:sceltaRuota("Milano"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-100, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Venezia", command=lambda:sceltaRuota("Venezia"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")
    
    bottoneSceltaRuota = tk.Button(text="Genova", command=lambda:sceltaRuota("Genova"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+100, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Firenze", command=lambda:sceltaRuota("Firenze"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+200, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Roma", command=lambda:sceltaRuota("Roma"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-200, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Napoli", command=lambda:sceltaRuota("Napoli"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-100, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Bari", command=lambda:sceltaRuota("Bari"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2, y=300, anchor="center")
    
    bottoneSceltaRuota = tk.Button(text="Palermo", command=lambda:sceltaRuota("Palermo"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+100, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Cagliari", command=lambda:sceltaRuota("Cagliari"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+200, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="NAZIONALE", command=lambda:sceltaRuota("NAZIONALE"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2, y=350, anchor="center")

def sceltaRuota(ruota_scelta):
    # print(ruota_scelta)
    dati_utente["ruota_scelta"] = ruota_scelta
    graficaSceltaNumeriDaGiocare()


def graficaSceltaNumeriDaGiocare() :
    cancellaElementi()
    testo = tk.Label(finestra, text='Scegli i numeri che vuoi giocare: ', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=100, anchor="center")

    testo2 = tk.Label(finestra, text='(I numeri devono essere compresi tra 1 e 90) ', bg="white", font=("Helvetica",12,"italic"))
    testo2.place(x=DIMENSIONE_FINESTRA_X/2, y=140, anchor="center")

    y1 = 0
    inputNumeri = []
    for i in range(giocatePossibili[dati_utente["giocata_scelta"]]):
        inputNumeri.append(tk.Entry())
        inputNumeri[i].configure(font=("Helvetica", 12), bg="lightgray")
        inputNumeri[i].insert(0,"")
        inputNumeri[i].place(x=DIMENSIONE_FINESTRA_X/2, y=200+y1, height=40, width=300, anchor="center")
        y1 += 50
    
    bottoneInvioCodicefiscale = tk.Button(text="Conferma", command=lambda:sceltaNumeriDaGiocare(inputNumeri))
    bottoneInvioCodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=200+y1+10, anchor="center")


def sceltaNumeriDaGiocare(inputNumeriScelti):
    elencoValido = True
    numeriScelti = []
    for num in inputNumeriScelti:       # crea l'array contenente i numeri scelti
        numeriScelti.append(num.get())
    
    pos_numero = 0
    for num in numeriScelti:
        numeroValido = False
        if len(numeriScelti) == giocatePossibili[dati_utente["giocata_scelta"]]:
            if num.isdecimal():
                if int(num) >= 1 and int(num) <= 90:    # controlla che il numero inserito sia compreso tra 1 e 90
                    if numeriScelti.count(num) == 1:
                        numeroValido = True
                else:
                    print(f"{num} non è un numero valdo")

        if numeroValido:
            inputNumeriScelti[pos_numero].configure(bg="lightgreen")
        else:
            inputNumeriScelti[pos_numero].configure(bg="red")
        
        if not numeroValido:
            elencoValido = False
        pos_numero += 1

    if elencoValido:
        dati_utente["numeri_scelti"] = numeriScelti
        graficaSceltaImportoDaGiocare()

def graficaSceltaImportoDaGiocare():
    cancellaElementi()
    testo = tk.Label(finestra, text="Inserisci l'importo in euro che vuoi giocare: ", bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=100, anchor="center")

    testo2 = tk.Label(finestra, text='(Minimo 1 euro, massimo 200 euro) ', bg="white", font=("Helvetica",12,"italic"))
    testo2.place(x=DIMENSIONE_FINESTRA_X/2, y=140, anchor="center")

    inputImportoEuro = tk.Entry()
    inputImportoEuro.configure(font=("Helvetica", 12), bg="lightgray")
    inputImportoEuro.insert(0,"1")
    inputImportoEuro.place(x=DIMENSIONE_FINESTRA_X/2, y=200, height=40, width=300, anchor="center")

    bottoneInvioImportoEuro = tk.Button(text="Conferma", command=lambda:controlloSceltaImportoDaGiocare(inputImportoEuro))
    bottoneInvioImportoEuro.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

def controlloSceltaImportoDaGiocare(inputImportoEuro):
    valido = False
    numero = inputImportoEuro.get()
    if numero.isdecimal():  # controlla che sia stato inserito un valore numerico
        if int(numero) >= 1 and int(numero) <= 200:
            valido = True
        else:
            print(f"{numero} non è una giocata valida")
    else:
        print(f"{numero} non è una giocata valida")

    if valido:
        cancellaElementi()
        dati_utente["importo_giocato"] = numero
        ruote_estrazione = estrazione()

        if dati_utente["giocata_secca"]:        # se la giocata è secca
            dati_utente["vincita_totale"] = calcoloPunteggioSecca(dati_utente["ruota_scelta"], dati_utente["numeri_scelti"], dati_utente["importo_giocato"], ruote_estrazione)
        else:
            dati_utente["vincita_totale"] = calcoloPunteggioSuTutteLeRuote(dati_utente["numeri_scelti"], dati_utente["importo_giocato"], ruote_estrazione)

        print(ruote_estrazione)
        print(dati_utente["numeri_scelti"])
        print(dati_utente["vincita_totale"])
        if dati_utente["vincita_totale"] > 0:
            print(f"Complimenti " + dati_utente["username"] + "! La tua vincita è di: " + str(dati_utente["vincita_totale"]) + " euro.")
        else:
            print("Non hai vinto, riprova.")


# Estrazione
def salvaEstrazione(ruote_estrazione, nomeFileEstrazione):
    np.save(nomeFileEstrazione, ruote_estrazione)   # salva l'estrazione nel file

def leggiEstrazione(nomeFileEstrazione):
    read_dictionary = np.load(f'{nomeFileEstrazione}.npy',allow_pickle='TRUE').item()   # prende l'estrazione dal file
    return read_dictionary

def estrazione():
    ruote_estrazione = {
        "Torino" : [],
        "Milano" : [],
        "Venezia" : [],
        "Genova" : [],
        "Firenze" : [],
        "Roma" : [],
        "Napoli" : [],
        "Bari" : [],
        "Palermo" : [],
        "Cagliari" : [],
        "NAZIONALE" : []
    }
    oraAttuale = datetime.now().time().hour
    dataAttuale = date.today()
    giornoEstrazione = dataAttuale.day
    if oraAttuale < 20:                 # se non sono passate le 20 si guarda l'estrazione precedente
        giornoEstrazione -= 1
    nomeFileEstrazione = f'{dataAttuale.year}-{dataAttuale.month}-{giornoEstrazione}'

    if not os.path.isfile(f"{nomeFileEstrazione}.npy"):     # controlla se esiste già il file dell'estrazione
        for element, valore in ruote_estrazione.items():
            ruote_estrazione[element] = np.random.randint(1, 90,(5))    # estrae 5 numeri casuali per ogni ruota
        salvaEstrazione(ruote_estrazione, nomeFileEstrazione)           # crea il file e salva l'estrazione
        print("Estrazione effettuata")
    else:
        ruote_estrazione = leggiEstrazione(nomeFileEstrazione)      # se esiste prende le ruote già estratte in precedenza dal file
        print("File estrazione già esistente")
    return ruote_estrazione



# Calcolo punteggio
def calcoloPunteggioSecca(ruota_scelta, numeri_scelti, importo_giocato, ruote_estrazione):
    vinciteGiocataSecca = {     # dizionario per indicare le vincite per ogni tipo di giocata
        "1" : 55,
        "2" : 250,
        "3" : 4500,
        "4" : 120000,
        "5" : 6000000
    }
    numeriCorretti = 0
    vincitaTotale = 0
    for ruota,numeriEstrazione in ruote_estrazione.items():     # esegue il for per ogni ruota
        if ruota_scelta == ruota:   # se la ruota corrente è quella scelta
            print(f"la ruota scelta è {ruota}")
            print(f"i numeri usciti sono: {numeriEstrazione}")
            for num in numeri_scelti:
                if num in numeriEstrazione:
                    numeriCorretti += 1
    if numeriCorretti != 0 and len(numeri_scelti) == numeriCorretti:
        vincitaTotale = (vinciteGiocataSecca[str(numeriCorretti)] * importo_giocato)
    return vincitaTotale

def calcoloPunteggioSuTutteLeRuote(numeri_scelti, importo_giocato, ruote_estrazione):
    vinciteGiocata = {          # dizionario per indicare le vincite per ogni tipo di giocata
        "1" : 5,
        "2" : 25,
        "3" : 450,
        "4" : 12000,
        "5" : 600000
    }
    vincitaTotale = 0
    for ruota,numeriEstrazione in ruote_estrazione.items():     # esegue il for per ogni ruota
        if ruota != "NAZIONALE":            # la ruota nazionale viene saltata quando si gioca su tutte le ruote
            numeriCorretti = 0
            for num in numeri_scelti:
                if num in numeriEstrazione:
                    numeriCorretti += 1
            if numeriCorretti != 0 and len(numeri_scelti) == numeriCorretti:
                vincitaTotale += (int(vinciteGiocata[str(numeriCorretti)]) * int(importo_giocato))
    return vincitaTotale


def menuPrincipale():
    testoLotto = tk.Label(finestra, text='Lotto', bg="white", font=("Helvetica",50,"bold"))
    testoLotto.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")

    bottoneAvviaPartita = tk.Button(text="Nuova partita", height=3, width=20, bg="lightgreen", font=("Helvetica",20, "bold"), command=graficaInserimentoUsername)
    bottoneAvviaPartita.place(x=DIMENSIONE_FINESTRA_X/2, y=300, anchor="center")


# Globali
DIMENSIONE_FINESTRA_X = 800
DIMENSIONE_FINESTRA_Y = 600

finestra = tk.Tk()
finestra.title("Gioco lotto - Martucci")
finestra.geometry(f"{DIMENSIONE_FINESTRA_X}x{DIMENSIONE_FINESTRA_Y}")
finestra.configure(background="white")
finestra.grid_columnconfigure(0, weight=1)
finestra.resizable(False,False)     # impedisce il ridimensionamento della finestra

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

giocatePossibili = {            # dizionario per indicare quanti numeri scergliere per ogni tipo di giocata
        "Estratto" : 1,
        "Ambo" : 2,
        "Terno" : 3,
        "Quaterna" : 4,
        "Cinquina" : 5
    }


def mainGioco():
    menuPrincipale()

    finestra.mainloop()


mainGioco()
