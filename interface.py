# -*- coding: utf-8 -*-
from enigmail import *




# DEFINITION DE L'ALPHABET
SIGMA =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ';           # maj
SIGMA += 'abcdefghijklmnopqrstuvwxyz';           # min
SIGMA += '&=+^~@%,.?!:;[](){}-_#$*/ \\"\'\n';    # ponctuation + retour charriot
SIGMA += '0123456789';                           # digit
SIGMA += 'éèêàùç';                               # accents
SIGMA = SIGMA.decode('utf-8');
# ALPHABET FORMATE EN LISTE
SIGMA = list(SIGMA);
# NOMBRE DE ROTORS
LEVEL = 3; # valeur par defaut
# CHOIX DE LA CLE
userkey = int( raw_input('Cle (hex ou int): '), 0);
# CALCUL de LEVEL en fonction de la clé
LEVEL = calcLevel(userkey, SIGMA);
# DECOMPOSITION DE LA CLE PRIMAIRE EN CLES SECONDAIRES
KEY = decomposeKey(userkey, len(SIGMA), LEVEL);
# CREATION DES ROTORS EN FONCTION DES CLES SECONDAIRES 
ROTOR = [];
ROTOR.append( [] );
# on cree les rotors grace a sigma et aux cles recuperees
for i in range(0, LEVEL):
	ROTOR.append( shuffle( SIGMA, KEY[i]) );           # on creer le rotor et le melange suivant la cle
	ROTOR[0].append( ROTOR[i+1][0] );                  # on enregistre la l&ettre en premiere position dans la premiere entree du rotor


# AFFICHAGE DES ROTORS
# printRotors(ROTOR);

# LIEN DU FICHIER A CRYPTER
f1 = raw_input('Fichier d\'entrée: ');
f2 = raw_input('Fichier de sortie: ');

# OUVERTURE ET LECTURE DU FICHIER
inFile = open(f1, 'r');
m = inFile.read().decode('utf-8');

# CHOIX DU TYPE (ENCODE / DECODE)
type = '';
while( type != 'E' and type != 'D' ):
	type = ( raw_input('encoder ou decoder [E/D]: ') ).upper();
# VARIABLE DU HASH
M = '';


# DEMARRE LE CHRONO
startTime = time.time();

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

# ON ECRIT LE RESULTAT DANS LE FICHIER DE SORTIE
outFile = open(f2, 'w');
outFile.write(M.encode('utf-8'));
outFile.close();

print
print 'Temps d\'exécution:',time.time() - startTime;