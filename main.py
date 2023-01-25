from tkinter import *
from tkinter import ttk

#----------------------------------------
#                Fenêtre
#----------------------------------------

fenetre = Tk()
fenetre.title("Convertisseur de monnaie")
fenetre.geometry("300x190+250+50")
titre_fenetre = Label(fenetre, text="Convertisseur de monnaie", bg="pink", fg="#FFFFFF")

#--------------------------------------------------------
# Monnaie de départ / Saisie du montant & Menu déroulant
#--------------------------------------------------------

monnaie_dep = Label(fenetre, text = "Monnaie de départ", bg = "#FE277E", fg = "#FFFFFF")
monnaie_dep.pack()
entree_monnaiedep = Entry(fenetre)
entree_monnaiedep.pack()
monnaie_from = ["Choix monnaie...", "euros", "dollar_americain", "livre_sterling", "couronne_danoise"]
m_from = ttk.Combobox(fenetre, values = monnaie_from)
m_from.current(0)
m_from.pack()

#----------------------------------------
#   Monnaie d'arrivée / Menu déroulant
#----------------------------------------

monnaie_to = ["Choix monnaie...", "euros", "dollar_americain", "livre_sterling", "couronne_danoise"]
m_to = ttk.Combobox(fenetre, values = monnaie_to)
m_to.current(0)
m_to.pack()

#----------------------------------------
#               Résultat
#----------------------------------------

resultat = Label(fenetre, text ="Résultat", bg = "#FE277E", fg = "#FFFFFF")
resultat.pack()
p_resultat = Listbox(fenetre, width=20, height=2)
p_resultat.pack()

#--------------------------------------------
#       Vérification de la conversion
#--------------------------------------------

def verification_conversion(monnaie_from,monnaie_to):
    if monnaie_from == monnaie_to:
        print("/!\ Conversion indisponible : la devise doit être différente de celle de départ /!\ ")
        return False
    return True

#--------------------------------------------
#               Taux de change
#--------------------------------------------

euros_vers_dollar = 1.09
euros_vers_livresterling = 0.88
euros_vers_couronnedanoise = 7.44
dollar_vers_euros = 0.92
dollar_vers_livresterling = 0.81
dollar_vers_couronnedanoise = 6.84
livresterling_vers_euros = 1.13
livresterling_vers_dollar = 1.23
livresterling_vers_couronnedanoise = 8.43
couronnedanoise_vers_euros = 0.13
couronnedanoise_vers_dollar = 0.15
couronnedanoise_vers_livresterling = 0.12

#---------------------------------------------
#                  Fonctions
#---------------------------------------------

def conversion(montant, monnaie_from, monnaie_to):
    if monnaie_from == 'euros' and monnaie_to == 'dollar_americain':
        return montant * euros_vers_dollar
    elif monnaie_from == 'euros' and monnaie_to == 'livre_sterling':
        return montant * euros_vers_livresterling
    elif monnaie_from == 'euros' and monnaie_to == 'couronne_danoise':
        return montant * euros_vers_couronnedanoise
    elif monnaie_from == 'dollar_americain' and monnaie_to == 'euros':
        return montant * dollar_vers_euros
    elif monnaie_from == 'dollar_americain' and monnaie_to == 'livre_sterling':
        return montant * dollar_vers_livresterling
    elif monnaie_from == 'dollar_americain' and monnaie_to == 'couronne_danoise':
        return montant * dollar_vers_couronnedanoise
    elif monnaie_from == 'livre_sterling' and monnaie_to == 'euros':
        return montant * livresterling_vers_euros
    elif monnaie_from == 'livre_sterling' and monnaie_to == 'dollar_americain':
        return montant * livresterling_vers_dollar
    elif monnaie_from == 'livre_sterling' and monnaie_to == 'couronne_danoise':
        return montant * livresterling_vers_couronnedanoise
    elif monnaie_from == 'couronne_danoise' and monnaie_to == 'euros':
        return montant * couronnedanoise_vers_euros
    elif monnaie_from == 'couronne_danoise' and monnaie_to == 'dollar_americain':
        return montant * couronnedanoise_vers_dollar
    elif monnaie_from == 'couronne_danoise' and monnaie_to == 'livre_sterling':
        return montant * couronnedanoise_vers_livresterling

def bouton_convertir():
    montant = float(entree_monnaiedep.get())
    monnaie_from = m_from.get()
    monnaie_to = m_to.get()
    if verification_conversion(monnaie_from, monnaie_to):
        res = str(conversion(montant, monnaie_from, monnaie_to))
        p_resultat.delete(0, END)
        p_resultat.insert(0, res)
    fichier =open("histo_conversion.txt", "a")
    fichier.writelines([str(montant), " ", monnaie_from, " ", '->', " ", res, " ", monnaie_to, '\n'])

#-----------------------------------------------
#                   Conversion
#-----------------------------------------------

button_conversion = Button(fenetre, text='Convertir', bg='#FFFFFF', command=bouton_convertir)
button_conversion.pack()
fenetre.mainloop()