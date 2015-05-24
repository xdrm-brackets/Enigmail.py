# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText




# cette fonction récupère toutes les lignes du fichier enigmail.config et les stocke dans un dictionaire qui est retourné
def getConf(pPath):
	fConf = open(pPath+'/../.config', 'r');
	lines = fConf.readlines();
	fConf.close();

	conf = {};

	for i in lines:
		confKey = i[:i.index('=')].replace(' ', '');
		confVal = i[i.index('=')+1:].replace(' ', '').replace('\n', '');
		conf[confKey] = confVal;

	if( len(conf) == 4 ): # si le fichier de config est bien récupéré et qu'il est complet
		return conf;
	else:
		return False;



# cette fonction envoie un mail
def sendMail(pConf, pPass, pTo, pSubject, pMessage):
	srv = smtplib.SMTP(pConf['smtp_server'], int(pConf['smtp_port']) );
	try:
		pMsg = MIMEMultipart();
		pMsg['From'] = pConf['mail_address'];
		pMsg['To'] = pTo;
		pMsg['Subject'] = pSubject;

		pMsg.attach( MIMEText(pMessage.encode('utf-8')) );

		srv.ehlo();

		if( srv.has_extn('STARTTLS') ):
			srv.starttls();
			srv.ehlo();

		srv.login(pConf['smtp_login'], pPass);
		srv.sendmail( pConf['mail_address'], pTo, pMsg.as_string() );
		
		print "> Mail envoye !";
	except smtplib.SMTPAuthenticationError:
		print "> Mauvais login ou mot de passe\n\(enigmail config) pour changer votre adresse";
	finally:
		srv.quit();




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
	try:
		for r in range(1, len(pROTOR)):                        # parcourt les rotors
			pChar = pSIGMA[ pROTOR[r].index(pChar) ];          # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
		return pChar;
	except ValueError:                                         # si un caractère n'est pas dans l'alphabet
		print "[ERREUR] Caractere non present dans l'alphabet";
		raise SystemExit(0);

# fonction qui decode un caractere pChar via les rotors
def decodeChar(pChar, pSIGMA, pROTOR):
	try:
		for r in reversed(range(1, len(pROTOR))):              # parcourt les rotors
			pChar = pROTOR[r][ pSIGMA.index(pChar) ];          # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
		return pChar;
	except ValueError:                                         # si un caractère n'est pas dans l'alphabet
		print "[ERREUR] Caractere non present dans l'alphabet";
		raise SystemExit(0);




# fonction qui encode une chaine
def encodeStr(pM, pSIGMA, pROTOR):
	encodedStr = '';
	for c in pM:
		encodedStr += encodeChar(c, pSIGMA, pROTOR);
		rotateRotorsClockwise(pROTOR);                  # on pivote les rotors dans le sens horaire
	return encodedStr;





# fonction qui decode une chaine
def decodeStr(pM, pSIGMA, pROTOR):
	decodedStr = '';
	# decalage des rotor en position de fin d'encodage (taille du message -1)
	for r in pM[1:]:
		rotateRotorsClockwise(pROTOR);

	# pour chaque caractere en partant du dernier
	for c in pM[::-1]:
		decodedStr += decodeChar(c, pSIGMA, pROTOR);           # on lit le caractere
		rotateRotorsAnticlockwise(pROTOR);                     # on tourne les rotors dans le sens inverse
		
	# on retourne la chaine
	return decodedStr[::-1];