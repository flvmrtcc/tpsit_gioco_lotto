# Martucci Flavio 4inf3
from datetime import date
import codicefiscale
import numpy as np
import os

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

# Scelta giocata da effettuare
def sceltaGiocata(giocatePossibili):
    valido = False
    while not valido:
        print("Segli il tipo di giocata che si desidera effettuare: ")
        # print("(Giocate possibili: Estratto, Estratto secco, Ambo, Ambo secco, Terno, Terno secco, Quaterna, Quaterna secca, Cinquina, Cinquina Secca)")
        print("(Giocate possibili: Estratto, Ambo, Terno, Quaterna, Cinquina)")
        giocata_scelta = input()
        if str(giocata_scelta) in giocatePossibili:
            valido = True
        else:
            print(f"{giocata_scelta} non è una giocata possibile")

    return giocata_scelta

def sceltaGiocataSecca():
    valido = False
    while not valido:
        tipo_giocata = input("Si desidera effettuare una giocata secca? (Y per si, N per no) ")
        if str(tipo_giocata) == "Y" or str(tipo_giocata) == "N":
            valido = True
    if tipo_giocata == "Y":
        return True
    else:
        return False

# Scelta della ruota su cui puntare se la giocata è secca
def sceltaRuota(ruote):
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
                if int(numero) >= 1 and int(numero) <= 90:
                    if not(numero in numeri_scelti):
                        valido = True
                    else:
                        print("Inserisci un numero diverso da quelli già scelti")
                else:
                    print(f"{numero} non è un numero valdo")
            else:
                print(f"{numero} non è un numero valdo")
        numeri_scelti.append(int(numero))
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
def salvaEstrazione(ruote_estrazione):
    np.save(f'{date.today()}', ruote_estrazione)
    # fileEsteazione = open("estrazione", "w")
    # pickle.dump(dictionary_data, a_file)
    # fileEsteazione.close()

def leggiEstrazione():
    read_dictionary = np.load(f'{date.today()}.npy',allow_pickle='TRUE').item()
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
    if not os.path.isfile(f'{date.today()}.npy'):
        for element, valore in ruote_estrazione.items():
            ruote_estrazione[element] = np.random.randint(1, 90,(5))
        salvaEstrazione(ruote_estrazione)
        print("Estrazione effettuata")
    else:
        ruote_estrazione = leggiEstrazione()
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
        vincitaTotale = vinciteGiocataSecca[str(numeriCorretti)]
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
                vincitaTotale += vinciteGiocata[str(numeriCorretti)]

    return vincitaTotale


######################################################################
def gioco():
    # Pt. 1 - I giocatori devono essere maggiorenni.
    print("Benvenuto nel gioco del lotto!")
    codice_fiscale = inserimentoCodiceFiscale()
    # print(f"Il codice fiscale inserito è: {codice_fiscale}")

    if verficaSeMaggiorenne(codice_fiscale):
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
    giocata_scelta = sceltaGiocata(giocatePossibili)
    # numeriDaGiocare = giocatePossibili[giocata_scelta]

    # Pt. 3 - Chiedere la ruota se la giocata è secca altrimenti vorrà dire che è su tutte le ruote.
    giocata_secca = sceltaGiocataSecca()

    ruote = ['Torino', 'Milano', 'Venezia', 'Genova', 'Firenze', 'Roma', 'Napoli', 'Bari', 'Palermo', 'Cagliari', 'NAZIONALE']
    if giocata_secca:
        ruota_scelta = sceltaRuota(ruote)
    
    # Pt. 4 - Chiedere che numeri vuole giocare.
    numeri_scelti = sceltaNumeriDaGiocare(giocatePossibili[giocata_scelta])
    print(numeri_scelti)

    # Pt. 5 - Chiedere quanto vuole giocare.
    importo_giocato = inserisciImportoDaGiocare()
    print(f"Importo giocato {importo_giocato} euro")


    ruote_estrazione = estrazione()
    # print(ruote_estrazione)


    if giocata_secca:
        vincitaTotale = calcoloPunteggioSecca(ruota_scelta, numeri_scelti, importo_giocato, ruote_estrazione)
    else:
        vincitaTotale = calcoloPunteggioSuTutteLeRuote(numeri_scelti, importo_giocato, ruote_estrazione)
    print(f"La vincita è di: {vincitaTotale}")



gioco()

