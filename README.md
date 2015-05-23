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

######Se positionner dans le dossier __enigmail/__.
```bash
cd enigmail/
```
######Créer un __alias__ pour l'utilisation d'enigmail.
```bash
alias enigmail="sh $(pwd)/enigmail.sh"
```
######Entrez vos paramètres personnels
```bash
enigmail config
```
Il vous faudra ensuite entrer vos paramètres en remplaçant les valeurs déjà écrites puis enregistrer le fichier
Si vous obtenez une erreur, retournez à la première étape vous n'êtes pas dans bon dossier.
### Utiliser


### Enigmail.py est prêt à être utilisé:

######Ecrire
```bash
enigmail write
```
######Lire
```bash
enigmail read
```
######Crypter+Envoyer par mail/Crypter seulement/Décrypter seulement
```bash
enigmail
```


### A faire
1. Prise en compte: accents + utf-8 [FAIT]
2. Gestion: fichiers [FAIT]
3. Améliorer le cryptage car pour un même caractère n fois, on obtient un schéma répétitif
4. Gestion de serveur SMTP [FAIT~50]
5. Fichier de config [FAIT~80]
6. Appel en shell
