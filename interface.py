# -*- coding: utf-8 -*-
from enigmail import *
from mail import *
import getpass




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

# OUVERTURE ET LECTURE DU FICHIER
inFile = open('bucket-file', 'r');
m = inFile.read().decode('utf-8');
inFile.close();

# CHOIX DU TYPE (ENCODE+MAIL / ENCODE / DECODE)
type = '';
while( type != 'M' and type != 'C' and type != 'D' ):
	type = ( raw_input('[M] Crypter et envoyer par mail\n[C] Crypter\n[D] Décrypter\n > ') ).upper();
# VARIABLE DU HASH
M = '';

# ENCODAGE DU MESSAGE
if( type == 'M' or type == 'C' ): 
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


# [TYPE = M] ENVOI DU MAIL 
if( type == 'M' ):
	From =       str( raw_input('Votre adr. gmail: ') );
	Pass = str( getpass.getpass('Mot de passe    : ') );
	print
	To   =       str( raw_input('Destinataire    : ') );
	Subj =       str( raw_input('Objet           : ') );
	print
	print 'Envoi en cours';
	sendMail(From, Pass, To, Subj, M);
# ECRITURE FICHIER
else:
	outFile = open('bucket-file', 'w');
	outFile.write( M.encode('utf-8') );
	outFile.close();
