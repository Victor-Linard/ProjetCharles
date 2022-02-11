import pandas as pd
from apps import Compte
from datetime import datetime
from csv import DictWriter


def verification_compte_avant_connexion(pseudo,paswd_saisi):
    if Compte.verification_compte(pseudo):
        compte = pd.read_csv("Data/comptes.csv")
        paswd = list(compte[compte["pseudo"]==pseudo].values)[0][4]
        if paswd ==Compte.hashPassword(paswd_saisi):
            log_file(pseudo)
            return infos_user(pseudo)
        else:
            return 0
    else:
        return False


# cette fonction enregistre les informations de connexion
def log_file(user):
    datetimes = datetime.now()
    log = {"date": datetimes, "user": user}
    headersCSV = ["date", "user"]
    with open('Data/loggs_file.csv', 'a', newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
        dictwriter_object.writerow(log)
        f_object.close()


def infos_user(user):
    compte = pd.read_csv("Data/comptes.csv")
    infos = list(compte[compte["pseudo"] == user].values)[0]
    nom = infos[0]
    prenom = infos[1]
    email = infos[2]
    pseudo = infos[3]
    return nom,prenom,email,pseudo


def statconnexion(pseudo):
    logs = pd.read_csv("Data/loggs_file.csv")
    logsUsers = logs[logs["user"]==pseudo]
    nbrConnexion = len(logsUsers)
    dernierConnexion = logs.tail(1).values[0][0]
    return nbrConnexion, dernierConnexion
