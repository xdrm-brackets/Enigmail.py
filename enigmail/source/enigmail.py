# -*- coding: utf-8 -*-

import email
import imaplib
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
		try:
			confKey = i[:i.index('=')].replace(' ', '');
			confVal = i[i.index('=')+1:].replace(' ', '').replace('\n', '');
			conf[confKey] = confVal;
		except ValueError:
			pass;

	allPropertiesOk = False;
	try:
		conf['smtp_server']; 
		conf['smtp_port'];

		conf['imap_server']; 
		conf['imap_port'];

		conf['mail_address']; 
		conf['login']; 

		conf['algorithm_complexity']; 

		return conf;
	except (KeyError, ValueError):
		print "Erreur: fichier de configuration incomplet";
		raise SystemExit(0);



# cette fonction envoie un mail
def sendMail(pConf, pPass, pTo, pSubject, pMessage):
	srv = smtplib.SMTP(pConf['smtp_server'], int(pConf['smtp_port']) );
	try:
		pMsg = MIMEMultipart();
		pMsg['From'] = pConf['mail_address'];
		pMsg['To'] = pTo;
		pMsg['Subject'] = "[ENIGMAIL] "+pSubject;

		pMsg.attach( MIMEText(pMessage.encode('utf-8')) );

		srv.ehlo_or_helo_if_needed();

		if( srv.has_extn('STARTTLS') ):
			srv.starttls();
			srv.ehlo_or_helo_if_needed();

		srv.login(pConf['login'], pPass);
		srv.sendmail( pConf['mail_address'], pTo, pMsg.as_string() );
		
		print "> Mail envoye !";
	except smtplib.SMTPAuthenticationError:
		print "> Mauvais login ou mot de passe\n\(enigmail config) pour changer votre adresse";
	finally:
		srv.quit();

# cette fonction récupère les mails
def getMail(pConf, pPass):
	mail = imaplib.IMAP4_SSL(pConf['imap_server'], pConf['imap_port']);
	mail.login(pConf['login'], pPass); # identification

	mail.list();
	mail.select("inbox"); # On choisit le dossier INBOX.

	result, data = mail.uid('search', None, '(HEADER Subject "[ENIGMAIL]")'); # on cherche les mails contenant [ENIGMAIL] dans le sujet
	latest_email_uid = data[0].split()[-1];
	result, data = mail.uid('fetch', latest_email_uid, '(RFC822)');
	m = data[0][-1];

	# Pour le dernier mail contenant [ENIGMAIL] dans le sujet, on met le contenu dans bucket file
	body = '';
	b = email.message_from_string(m);
	if( b.is_multipart() ):
	    for p in b.get_payload():
			body += p.get_payload()
	return body;



# fonction qui renvoie l'alphabet 
def getSigma():
	SIGMA =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ';           # maj
	SIGMA += 'abcdefghijklmnopqrstuvwxyz';           # min
	SIGMA += '&=+^~@%,.?!:;[](){}-_#$*/ \t\\"«»\'\n';    # ponctuation + retour charriot
	SIGMA += '0123456789';                           # digit
	SIGMA += 'éèêàâùçîô';                               # accents
	SIGMA = SIGMA.decode('utf-8');

	# ALPHABET FORMATE EN LISTE
	return list(SIGMA);

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
		print "[ERREUR] Caractere %s non present dans l'alphabet" % pChar;
		raise SystemExit(0);

# fonction qui decode un caractere pChar via les rotors
def decodeChar(pChar, pSIGMA, pROTOR):
	try:
		for r in reversed(range(1, len(pROTOR))):              # parcourt les rotors
			pChar = pROTOR[r][ pSIGMA.index(pChar) ];          # le caractere devient celui au rang de l'alphabet correspondant au rang du caractere dans le rotor r
		return pChar;
	except ValueError:                                         # si un caractère n'est pas dans l'alphabet
		print "[ERREUR] Caractere %s non present dans l'alphabet" % pChar;
		raise SystemExit(0);




# fonction qui encode une chaine (pTimes fois)
def encodeStr(pM, pSIGMA, pROTOR, pTimes):
	tmp = pM;                                               # tmp contient le mot en cours [initial, initial codé 1 fois, ...]

	for t in range(0, pTimes):                              # pour chaque fois, on encode le message
		encodedStr = '';
		for c in tmp:                                       # pour chaque caractère de tmp
			encodedStr += encodeChar(c, pSIGMA, pROTOR);    # on encode le caractère courant
			rotateRotorsClockwise(pROTOR);                  # on pivote les rotors dans le sens horaire
		tmp = encodedStr;                                   # tmp vaut maintenant la valeur déjà codée

	return encodedStr;





# fonction qui decode une chaine (pTimes fois)
def decodeStr(pM, pSIGMA, pROTOR, pTimes):
	tmp = pM;

	# decalage des rotor en position de fin d'encodage (taille du message -1)
	for r in range(1, pTimes*len(pM)):
		rotateRotorsClockwise(pROTOR);

	for t in range(0,pTimes):
		decodedStr = '';
		for c in tmp[::-1]:                                        # pour chaque caractere en partant du dernier
			decodedStr += decodeChar(c, pSIGMA, pROTOR);           # on lit le caractere
			rotateRotorsAnticlockwise(pROTOR);                     # on tourne les rotors dans le sens inverse
		tmp = decodedStr[::-1];
	# on retourne la chaine
	return decodedStr[::-1];