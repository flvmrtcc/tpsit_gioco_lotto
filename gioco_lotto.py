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

print("Benvenuto nel gioco del lotto!")
codice_fiscale = inserimentoCodiceFiscale()
# print(f"Il codice fiscale inserito è: {codice_fiscale}")

if verficaSeMaggiorenne(codice_fiscale):
    print("è maggiorenne")
else:
    print("non è maggiorenne")

