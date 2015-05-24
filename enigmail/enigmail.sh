#!/bin/bash

path=$(readlink -f $(dirname $0))

if [ $# -eq 1 ]
then # si 1 paramètre
	case $1 in
		'help') cat "$path/source/help"|less;;
		'init')                               # initialise le contenu du fichier de config
			echo "smtp_server = smtp.gmail.com" > "$path/.config"
			echo "smtp_port = 587" >> "$path/.config"
			echo "smtp_login = equal_mailadress_or_different_login" >> "$path/.config"
			echo "mail_address = test@mail.com" >> "$path/.config"
			;;
		'config') nano "$path/.config";;      # ouvre en modification le fichier de config
		'write')  nano "$path/bucket-file";;  # ouvre en modification le bucket file
		'empty')  echo "">"$path/bucket-file";;  # vide le bucket file
			                                  # ouvre en lecture le bucket file
		'read')  echo "\n======================================="; cat "$path/bucket-file"; echo "\n=======================================";; 
		'encode') python "$path/source/encode.py";;
		'decode') python "$path/source/decode.py";;
		'send') python "$path/source/send.py";;
		*) echo "Erreur";
	esac;
else
	echo "Parametre manquant: enigmail help";
fi;
