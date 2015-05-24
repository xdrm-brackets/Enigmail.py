# -*- coding: utf-8 -*-
from enigmail import *
import getpass, sys, os










# on teste l'existence du paramètre passé à l'appel (encode/decode/send)
if( len(sys.argv) == 2 ):
	if( sys.argv[1] == 'encode' or sys.argv[1] == 'decode' or sys.argv[1] == 'send' ):
		arg = sys.argv[1];
	else:
		print("Erreur: enigmail help");
		raise SystemExit(0);
else:
	print("Erreur: enigmail help");
	raise SystemExit(0);









path = os.path.abspath( os.path.dirname(sys.argv[0]) );
# OUVERTURE ET LECTURE DU FICHIER
inFile = open(path + '/../bucket-file', 'r');
m = inFile.read().decode('utf-8');
inFile.close();
# DEFINITION DE L'ALPHABET
SIGMA =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ';           # maj
SIGMA += 'abcdefghijklmnopqrstuvwxyz';           # min
SIGMA += '&=+^~@%,.?!:;[](){}-_#$*/ \\"\'\n';    # ponctuation + retour charriot
SIGMA += '0123456789';                           # digit
SIGMA += 'éèêàùç';                               # accents
SIGMA = SIGMA.decode('utf-8');
# ALPHABET FORMATE EN LISTE
SIGMA = list(SIGMA);













if( arg == 'encode'):
	# CHOIX DE LA CLE
	userkey = int( raw_input('Cle (hex ou int): '), 0);

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
	M = encodeStr(m, SIGMA, ROTOR); # ENCODAGE DU MESSAGE
	# ECRITURE FICHIER
	outFile = open(path + '/../bucket-file', 'w');
	outFile.write( M.encode('utf-8') );
	outFile.close();

elif( arg == 'decode' ):
	# CHOIX DE LA CLE
	userkey = int( raw_input('Cle (hex ou int): '), 0);

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

elif( arg == 'send' ):
	# paramètres utilisateurs
	conf = getConf(path);

	if( conf == False ): # si manque des paramètres
		print "parametres manquants";
		raise SystemExit(0);

	To   =       str( raw_input('Destinataire    : ') );
	Subj =       str( raw_input('Objet           : ') );
	Pass = str( getpass.getpass('Mot de passe    : ') );
	print '...';
	
	sendMail(conf, Pass, To, Subj, m);
