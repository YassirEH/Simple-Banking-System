import random
import csv

# dictionary
Compte = {}
ClientCompte = {}
Client = {}


def ajouterClient():
    genererNumCompte = lambda numCl: int(str(numCl) + str(random.randint(0, 100)).zfill(2))
    numCl = int(input("Entrez le numéro du client: "))
    MPC = input("Entrez le code secret: ")
    numC = genererNumCompte(numCl)
    SoldeC = float(input("Entrez le solde initial de votre compte: "))
    if numCl in Client:
        print(f"Le client {numCl} existe déjà!")
        return mainMenu()
    Client[numCl] = MPC
    Compte[numC] = SoldeC
    ClientCompte[numCl] = numC
    print(f"Le compte {numC} avec le code {MPC} a été ajouté avec succès pour le client {numCl}!")


def supprimerClient(numC):
    if numC not in Compte:
        print(f"Pas de compte associe au compte suivant: {numC}!")
        return mainMenu()
    numCl = ClientCompte[numC]
    del Client[numCl]
    del Compte[numC]
    del ClientCompte[numC]
    print(f"Le compte {numC} associe au client {numCl} a ete supprime avec succes!")


def afficher_solde(numCl):
    if numCl not in ClientCompte:
        print(f"Client {numCl} n'a pas de compte associé.")
        return
    numC = ClientCompte[numCl]
    solde = Compte[numC]
    print(f"Le solde du compte {numC} est de {str(solde)} DH.")


def modifierMPclient(numCl, MPC, nouveauMP):
    if Client[numCl] != str(MPC):
        print("Mod de passe saisi est incorrect")
        return mainMenu()
    Client[numCl] = nouveauMP
    print("Votre mot de passe est modifie avec succes!")


def deposit(numCl, soldeD):
    numC = ClientCompte[numCl]
    Compte[numC] += soldeD
    print(f"Votre mantant a été déposé avec succès. Votre nouveau solde est de: {Compte[numC]}")


def retirer(numCl, soldeR):
    numC = ClientCompte[numCl]
    if Compte[numC] >= soldeR:
        Compte[numC] -= soldeR
        print(f"Montant retiré avec succès. Votre nouveau solde est: {Compte[numC]}! ")
    else:
        print("Solde insuffisant pour retirer ce montant.")


def EcrireFichierCSV():
    with open('clients.csv', mode='w', newline='') as csvfile:
        fieldnames = ['Numero de client', 'Code secret']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for numCl, MPC in Client.items():
            writer.writerow({'Numero de client': numCl, 'Code secret': MPC})
    print('Le fichier clients.csv a été créé avec succès.')


def mainMenu():
    print("Bienvenue a notre bank! "
          "\n1) Agent de la bank."
          "\n2) Espace client."
          "\n9) Quitter")
    choice = input("Choisir une action: ")
    if choice == "1":
        agentMenu()
    elif choice == "2":
        clientMenu()
    elif choice == "9":
        print("Merci")
        return
    else:
        print("Choix invalide...")
        mainMenu()


def agentMenu():
    print("\nMenu d'agent:"
          "\n1) Ajouter un compte."
          "\n2) Supprimer un compte."
          "\n3) Enregistrer les numéros de clients et codes secrets."
          "\n9) Retourner.")
    choice = input("Choisir une action: ")
    if choice == "1":
        ajouterClient()
        print(Client)
        print(ClientCompte)
        print(Compte)
        mainMenu()
    elif choice == "2":
        numC = int(input("Entrez le numéro du compte à supprimer: "))
        supprimerClient(numC)
        print("Le compte a été supprimé avec succès.")
        mainMenu()
    elif choice == "3":
        EcrireFichierCSV()
        print("les informations sont enregistree sur le fichier -clients.csv- avec succee.")
        agentMenu()
    elif choice == "9":
        mainMenu()
    else:
        print("Choix invalide.")


def clientMenu():
    numCl = int(input("Entrez votre numéro de client: "))
    MPC = input("Entrez votre code secret: ")

    while numCl not in Client or Client[numCl] != MPC:
        print("Numéro de compte ou code secret invalide!")
        numCl = int(input("Entrez votre numéro client : "))
        MPC = str(input("Entrez votre code secret: "))

    else:
        print(f"Bienvenue! Client {numCl} !!")

    while True:
        print("1) Déposer de l'argent")
        print("2) Retirer de l'argent")
        print("3) Afficher le solde")
        print("4) Modifier le mot de passe")
        print("5) Allez ou menu principal")
        print("9) Retourner")
        choix = input("Veuillez choisir une option: ")
        if choix == "1":
            balance = float(input("Entrez le montant à déposer: "))
            deposit(numCl, balance)
        elif choix == "2":
            montant = float(input("Entrez le montant à retirer: "))
            retirer(numCl, montant)
        elif choix == "3":
            afficher_solde(numCl)
        elif choix == '4':
            nouveauMP = input("Entrez votre nouveau mot de passe : ")
            modifierMPclient(numCl, Client[numCl], nouveauMP)
            print(Client)
        elif choix == '5':
            mainMenu()
        elif choix == '9':
            return
        else:
            print("Choix invalide...")



mainMenu()