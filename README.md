# Enigmail.py

Implémentation enigma alternative en python

##### Note: Je ne suis pas expert en cryptographie, ceci n'est qu'une ébauche

### Paramètres internes
1. Alphabet utilisé

### Paramètres externes
1. Clé (hex ou int)
2. Fichier d'entrée
3. Encodage+mail OU encodage OU décodage

### Sortie
1. Message encodé ou décodé dans le fichier de sortie OU mail

### Points forts
1. Rapide
2. Complexe
3. Modulable
4. Appel en shell




# Utilisation

### Initialiser

1. Se positionner dans le dossier _enigmail/_.
``bash
cd enigmail/
``








### A faire
1. Prise en compte: accents + utf-8 [FAIT]
2. Gestion: fichiers [FAIT]
3. Améliorer le cryptage car pour un même caractère n fois, on obtient un schéma répétitif
4. Gestion de serveur SMTP [FAIT~50]
5. Fichier de config [FAIT~80]
6. Appel en shell
