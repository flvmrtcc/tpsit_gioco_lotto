# Martucci Flavio 4inf3
from datetime import date
from codicefiscale import build
import codicefiscale

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
    anno_codice = dataNascita[6:9]
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


# Pt. 1
print("Benvenuto nel gioco del lotto!")
codice_fiscale = inserimentoCodiceFiscale()
# print(f"Il codice fiscale inserito è: {codice_fiscale}")

if verficaSeMaggiorenne(codice_fiscale):
    print("è maggiorenne")
else:
    print("non è maggiorenne")
    exit()

# Pt. 2
giocatePossibili = {
    "Estratto" : 1,
    "Ambo" : 2,
    "Terno" : 3,
    "Quaterna" : 4,
    "Cinquina" : 5,
}
giocata_scelta = sceltaGiocata(giocatePossibili)
numeriDaGiocare = giocatePossibili[giocata_scelta]
# print(f"{numeriDaGiocare}")

# Pt. 3
giocata_secca = sceltaGiocataSecca()

ruote = ['Torino', 'Milano', 'Venezia', 'Genova', 'Firenze', 'Roma', 'Napoli', 'Bari', 'Palermo', 'Cagliari', 'NAZIONALE']
if giocata_secca:
    ruota_scelta = sceltaRuota(ruote)
    


