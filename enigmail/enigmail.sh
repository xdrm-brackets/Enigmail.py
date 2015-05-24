#!/bin/bash

path=$(readlink -f $(dirname $0));
config_file="$path/.config";

editor_line=`cat $config_file | grep -E '^text_editor +=' | cut -d= -f2 | tr -d "[[:space:]]" | tr -d "\n"`;
editor="nano";

# si l'editeur est specifie on l enregistre sinon par defaut on met nano
if [ -z $editor_line ] || [ $editor_line = "" ]
then
	echo "text_editor =  nano" >> $config_file;
else
	editor=$editor_line;
fi;


if [ $# -ge 1 ]
then # si 1 paramètre au moins

	if [ $# -ge 2 ]
	then # si au moins 2 parametres
		param=$2;
	else
		param="";
	fi;

	case $1 in
		'help') cat "$path/source/help"|less;;
		'init')                               # initialise le contenu du fichier de config
			echo "smtp_server  = smtp.gmail.com" > "$path/.config";
			echo "smtp_port    = 587" >> "$path/.config";
			echo "" >> "$path/.config";
			echo "imap_server  = imap.gmail.com" >> "$path/.config";
			echo "imap_port    = 993" >> "$path/.config";
			echo "" >> "$path/.config";
			echo "mail_address = test@mail.com" >> "$path/.config";
			echo "" >> "$path/.config";
			echo "login        = equal_mailadress_or_different_login" >> "$path/.config";
			echo "" >> "$path/.config";
			echo "text_editor  = nano" >> "$path/.config";
			;;
		'config')
			if [ -z $param ]
			then # si aucun parametre alors on lance l'editeur choisi
				$editor "$path/.config";      # ouvre en modification le fichier de config
			else
				$editor "$path/.config";
			fi;;
		'write')  $editor "$path/bucket-file";;  # ouvre en modification le bucket file
		'empty')  echo "">"$path/bucket-file";;  # vide le bucket file
			                                  # ouvre en lecture le bucket file
		'read')  echo "\n======================================="; cat "$path/bucket-file"; echo "\n=======================================";; 
		'encode') python "$path/source/encode.py" $param;;
		'decode') python "$path/source/decode.py" $param;;
		'receive') python "$path/source/receive.py" $param;;
		'send') python "$path/source/send.py" $param;;
		*) echo "Erreur";
	esac;
else
	echo "Parametre manquant: enigmail help";
fi;
