a=$(cat ~/.bashrc|grep -E '^alias enigmail="sh (.+)$')


if [ -z $a ] # si l'alias n existe pas on le cree
then
	echo "alias enigmail=\"sh $(pwd)/enigmail.sh\"" >> ~/.bashrc
	echo "Configuration terminee. Les changements prendront effet au prochain terminal ouvert."
else
	x=""
	echo "Voulez vous ecraser la configuration précédente [o,n]";
	read x
	case $x in
		'o')  cp ~/.bashrc ~/.bashrc_cpy; # effectue une copie de .bashrc [prevention]
		      sed -E '/^alias enigmail="sh (.+)"$/d' ~/.bashrc > tmp_bashrc # supprime l'ancien alias de bashrc et stocke dans tmp_bashrc
		      echo "alias enigmail=\"sh $(pwd)/enigmail.sh\"" >> tmp_bashrc #ajoute le nouvel alias dans le fichier temporaire
		      cat tmp_bashrc > ~/.bashrc; # stocke le bashrc modifie dans l'original
		      rm tmp_bashrc; # supprime le fichier temporaire
        	      echo "\nConfiguration terminee. Les changements prendront effet au prochain terminal ouvert\n"
		      echo "Si il y a une erreur ou que le fichier .bashrc est endommage, une copie a été faite"
		      echo "Pour la récupérer: cat ~/.bashrc_cpy > ~/.bashrc";;
		*) echo  "Aucun changement effectue";;
	esac;
fi
