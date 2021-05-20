# Martucci Flavio 4inf3
from datetime import date, datetime
import tkinter as tk
import codicefiscale
import numpy as np
import os


def cancellaElementi():     # rimuove tutti gli elementi della finestra
    for widget in finestra.winfo_children():
        widget.destroy()

def menuPrincipale():       # schermata grafica del menu principale
    cancellaElementi()
    testoLotto = tk.Label(finestra, text='Lotto', bg="white", font=("Helvetica",50,"bold"))
    testoLotto.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")

    bottoneAvviaPartita = tk.Button(text="Nuova giocata", height=3, width=20, bg="lightgreen", font=("Helvetica",20, "bold"), command=graficaInserimentoUsername)
    bottoneAvviaPartita.place(x=DIMENSIONE_FINESTRA_X/2, y=300, anchor="center")


# Inserimento username
def graficaInserimentoUsername():   # schermata grafica per l'inserimento dell'username
    cancellaElementi()
    testo = tk.Label(finestra, text='Inserisci il tuo username:', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    inputUsername = tk.Entry()
    inputUsername.configure(font=("Helvetica", 12), bg="lightgray")
    inputUsername.insert(0,"")
    inputUsername.place(x=DIMENSIONE_FINESTRA_X/2, y=200, height=40, width=300, anchor="center")

    bottoneInvioUsername = tk.Button(text="Conferma", font=("Helvetica",12, "bold"), command=lambda:inserimentoUsername(inputUsername))
    bottoneInvioUsername.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

def inserimentoUsername(inputUsername):
    global dati_utente
    if controlloInserimentoUsername(inputUsername.get()):   # controlla l'username inserito
        dati_utente["username"] = inputUsername.get()
        graficaInserimentoCodiceFiscale()                   # passa alla schermata di inserimento del codice fiscale
    else:
        testoErrore = tk.Label(text="L'username deve contenere tra i 3 e i 15 caratteri", bg="white", fg="red", font=("Helvetica",12))
        testoErrore.place(x=DIMENSIONE_FINESTRA_X/2, y=350, anchor="center")

def controlloInserimentoUsername(username):
    if len(username) >= 3 and len(username) <= 15:  # controlla il minimo e massimo di caratteri dell'username inserito
        return True
    return False

# Inserimento codice fiscale
def graficaInserimentoCodiceFiscale():   # schermata grafica per l'inserimento del codice fiscale
    cancellaElementi()
    testo = tk.Label(finestra, text='Inserisci il tuo codice fiscale:', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    inputCoodicefiscale = tk.Entry()
    inputCoodicefiscale.configure(font=("Helvetica", 12), bg="lightgray")
    inputCoodicefiscale.insert(0,"SDYSTO40S06G159X")
    inputCoodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=200, height=40, width=300, anchor="center")
    
    bottoneInvioCodicefiscale = tk.Button(text="Conferma", font=("Helvetica",12, "bold"), command=lambda:inserimentoCodiceFiscale(inputCoodicefiscale))
    bottoneInvioCodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

def inserimentoCodiceFiscale(inputCoodicefiscale):
    global dati_utente
    codice_fiscale = (inputCoodicefiscale.get()).upper() # prende dalla casella il codice fiscale inserito
    valido = codicefiscale.isvalid(codice_fiscale)  # cpntrolla se è valido
    if valido:
        dati_utente["codice_fiscale"] = codice_fiscale
        if verficaSeMaggiorenne(codice_fiscale):    # controlla se è maggiorenne
            graficaSceltaGiocata()
        else:                           # se non è maggiorenne
            cancellaElementi()
            testoMinorenne = tk.Label(finestra, text='Devi essere maggiorenne per poter giocare!', bg="white", fg="red", font=("Helvetica",20, "bold"))
            testoMinorenne.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
            bottoneEsci = tk.Button(text="Esci dal gioco", font=("Helvetica",15, "bold"), command=exit)
            bottoneEsci.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")
    else:
        testoErrore = tk.Label(text="Inserisci un codice fiscale valido", bg="white", fg="red", font=("Helvetica",12))
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
    
    bottoneSceltaGiocata = tk.Button(text="Estratto", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaGiocata("Estratto"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2-200, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="Ambo", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaGiocata("Ambo"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2-100, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="Terno", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaGiocata("Terno"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")
    
    bottoneSceltaGiocata = tk.Button(text="Quaterna", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaGiocata("Quaterna"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2+100, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="Cinquina", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaGiocata("Cinquina"))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2+200, y=250, anchor="center")

def sceltaGiocata(tipoGiocata):
    dati_utente["giocata_scelta"] = tipoGiocata
    graficaSceltaGiocataSecca()

# Scelta se effettuare una giocata secca
def graficaSceltaGiocataSecca():
    cancellaElementi()
    testo = tk.Label(finestra, text='Vuoi effettuare una giocata secca?', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    
    bottoneSceltaGiocata = tk.Button(text="Sì", width=3, font=("Helvetica",20, "bold"), command=lambda:sceltaGiocataSecca(True))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2-50, y=250, anchor="center")

    bottoneSceltaGiocata = tk.Button(text="No", width=3, font=("Helvetica",20, "bold"), command=lambda:sceltaGiocataSecca(False))
    bottoneSceltaGiocata.place(x=DIMENSIONE_FINESTRA_X/2+50, y=250, anchor="center")

def sceltaGiocataSecca(giocataSecca):
    dati_utente["giocata_secca"] = giocataSecca
    if giocataSecca:    # se la giocata è secca fa scegliere la ruota, altrimenti passa direttamente alla scelta dei numeri da giocare
        graficaSceltaRuota()
    else:
        graficaSceltaNumeriDaGiocare()

# Scelta ruota giocata non secca
def graficaSceltaRuota():
    cancellaElementi()
    testo = tk.Label(finestra, text='Scegli la ruota su cui puntare: ', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=120, anchor="center")
    
    bottoneSceltaRuota = tk.Button(text="Torino", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Torino"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-200, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Milano", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Milano"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-100, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Venezia", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Venezia"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")
    
    bottoneSceltaRuota = tk.Button(text="Genova", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Genova"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+100, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Firenze", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Firenze"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+200, y=250, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Roma", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Roma"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-200, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Napoli", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Napoli"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2-100, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Bari", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Bari"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2, y=300, anchor="center")
    
    bottoneSceltaRuota = tk.Button(text="Palermo", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Palermo"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+100, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="Cagliari", width=8, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("Cagliari"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2+200, y=300, anchor="center")

    bottoneSceltaRuota = tk.Button(text="NAZIONALE", width=12, font=("Helvetica",12, "bold"), command=lambda:sceltaRuota("NAZIONALE"))
    bottoneSceltaRuota.place(x=DIMENSIONE_FINESTRA_X/2, y=350, anchor="center")

def sceltaRuota(ruota_scelta):
    dati_utente["ruota_scelta"] = ruota_scelta
    graficaSceltaNumeriDaGiocare()

# Scelta numeri da giocare
def graficaSceltaNumeriDaGiocare() :
    cancellaElementi()
    testo = tk.Label(finestra, text='Scegli i numeri che vuoi giocare: ', bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=100, anchor="center")

    testo2 = tk.Label(finestra, text='(I numeri devono essere compresi tra 1 e 90) ', bg="white", font=("Helvetica",12,"italic"))
    testo2.place(x=DIMENSIONE_FINESTRA_X/2, y=140, anchor="center")

    y1 = 0
    inputNumeri = []
    for i in range(giocatePossibili[dati_utente["giocata_scelta"]]):    # mostra a grafica il numero di caselle per la giocata scelta
        inputNumeri.append(tk.Entry())
        inputNumeri[i].configure(font=("Helvetica", 12), bg="lightgray")
        inputNumeri[i].insert(0,"")
        inputNumeri[i].place(x=DIMENSIONE_FINESTRA_X/2, y=200+y1, height=40, width=300, anchor="center")
        y1 += 50
    bottoneInvioCodicefiscale = tk.Button(text="Conferma", font=("Helvetica",12, "bold"), command=lambda:sceltaNumeriDaGiocare(inputNumeri))
    bottoneInvioCodicefiscale.place(x=DIMENSIONE_FINESTRA_X/2, y=200+y1+10, anchor="center")

def sceltaNumeriDaGiocare(inputNumeriScelti):
    elencoValido = True
    numeriScelti = []
    for num in inputNumeriScelti:       # crea l'array contenente i numeri scelti
        numeriScelti.append(num.get())
    
    pos_numero = 0
    for num in numeriScelti:    # esegue il ciclo di controllo per ogni numero inserito
        numeroValido = False
        if len(numeriScelti) == giocatePossibili[dati_utente["giocata_scelta"]]:    # controlla che siano stati inseriti tutti i numeri in base alla giocata scelta
            if num.isdecimal():
                if int(num) >= 1 and int(num) <= 90:    # controlla che il numero inserito sia compreso tra 1 e 90
                    if numeriScelti.count(num) == 1:    # controlla che il numero sia presente una sola volta nell'array dei numeri scelti
                        numeroValido = True
        if numeroValido:    # cambia il colore della casella in base alla correttezza del numero inserito
            inputNumeriScelti[pos_numero].configure(bg="lightgreen")
        else:
            inputNumeriScelti[pos_numero].configure(bg="red")
        
        if not numeroValido:    # se viene trovato un numero non valido l'elenco non è valido
            elencoValido = False
        pos_numero += 1

    if elencoValido:
        dati_utente["numeri_scelti"] = numeriScelti
        graficaSceltaImportoDaGiocare()
    else:
        testoErrore = tk.Label(text="Sono stati inseriti alcuni numeri non validi.\nInserisci dei numeri da giocare validi!", bg="white", fg="red", font=("Helvetica",12))
        testoErrore.place(x=DIMENSIONE_FINESTRA_X/2, y=550, anchor="center")

# Scelta importo da giocare
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

    bottoneInvioImportoEuro = tk.Button(text="Conferma", font=("Helvetica",12, "bold"), command=lambda:controlloSceltaImportoDaGiocare(inputImportoEuro))
    bottoneInvioImportoEuro.place(x=DIMENSIONE_FINESTRA_X/2, y=250, anchor="center")

def controlloSceltaImportoDaGiocare(inputImportoEuro):
    valido = False
    numero = inputImportoEuro.get()
    if numero.isdecimal():  # controlla che sia stato inserito un valore numerico
        if int(numero) >= 1 and int(numero) <= 200:
            valido = True

    if not valido:              # Se l'importo inserito non è valido mostra l'errore
        inputImportoEuro.configure(bg="red")
        testoErrore = tk.Label(text="Inserisci un importo da giocare valido", bg="white", fg="red", font=("Helvetica",12))
        testoErrore.place(x=DIMENSIONE_FINESTRA_X/2, y=350, anchor="center")

    if valido:
        cancellaElementi()
        dati_utente["importo_giocato"] = numero
        ruote_estrazione = estrazione()

        if dati_utente["giocata_secca"]:        # se la giocata è secca
            dati_utente["vincita_totale"] = calcoloPunteggioSecca(dati_utente["ruota_scelta"], dati_utente["numeri_scelti"], dati_utente["importo_giocato"], ruote_estrazione)
        else:
            dati_utente["vincita_totale"] = calcoloPunteggioSuTutteLeRuote(dati_utente["numeri_scelti"], dati_utente["importo_giocato"], ruote_estrazione)

        graficaFinale()


# Estrazione
def salvaEstrazione(ruote_estrazione, nomeFileEstrazione):
    np.save(nomeFileEstrazione, ruote_estrazione)   # salva l'estrazione nel file

def leggiEstrazione(nomeFileEstrazione):
    read_dictionary = np.load(f'{nomeFileEstrazione}.npy',allow_pickle='TRUE').item()   # prende l'estrazione dal file
    return read_dictionary

def estrazione():
    global dataEstrazione
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
    dataEstrazione = nomeFileEstrazione     # salva nella variabile globale la data dell'ultima estrazione 
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
            for num in numeri_scelti:           # effettua il controllo seguente per tutti i numeri inseriti
                if int(num) in numeriEstrazione:    # controlla se il numero inserito è presente nell'array dell'estrazione
                    numeriCorretti += 1
    if numeriCorretti != 0 and len(numeri_scelti) == numeriCorretti:
        vincitaTotale = (int(vinciteGiocataSecca[str(numeriCorretti)]) * int(importo_giocato))
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
            for num in numeri_scelti:           # effettua il controllo seguente per tutti i numeri inseriti
                if int(num) in numeriEstrazione:    # controlla se il numero inserito è presente nell'array dell'estrazione
                    numeriCorretti += 1
            if numeriCorretti != 0 and len(numeri_scelti) == numeriCorretti:
                vincitaTotale += (int(vinciteGiocata[str(numeriCorretti)]) * int(importo_giocato))
    return vincitaTotale

# Grafica che mostra la vincita
def graficaFinale():
    testo = tk.Label(finestra, text="Risultato della giocata: ", bg="white", font=("Helvetica",25))
    testo.place(x=DIMENSIONE_FINESTRA_X/2, y=100, anchor="center")

    if dati_utente["vincita_totale"] > 0:
        testo2 = tk.Label(finestra, text=f"Complimenti {dati_utente['username']}! \nLa tua vincita è di: {dati_utente['vincita_totale']} euro.", bg="white", fg="green", font=("Helvetica",25))
    else:
        testo2 = tk.Label(finestra, text="Non hai vinto, riprova.", bg="white", fg="red", font=("Helvetica",25))
    testo2.place(x=DIMENSIONE_FINESTRA_X/2, y=260, anchor="center")

    testo3 = tk.Label(finestra, text=f"Data ultima estrazione: {dataEstrazione} alle ore 18:00", bg="white", fg="black", font=("Helvetica",13))
    testo3.place(x=DIMENSIONE_FINESTRA_X-200, y=580, anchor="center")

    if dati_utente['giocata_secca']: # stringa del tipo di giocata effettuata
        strTipoGiocata = f"Sulla ruota: {dati_utente['ruota_scelta']}"
    else:
        strTipoGiocata = "Su tutte le ruote"
    testo4 = tk.Label(finestra, text=f"Numeri giocati: {dati_utente['numeri_scelti']}\n {strTipoGiocata}", bg="white", fg="gray", font=("Helvetica",13))
    testo4.place(x=DIMENSIONE_FINESTRA_X/2, y=180, anchor="center")
    bottoneRigioca = tk.Button(text="Nuova giocata", font=("Helvetica",12, "bold"), command=menuPrincipale)
    bottoneRigioca.place(x=DIMENSIONE_FINESTRA_X/2-80, y=440, anchor="center")
    bottoneEsci = tk.Button(text="Esci dal gioco", font=("Helvetica",12, "bold"), command=exit)
    bottoneEsci.place(x=DIMENSIONE_FINESTRA_X/2+80, y=440, anchor="center")




# Globali   ---------------------------------------------
DIMENSIONE_FINESTRA_X = 800
DIMENSIONE_FINESTRA_Y = 600
dataEstrazione = ""

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
