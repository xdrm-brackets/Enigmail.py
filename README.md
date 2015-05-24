# Enigmail.py

Implémentation enigma alternative en python

##### Note: Je ne suis pas expert en cryptographie, ceci n'est qu'une ébauche



# Utilisation (terminal linux)

### Initialisation

######Se positionner dans le dossier __enigmail/__.
```bash
cd chemin/enigmail/
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
Si vous obtenez une erreur, retournez à la première étape vous n'êtes pas dans le bon dossier.


### Utilisation

######Ecrire
```bash
enigmail write
```
######Modifier les paramètres
```bash
enigmail config
```
######Réinitialiser les paramètres
```bash
enigmail init
```
######Lire
```bash
enigmail read
```
######Effacer
```bash
enigmail del
```
######Crypter
```bash
enigmail encode
```
######Décrypter
```bash
enigmail decode
```
######Envoyer par mail
```bash
enigmail send
```
######Obtenir de l'aide
```bash
enigmail help
```


### A faire
1. Prise en compte: accents + utf-8 [FAIT]
2. Gestion: fichiers [FAIT]
3. Améliorer le cryptage car pour un même caractère n fois, on obtient un schéma répétitif
4. Gestion de serveur SMTP [FAIT~50]
5. Fichier de config [FAIT~80]
6. Appel en shell [FAIT]
