#!/bin/bash

if [ $# -eq 1 ]
then # si 1 paramètre
	case $1 in
		'init') echo """\nalias enigmail="sh $(pwd)/enigmail.sh"\n""";;
		'config') nano .config ;;
		'write')  nano bucket-file ;; 
		'read')  echo "\n======================================="; cat bucket-file; echo "\n=======================================";; 
		*) echo "Erreur";
	esac;
else
	python source/interface.py;
fi;
