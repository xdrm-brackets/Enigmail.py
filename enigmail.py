# -*- coding: utf-8 -*-

# fonction qui calcule le nombre de rotors en fonction de la clé pKey et qui retourne un entier
def calcLevel(pKey, pSIGMA):
	xN = 1;
	for r in range(1,100):
		if( pKey >= len(pSIGMA)**r ):  # si la clé est inférieure à la valeur max pour r rotors
			xN = r;                    # on enregistre la valeur
		else:                          # sinon (c'est qu'on a dépassé)
			break;                     # on arrête la boucle et on renvoie la derniere valeur de r (xN)
	return xN;

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
		pChar = pSIGMA[ pROTOR[r].index(pChar) ]; # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
	return pChar;

# fonction qui decode un caractere pChar via les rotors
def decodeChar(pChar, pSIGMA, pROTOR):
	for r in reversed(range(1, len(pROTOR))):              # parcourt les rotors
		pChar = pROTOR[r][ pSIGMA.index(pChar) ];          # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
	return pChar;
