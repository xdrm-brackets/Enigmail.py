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
		if( pList[i] != 'stop_value' ):          # si l'element n'est pas traite
			xReturn.append( pList[i] ); # on met le caractere dans xReturn
			pList[i] = 'stop_value';             # on met un caractere qui nous indique que l'on a deja traite
			n += 1;                     # on met a jour notre indicateur de caracteres traites
		else:                           # si l'element est deja traite
			i += 1
		i = (i+pKEY) % l
	return xReturn;


# fonction qui fait tourner les rotors (sens horaire) de pROTOR (indice 1 a len(pROTOR)) l'indice 0 etant la liste des premiers caracteres des rotors
def rotateRotorsClockwise(pROTOR):
	moveNext = True;
	for r in range(1, len(pROTOR)):                                         # parcourt les rotors
		if( moveNext ):                                                     # si on doit deplacer le rotor
			pROTOR[r] = [pROTOR[r][-1]] + pROTOR[r][:-1]                    # pivote le rotor de 1 caractere
			moveNext = ( pROTOR[r][0] == pROTOR[0][r-1] );                  # si le rotor vient de finir un tour, moveNext = True sinon moveNext = False


# fonction qui fait tourner les rotors (sens anti-horaire) de pROTOR (indice 1 a len(pROTOR)) l'indice 0 etant la liste des premiers caracteres des rotors
def rotateRotorsAnticlockwise(pROTOR):
	moveNext = True;
	for r in range(1, len(pROTOR)):                                         # parcourt les rotors
		if( moveNext ):                                                     # si on doit deplacer le rotor
			pROTOR[r] = pROTOR[r][1:] + [pROTOR[r][0]]                    # pivote le rotor de 1 caractere
			moveNext = ( pROTOR[r][-1] == pROTOR[0][r-1] );                  # si le rotor vient de finir un tour, moveNext = True sinon moveNext = False


# fonction qui affiche les rotors
def printRotors(pROTOR):
	for i in range(1, len(pROTOR)):
		print pROTOR[i];

# fonction qui code un caractere pChar via les rotors
def encodeChar(pChar, pSIGMA, pROTOR):
	for r in range(1, len(pROTOR)):              # parcourt les rotors
		pChar = SIGMA[ pROTOR[r].index(pChar) ]; # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
	return pChar;

# fonction qui decode un caractere pChar via les rotors
def decodeChar(pChar, pSIGMA, pROTOR):
	for r in reversed(range(1, len(pROTOR))):              # parcourt les rotors
		pChar = pROTOR[r][ pSIGMA.index(pChar) ];          # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
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

# DEFINITION DE L'ALPHABET
SIGMA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,.?!:[](){}-_0123456789#$*/ \\"\'';

# ALPHABET FORMATE EN LISTE
SIGMA = list(SIGMA);
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


# AFFICHAGE DES ROTORS
# printRotors(ROTOR);

# SAISIE DU MESSAGE
m = ( raw_input('Message: ') );

# CHOIX DU TYPE (ENCODE / DECODE)
type = 'X';
while( type != 'E' and type != 'D' ):
	type = ( raw_input('encoder ou decoder [E/D]: ') ).upper();
# VARIABLE DU HASH
M = '';



# ENCODAGE DU MESSAGE
if( type == 'E' ): 
	for c in range(0, len(m)):
			M += encodeChar(m[c], SIGMA, ROTOR);
			rotateRotorsClockwise(ROTOR);                  # on pivote les rotors dans le sens horaire
# DECODAGE DU MESSAGE
else:
	# decalage des rotor en position de fin d'encodage (taille du message -1)
	for r in range(1, len(m)):
		rotateRotorsClockwise(ROTOR);

	# pour chaque caractere en partant du dernier
	for c in reversed(range(0, len(m))):
		M += decodeChar(m[c], SIGMA, ROTOR); # on lit le caractere
		rotateRotorsAnticlockwise(ROTOR);    # on tourne les rotors dans le sens inverse
	
	# on retourne la chaine
	M = M[::-1];

print
print 'Enigma :', M