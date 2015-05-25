# Enigmail.py

Implémentation enigma alternative en python

##### Note: Je ne suis pas expert en cryptographie, ceci n'est qu'une ébauche



# Utilisation (terminal linux)
- [Ecrire](#ecrire)
- [Lire](#lire)
- [Effacer le contenu](#effacer-le-contenu)
- [Réinitialiser les paramètres](#r%C3%A9initialiser-les-param%C3%A8tres)
- [Modifier les paramètres](#modifier-les-param%C3%A8tres)
- [Crypter](#crypter)
- [Décrypter](#d%C3%A9crypter)
- [Envoyer par mail](#envoyer-par-mail)
- [Récupérer le dernier mail](#r%C3%A9cup%C3%A9rer-le-contenu-du-dernier-mail)
- [Obtenir de l'aide](#obtenir-de-laide)

### Initialisation

#####Se positionner dans le dossier __enigmail/__.
```bash
cd chemin/enigmail/
```
#####Créer un __alias__ pour l'utilisation d'enigmail.
```bash
alias enigmail="sh $(pwd)/enigmail.sh"
```
#####Enregistrer comme commande intégrée
- toujours dans le dossier d'enigmail
```bash
sh install.sh
```
- la commande enigmail fonctionnera à la prochaine ouverture d'un terminal

_Note: Il faudra refaire cette manipulation si vous changez le répertoire de place._
#####Entrez vos paramètres personnels
```bash
enigmail config
```
Il vous faudra ensuite entrer vos paramètres en remplaçant les valeurs déjà écrites puis enregistrer le fichier
Si vous obtenez une erreur, retournez à la première étape vous n'êtes pas dans le bon dossier.
(voir [config](#config))

### Utilisation

#####Ecrire
```bash
enigmail write
enigmail w
```
#####Modifier les paramètres
```bash
enigmail config
enigmail c
```
#####Réinitialiser les paramètres
```bash
enigmail init
enigmail i
```
#####Lire
```bash
enigmail read
enigmail r
```
#####Effacer le contenu
```bash
enigmail empty
enigmail em
```
#####Crypter
```bash
enigmail encode
enigmail encode 168
enigmail encode 0x1f2e85

enigmail e
enigmail e 168
enigmail e 0x1f2e85
```
#####Décrypter
```bash
enigmail decode
enigmail decode 168
enigmail decode 0x1285

enigmail d
enigmail d 168
enigmail d 0x1285
```
#####Envoyer par mail
```bash
enigmail send
enigmail ms  # MailSend
```
#####Récupérer le contenu du dernier mail
```bash
enigmail receive
enigmail mr  # MailReceive
```
#####Obtenir de l'aide
```bash
enigmail help
enigmail h
```

######Config
- serveur smtp
- port smtp
- serveur imap
- port imap
- login smtp/imap
- adresse mail

_Note: le login smtp et imap est commun. Le protocole POP n'est pas pris en charge dans cette version. L'utilisation du service mail fonctionne pour gmail et n'est pas stable pour les autres clients mail._


###A faire
1. Prise en compte: accents + utf-8 [FAIT]
2. Gestion: fichiers [FAIT]
3. Améliorer le cryptage car pour un même caractère n fois, on obtient un schéma répétitif [fait~50]
4. Gestion de serveur SMTP [FAIT~50]
5. Fichier de config [FAIT~80]
6. Appel en shell [FAIT]
