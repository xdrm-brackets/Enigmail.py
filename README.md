# Enigmail.py

Implémentation enigma alternative en python

##### Note: Je ne suis pas expert en cryptographie, ceci n'est qu'une ébauche



# Utilisation (terminal linux)
- Ecrire
- Lire
- Modifier les paramètres
- dsf
-sdf

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
######Effacer le contenu
```bash
enigmail empty
```
######Crypter
```bash
enigmail encode
enigmail encode 168
enigmail encode 0x1f2e85
```
######Décrypter
```bash
enigmail decode
enigmail decode 168
enigmail decode 0x1285
```
######Envoyer par mail
```bash
enigmail send
```
######Récupérer le contenu du dernier mail
```bash
enigmail receive
```
######Obtenir de l'aide
```bash
enigmail help
```


### A faire
1. Prise en compte: accents + utf-8 [FAIT]
2. Gestion: fichiers [FAIT]
3. Améliorer le cryptage car pour un même caractère n fois, on obtient un schéma répétitif [fait~50]
4. Gestion de serveur SMTP [FAIT~50]
5. Fichier de config [FAIT~80]
6. Appel en shell [FAIT]
