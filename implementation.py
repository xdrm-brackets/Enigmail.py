# fonction qui retourne une liste de nombres entre 0 pLength a partir d'un nombre
# compris entre 0 et pLength**pLevel
def decomposeKey(pNum, pLength, pLevel):
	xReturn = [];
	n = pNum
	for i in range(pLevel-1, -1, -1):
		xReturn.append( n // (pLength**i) );
		n -= xReturn[i-pLevel+1] * (pLength**i) 
	return xReturn;


# fonction qui retourne le resultat d'une liste pList melangee par un nombre pNum
def shuffle(pList, pNum):
	xReturn = []
	l = len(pList)
	i = pNum % l;                       # rang actuel
	n = 0;                              # nombre d'elements traites
	while( n < len(pList) ):
		if( pList[i] != '_' ):          # si l'element n'est pas traite
			xReturn.append( pList[i] ); # on met le caractere dans xReturn
			pList[i] = '_';             # on met un caractere qui nous indique que l'on a deja traite
			n += 1;                     # on met a jour notre indicateur de caracteres traites
		else:                           # si l'element est deja traite
			i += 1
		i = (i+pNum) % l
	return xReturn

# fonction qui fait tourner les rotors







sigma = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
userkey = 3*(27**0) + 21*(27**1) + 25*(27**2);
level = 3;
keymax = len(sigma)**level

# decomposition de n compris entre 0 et len(sigma)**level
key = decomposeKey(userkey, len(sigma), level);

rotor = [];
# on cree les rotors grace a sigma et aux cles recuperees
for i in range(0, level):
	print key[i]
	rotor.append( shuffle(sigma, key[i]) );
	print rotor[i]
