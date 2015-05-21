# fonction qui retourne une liste de nombres entre 0 pLength a partir d'un nombre
# compris entre 0 et pLength**pLevel
def decomposeKey(pNum, pLength, pLevel):
	xReturn = [];
	n = pNum
	for i in range(pLevel-1, -1, -1):
		xReturn.append( n // (pLength**i) );
		n -= xReturn[i-pLevel+1] * (pLength**i) 
	return xReturn;


# fonction qui melange une liste pSIGMA melangee par une cle pKEY
def shuffle(pSIGMA, pKEY):
	xReturn = []
	pList = pSIGMA[:]
	l = len(pList)
	i = pKEY % l;                       # rang actuel
	n = 0;                              # nombre d'elements traites
	while( n < len(pList) ):
		if( pList[i] != '_' ):          # si l'element n'est pas traite
			xReturn.append( pList[i] ); # on met le caractere dans xReturn
			pList[i] = '_';             # on met un caractere qui nous indique que l'on a deja traite
			n += 1;                     # on met a jour notre indicateur de caracteres traites
		else:                           # si l'element est deja traite
			i += 1
		i = (i+pKEY) % l
	return xReturn;


# fonction qui fait tourner les rotors de pROTOR (indice 1 a len(pROTOR)) l'indice 0 etant la liste des premiers caracteres des rotors
def rotateRotors(pROTOR):
	moveNext = True;
	for r in range(1, len(pROTOR)):                                        # parcourt les rotors
		if( moveNext ):                                                     # si on doit deplacer le rotor
			pROTOR[r] = [pROTOR[r][-1]] + pROTOR[r][:-1]                   # pivote le rotor de 1 caractere
			moveNext = ( pROTOR[r][0] == pROTOR[0][r-1] );                  # si le rotor vient de finir un tour, moveNext = True sinon moveNext = False


# fonction qui affiche les rotors
def printRotors(pROTOR):
	for i in range(1, len(pROTOR)):
		print pROTOR[i];

# fonction qui code un caractere pChar via les rotors
def codeChar(pChar, pSIGMA, pROTOR):
	for r in range(1, len(pROTOR)):              # parcourt les rotors
		pChar = SIGMA[ pROTOR[r].index(pChar) ]; # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
	return pChar;



#############################################################################################################################
#############################################################################################################################
#############################################################################################################################
#########################################  ##############  ############            ##########################################
#########################################  ##############  #################  ###############################################
#########################################  ##############  #################  ###############################################
#########################################  ##############  #################  ###############################################
#########################################  ##############  #################  ###############################################
#########################################  ##############  #################  ###############################################
#########################################  ##############  #################  ###############################################
#########################################  ##############  #################  ###############################################
#########################################  ##############  #################  ###############################################
#########################################                  ############             #########################################
#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

# ALPHABET 
SIGMA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '];
# NOMBRE DE ROTORS
LEVEL = 3; # valeur par defaut
LEVEL = int( raw_input('Level: ') );
# CHOIX DE LA CLE (entre 0 et len(SIGMA)**level-1 ) => simplification grace a keymax
keymax = len(SIGMA)**LEVEL
userkey = int( raw_input('Cle (0 - %d): '%keymax) );
# DECOMPOSITION DE LA CLE PRIMAIRE EN CLES SECONDAIRES
KEY = decomposeKey(userkey, len(SIGMA), LEVEL);
# CREATION DES ROTORS EN FONCTION DES CLES SECONDAIRES 
ROTOR = [];
ROTOR.append( [] );
# on cree les rotors grace a sigma et aux cles recuperees
for i in range(0, LEVEL):
	ROTOR.append( shuffle( SIGMA, KEY[i]) );           # on creer le rotor et le melange suivant la cle
	ROTOR[0].append( ROTOR[i+1][0] );                  # on enregistre la lettre en premiere position dans la premiere entree du rotor
	print ROTOR[i+1]                                   # on l'affiche

# SAISIE DU MESSAGE
m = raw_input('Message: ');

# CODAGE DU MESSAGE
M = '';
for c in range(0, len(m)):
	M += codeChar(m[c], SIGMA, ROTOR);
	rotateRotors(ROTOR);                               # on pivote les rotors

print
print 'Enigma :', M