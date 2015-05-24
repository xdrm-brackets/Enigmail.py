# -*- coding: utf-8 -*-
from enigmail import *
import getpass, sys, os

# RECUPERATION DU CHEMIN ABSOLU
path = os.path.abspath( os.path.dirname(sys.argv[0]) );

# OUVERTURE ET LECTURE DU FICHIER
inFile = open(path + '/../bucket-file', 'r');
m = inFile.read().decode('utf-8');
inFile.close();

# paramètres utilisateurs
conf = getConf(path);

To   =       str( raw_input('Destinataire    : ') );
Subj =       str( raw_input('Objet           : ') );
Pass = str( getpass.getpass('Mot de passe    : ') );
print '...';

sendMail(conf, Pass, To, Subj, m);