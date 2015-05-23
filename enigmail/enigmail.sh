#!/bin/bash

path=$(readlink -f $(dirname $0))

if [ $# -eq 1 ]
then # si 1 paramètre
	case $1 in
		'init')                               # initialise le contenu du fichier de config
			echo "smtp_server = smtp.gmail.com" > "$path/.config"
			echo "smtp_port = 587" >> "$path/.config"
			echo "mail_address = test@mail.com" >> "$path/.config"
			;;
		'config') nano "$path/.config";;      # ouvre en modification le fichier de config
		'write')  nano "$path/bucket-file";;  # ouvre en modification le bucket file
			                                  # ouvre en lecture le bucket file
		'read')  echo "\n======================================="; cat "$path/bucket-file"; echo "\n=======================================";; 
		*) echo "Erreur";
	esac;
else
	python "$path/source/interface.py";
fi;
