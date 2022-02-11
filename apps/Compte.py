import pandas as pd
from csv import DictWriter
import hashlib


def insertion_user(nom,prenom,pseudo,email,paswd):
    user = {"nom":nom,"prenom":prenom,"email":email,"pseudo":pseudo,"paswd": hashPassword(paswd)}
    headersCSV=["nom","prenom","email","pseudo","paswd"]
    with open('Data/comptes.csv', 'a', newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
        dictwriter_object.writerow(user)
        f_object.close()
    print(hash("123456"))
    return True


def supression_de_compte(pseudo):
    data = pd.read_csv("Data/comptes.csv")
    data = data.drop(index=data[data["pseudo"] == pseudo].index.values[0])
    data.to_csv("Data/comptes.csv", index=False)
    return True


def verification_compte(pseudo):
    compte = pd.read_csv("Data/comptes.csv")
    return (pseudo in compte['pseudo'].values)


def creation_de_compte(nom,prenom,pseudo,email,paswd):
    if verification_compte(pseudo)==False:
        insertion_user(nom,prenom,pseudo,email,paswd)
        return True
    else:
        return False


def changement_de_mot_passe(pseudo,ancien,nouveau):
    data = pd.read_csv("Data/comptes.csv")
    data.at[data[data["pseudo"] == pseudo].index.values[0], 'paswd'] = hashPassword(nouveau)
    data.to_csv("Data/comptes.csv", index=False)
    return True


def hashPassword(paswd):
    message = hashlib.md5(paswd.encode())
    return message.hexdigest()


def mis_a_jour_compte(liste_des_parm,pseudo):
    data = pd.read_csv("Data/comptes.csv")
    prenom=liste_des_parm[1]
    email=liste_des_parm[2]
    nom=liste_des_parm[0]
    if (nom!=None):
        data.at[data[data["pseudo"] == pseudo].index.values[0], 'nom'] = nom
    if(prenom!=None):
        data.at[data[data["pseudo"] == pseudo].index.values[0], 'prenom'] = prenom
    if(email!=None):
        data.at[data[data["pseudo"] == pseudo].index.values[0], 'email'] = email

    data.to_csv("Data/comptes.csv", index=False)
    return True