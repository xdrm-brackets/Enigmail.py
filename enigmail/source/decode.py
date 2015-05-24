# -*- coding: utf-8 -*-
from enigmail import *
import getpass, sys, os


# RECUPERATION DU CHEMIN ABSOLU
path = os.path.abspath( os.path.dirname(sys.argv[0]) )





# OUVERTURE ET LECTURE DU FICHIER
inFile = open(path + '/../bucket-file', 'r');
m = inFile.read().decode('utf-8');
inFile.close();


# DEFINITION DE L'ALPHABET
SIGMA = getSigma();

if( len(sys.argv) >= 2 ): # si clé en argument
	userkey = int( sys.argv[1], 0 );
else:                     # sinon saisie
	userkey = int( raw_input('Cle (hex ou int): '), 0 );

# CALCUL de LEVEL en fonction de la clé (LEVEL = nombre de rotors)
LEVEL = calcLevel(userkey, SIGMA);

# DECOMPOSITION DE LA CLE PRIMAIRE EN CLES SECONDAIRES
KEY = decomposeKey(userkey, len(SIGMA), LEVEL);

# CREATION DES ROTORS EN FONCTION DES CLES SECONDAIRES 
ROTOR = [];
ROTOR.append( [] );

# on cree les rotors grace a SIGMA et aux cles recuperees
for i in range(0, LEVEL):
	ROTOR.append( shuffle( SIGMA, KEY[i]) );           # on creer le rotor et le melange suivant la cle
	ROTOR[0].append( ROTOR[i+1][0] );                  # on enregistre la l&ettre en premiere position dans la premiere entree du rotor
	
M = decodeStr(m, SIGMA, ROTOR); # DECODAGE DU MESSAGE

# ECRITURE FICHIER
outFile = open(path + '/../bucket-file', 'w');
outFile.write( M.encode('utf-8') );
outFile.close();