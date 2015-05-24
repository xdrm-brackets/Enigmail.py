# -*- coding: utf-8 -*-
from enigmail import *
import getpass, sys, os

# RECUPERATION DU CHEMIN ABSOLU
path = os.path.abspath( os.path.dirname(sys.argv[0]) );

# paramètres utilisateurs
conf = getConf(path);

Pass = str( getpass.getpass('Mot de passe    : ') );
print '...';

# si il existe bien un mail et qu'il n'y a pas d'erreurs
body = getMail(conf, Pass);
if( body != '' ):
	# ECRITURE FICHIER
	outFile = open(path + '/../bucket-file', 'w');
	outFile.write( body );
	outFile.close();
	print "Fini!";
else:
	print "Erreur";