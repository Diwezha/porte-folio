import random
# traiter cas joueur donne une réponce vide -> peut aussi être des espace
# /!\ au mot avec espace et tiret
# /!\ liste de mot déjà saisie affiche les lettre du mot

# création des variable
listeLettre = []
pendu2 = []
lettre = []
pendu = []
mot2 = []

def Mot (): #création de la fonction mot qui choisie au azard un mot
    # création des mots
    # pb out of range aléatoire
    hibou = ["h","i","b","o","u"]# création du mot hibou
    manger = ["m","a","n","g","e","r"]# création du mot manger
    bonbon = ["b","o","n","b","o","n"]# création du mot bonbon
    miel = ["m","i","e","l"]# création miel
    circle = ["c","i","r","c","l","e"]#création du mot circle
    clown = ["c","l","o","w","n"]#création du mot clown
    stylos = ["s","t","y","l","o","s"]#création du mot stylos
    motsliste = [hibou,manger,bonbon,miel,circle,clown,stylos] # récupère tous les mots définit dans une liste
    mots = motsliste[random.randint(0,len(motsliste)-1)] # choisi un mot au hazard dans le liste motsliste
    return mots # revoie un des mots définie plus haut

mot = Mot() # variable mot qui contient le mot a deviner
#print (mot) # teste

for i in range (len(mot)): # nouvelle liste de la même longeur que le mot a deviner pour afficher les lettre trouver par le joueur
    mot2 = mot2+["_"] # création de la liste

def Parti(mot,mot2,listeLettre,pendu2,lettre,pendu):# création de la fonction partie qui lance une partie de pendu
    print ()# aéré la console en séparent chaque affichage entre 2 lettre saisie
    print (mot2)# affichage des lettre trouver par le joueur
    print ("les lettres déjà saisie sont :",listeLettre) # affichage des lettres déjà saisie par le joueur
    lettrePasDansMot=True # variable pour définir si le lettre saisie par le joueur est dans le mot ou pas (définie sur le fait que la lettre n'ai pas dans le mot)
    lettre = input("saisisez une lettre : ") # demande d'une lettre au joueur
    pendu = ["platau","potoVertical","potoHorizontal","potoDiagonal","corde","tete","corps","jambeGauche","jambeDroite","brasGauche","brasDroit"] # création de la variable pendu pour vérifier quand le pendu est fini
#    print (lettre,listeLettre) # teste
    if len(lettre) == 0 :
        return Parti(mot,mot2,listeLettre,pendu2,lettre,pendu)
    if len(lettre) > 1 : # si le joueur a mis 2 lettre au lieu d'une seul
        print ("Il vaudrais mieux ne mettre qu'une lettre.") # informer le joueur qu'il ne faut mettre qu'une lettre a la fois
        return Parti(mot,mot2,listeLettre,pendu2,lettre,pendu) # demande une nouvelle lettre au joueur, retour au début
    print(listeLettre, len(listeLettre))
    for i in range (len(listeLettre)): # boucle pour vérifer si le joueur a déjà proposer une lettre
        #print(i)
        if lettre[0] == listeLettre[i]: # si la lettre proposer est = dans la liste de lettre déjà proposer
            print ("Vous avez déjà saisi cette lettre.") # informer le joueur qu'il a déjà saisie cette lettre
            return Parti(mot,mot2,listeLettre,pendu2,lettre,pendu) # demande une nouvelle lettre au joueur, retour au début
# faire en sorte que les lettres du mot n'y sois pas
    listeLettre = listeLettre+[lettre] # allongement de la liste listeLettre avec la nouvelle lettre
    # print ("une lettre de plus") # teste

    for i in range (len(mot)): # boucle pour vérifier si lettre proposer est dans le mot
        if lettre [0]== mot[i]: # si le mot contient la lettre proposer
            mot2[i] = lettre # affectation a mot2 avec la lettre
            lettrePasDansMot=False # pour empécher d'afficher perdu dans pendu2
    if lettrePasDansMot == False : # afficher que le joueur a trouver une lettre du mot
        print ("cette lettre est dans le mot, bravo.") # informer le joueur qui a trouver une lettre du mot

    if lettrePasDansMot==True :#si la lettre saisie n'ai pas dans le mot
        pendu2 = pendu2+["perdu"] # affecttion à pendu2, un nouvelle élément
        print ("Cette lettre n'ai pas dans le mot, domage.") # informer le joueur que la lettre saisie n'est pas dans le mot
        print (pendre_pendu(pendu2))# affiche le pendu

    if mot == mot2 : # déclenchement de la fin de la partie si le joueur gagne
        print ("fin parti, gagner") # informe le joueur que la pertie est fini et qu'il a gagner
        
    elif len(pendu) == len(pendu2) :  # déclenchement de la fin de la partie si le joueur perd
        print ("fin parti, perdu") # informe le joueur que le partie est fini et qu'il a perdu
        #print (listeLettre, pendu2) # teste  
    else : # si la parti n'ai pas fini
        return Parti(mot,mot2,listeLettre,pendu2,lettre,pendu) # reprend la fonction au début et redemande un nouveau mot

def pendre_pendu (pendu): # fonction qui fait l'affichage du pendu et qui prend pour argument pendu ( une liste qui contien le nombre de lettre qui ne sont pas dans le mot et que le joueur a saisi
    # ligne 1
    ligne = "" # création de la variable ligne qui contien une chaine de caractère pour le ligne 1 (la plus haute)
    if len(pendu) >= 3: # si le joueur a fait plus de 3 erreur
        ligne = "--------" # affiche la ligne du haut
    print (ligne)# affiche la ligne
    # ligne 2
    ligne = "" # affecte une nouvelle chaine de caractère vide pour pouvoir afficher la 2e ligne
    if len(pendu) >= 2 :# si le joueur a fait plus de 2 erreur
        ligne = "|" # réaffecte la variable ligne
    if len (pendu) >= 4 :# si le joueur a fait plus de 4 erreur
        ligne = "|/"
    if len(pendu) >= 5 : # si le joueur a fait plus de 5 erreur
        ligne = "|/   |"
    print (ligne) # affiche la ligne
    # ligne 3
    ligne = ""# affecte une nouvelle chaine de caractère vide pour la 3e ligne
    if len(pendu) >= 2 : # si le joueur a fait plus de 2 erreur
        ligne = "|"
    if len(pendu) >= 6 : # si le joueur a fait plus de 6 erreur
        ligne = "|    ☻"
    print (ligne) #affiche la ligne
    # ligne 4
    ligne = "" # affecte une nouvelle chaine de caractère vide pour la 4e ligne
    if len(pendu) >= 2 :#si le joueur a fait plus de 2
        ligne = "|"
    if len(pendu) >= 7 :#si le joueur a fait plus de 7 erreur
        ligne = "|    |"
    if len(pendu) >= 8:#si le joueur a fait plus de 8 erreur
        ligne = "|   /|"
    if len(pendu) >= 9 :#si le joueur a fait plus de 9 erreur
        ligne = "|   /|\\"
    print (ligne)# affiche la ligne
    # ligne 5
    ligne = ""# affecte une nouvelle chaine de caractère vide pour la 5e ligne
    if len(pendu) >= 2 :#si le joueur a fait plus de 2 erreur
        ligne = "|"
    if len(pendu) >= 10 :#si le joueur a fait plus de 10 erreur
        ligne = "|   /"
    if len(pendu) >= 11:#si le joueur a fait plus de 11 erreur
        ligne = "|   / \\"
    print (ligne)#affiche la ligne
    # ligne 6
    ligne = ""# affecte une nouvelle chaine de caractère vide pour la 6e ligne
    if len(pendu) >= 2 :#si le joueur a fait plus de 2 erreur
        ligne = "|"
    print (ligne)#affiche la ligne
    # ligne 7
    ligne = ""# affecte une nouvelle chaine de caractère vide pour la 7e ligne
    if len(pendu) >= 1:#si le joueur a fait plus de 1 erreur
        ligne = "--------"
    print (ligne)#affiche la ligne
    
print (Parti(mot,mot2,listeLettre,pendu2,lettre,pendu))# lance la partie de pendu


