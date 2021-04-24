from codicefiscale import build
import codicefiscale

def inserimentoCodiceFiscale():
    codiceFiscale = 0
    while not controllaValiditaCodiceFiscale(codiceFiscale):
        codiceFiscale = input("Inserisci il codice fiscale:")
    return codiceFiscale

def controllaValiditaCodiceFiscale(codiceFiscale):
    if(codicefiscale.isvalid(codiceFiscale)):
        print("Il codice fiscale inserito è valido.")
        return True
    else:
        print("Il codice fiscale inserito non è valido.")
        return False

codiceFiscale = inserimentoCodiceFiscale()
print(f"Il codice fiscale inserito è: {codiceFiscale}")



