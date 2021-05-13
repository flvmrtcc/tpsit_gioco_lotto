# Martucci Flavio 4inf3
from datetime import date, datetime
import codicefiscale
import numpy as np
import os


# Inserimento username
def inserimentoUsername():
    username = input("Inserisci l'username: ")
    return username

# Controlli codice fiscale
def inserimentoCodiceFiscale():
    codice_fiscale = 0
    valido = False
    while not valido:
        codice_fiscale = input("Inserisci il codice fiscale:")
        valido = controllaValiditaCodiceFiscale(codice_fiscale)
    return codice_fiscale

def controllaValiditaCodiceFiscale(codice_fiscale):
    if(codicefiscale.isvalid(codice_fiscale)):
        print("Il codice fiscale inserito è valido.")
        return True
    else:
        print("Il codice fiscale inserito non è valido.")
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
    # print(giorno_codice + " " + mese_codice + " " + anno)
    if (data_attuale.year - anno) > 18:
        return True
    elif (data_attuale.year - anno) == 18:
        if data_attuale.month >= mese_codice:
            if data_attuale.day >= giorno_codice:
                return True
    return False

# Scelta giocata da effettuare
def sceltaGiocata(giocatePossibili):
    valido = False
    while not valido:
        print("Segli il tipo di giocata che si desidera effettuare: ")
        print("(Giocate possibili: Estratto, Ambo, Terno, Quaterna, Cinquina)")
        giocata_scelta = input()
        if str(giocata_scelta) in giocatePossibili:
            valido = True
        else:
            print(f"'{giocata_scelta}' non è una giocata possibile")
    return giocata_scelta

def sceltaGiocataSecca():
    valido = False
    while not valido:
        tipo_giocata = str(input("Si desidera effettuare una giocata secca? (Y per si, N per no) "))
        if tipo_giocata == "Y" or tipo_giocata == "N":
            valido = True
    if tipo_giocata == "Y":
        return True
    else:
        return False

# Scelta della ruota su cui puntare se la giocata è secca
def sceltaRuota():
    ruote = ['Torino', 'Milano', 'Venezia', 'Genova', 'Firenze', 'Roma', 'Napoli', 'Bari', 'Palermo', 'Cagliari', 'NAZIONALE']
    stringaRuoteEstenti = "Ruote disponibili: "
    for element in ruote:
        stringaRuoteEstenti = f"{stringaRuoteEstenti} {element},"
    stringaRuoteEstenti = stringaRuoteEstenti[:len(stringaRuoteEstenti)-1] + ".\n"
    valido = False
    while not valido:
        ruota_puntata = input(f"Su quale ruota si vuole puntare? \n{stringaRuoteEstenti}")
        if str(ruota_puntata) in ruote:
            valido = True
        else:
            print(f"{ruota_puntata} non è una ruota esistente")
    return ruota_puntata

# Scelta dei numeri da giocare
def sceltaNumeriDaGiocare(numeriDaGiocare):
    numeri_scelti = []
    for i in range(numeriDaGiocare):
        valido = False
        while not valido:
            numero = input("Inserisci un numero da giocare compreso da 1 e 90: ")
            if numero.isdecimal():
                numero = int(numero)
                if numero >= 1 and numero <= 90:
                    if not(numero in numeri_scelti):
                        valido = True
                    else:
                        print("Inserisci un numero diverso da quelli già scelti")
                else:
                    print(f"{numero} non è un numero valdo")
            else:
                print(f"{numero} non è un numero valdo")
        numeri_scelti.append(numero)
    return numeri_scelti


def inserisciImportoDaGiocare():
    valido = False
    while not valido:
        numero = input("Inserisci l'importo in euro da giocare (giocata minimo 1 euro, massimo 200 euro): ")
        if numero.isdecimal():
            if int(numero) >= 1 and int(numero) <= 200:
                valido = True
            else:
                print(f"{numero} non è una giocata valida")
        else:
            print(f"{numero} non è una giocata valida")
    return numero

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
    vinciteGiocataSecca = {
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
    vinciteGiocata = {
        "1" : 5,
        "2" : 25,
        "3" : 450,
        "4" : 12000,
        "5" : 600000
    }
    vincitaTotale = 0
    for ruota,numeriEstrazione in ruote_estrazione.items():     # esegue il for per ogni ruota
        if ruota != "NAZIONALE":
            numeriCorretti = 0
            for num in numeri_scelti:
                if num in numeriEstrazione:
                    numeriCorretti += 1
            if numeriCorretti != 0 and len(numeri_scelti) == numeriCorretti:
                vincitaTotale += (int(vinciteGiocata[str(numeriCorretti)]) * int(importo_giocato))
    return vincitaTotale


######################################################################
def mainGioco():
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

    print("Benvenuto nel gioco del lotto!")
    # Inserisci username
    dati_utente["username"] = inserimentoUsername()

    # Pt. 1 - I giocatori devono essere maggiorenni.
    dati_utente["codice_fiscale"] = inserimentoCodiceFiscale()
    # print(f"Il codice fiscale inserito è: {codice_fiscale}")

    if verficaSeMaggiorenne(dati_utente["codice_fiscale"]):
        print("è maggiorenne")
    else:
        print("Devi essere maggiorenne per poter giocare!")
        exit()

    # Pt. 2 - Chiedere al giocatore che tipo di giocata vuole fare.
    giocatePossibili = {
        "Estratto" : 1,
        "Ambo" : 2,
        "Terno" : 3,
        "Quaterna" : 4,
        "Cinquina" : 5
    }
    dati_utente["giocata_scelta"] = sceltaGiocata(giocatePossibili)
    # numeriDaGiocare = giocatePossibili[giocata_scelta]

    # Pt. 3 - Chiedere la ruota se la giocata è secca altrimenti vorrà dire che è su tutte le ruote.
    dati_utente["giocata_secca"] = sceltaGiocataSecca()

    if dati_utente["giocata_secca"]:
        dati_utente["ruota_scelta"] = sceltaRuota()
    
    # Pt. 4 - Chiedere che numeri vuole giocare.
    dati_utente["numeri_scelti"] = sceltaNumeriDaGiocare(giocatePossibili[dati_utente["giocata_scelta"]])
    print(dati_utente["numeri_scelti"])

    # Pt. 5 - Chiedere quanto vuole giocare.
    dati_utente["importo_giocato"] = inserisciImportoDaGiocare()
    print("Importo giocato: " + dati_utente["importo_giocato"] + " euro")


    ruote_estrazione = estrazione()
    # print(ruote_estrazione)


    if dati_utente["giocata_secca"]:
        dati_utente["vincita_totale"] = calcoloPunteggioSecca(dati_utente["ruota_scelta"], dati_utente["numeri_scelti"], dati_utente["importo_giocato"], ruote_estrazione)
    else:
        dati_utente["vincita_totale"] = calcoloPunteggioSuTutteLeRuote(dati_utente["numeri_scelti"], dati_utente["importo_giocato"], ruote_estrazione)
    print(f"La vincita è di: " + str(dati_utente["vincita_totale"]) + " euro")



mainGioco()

