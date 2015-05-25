# Enigmail.py



_Note: Je ne suis pas expert en cryptographie, ceci n'est qu'une ébauche_



# Utilisation (terminal linux)
- [Configurer](#configurer)
- [Ecrire](#utilisation)
- [Lire](#utilisation)
- [Effacer le contenu](#utilisation)
- [Réinitialiser les paramètres](#utilisation)
- [Modifier les paramètres](#utilisation)
- [Crypter](#utilisation)
- [Décrypter](#utilisation)
- [Envoyer par mail](#utilisation)
- [Récupérer le dernier mail](#utilisation)
- [Obtenir de l'aide](#utilisation)

### Initialisation

```bash
# 1. Se positionner dans le dossier __enigmail/__.
cd chemin/enigmail/

# 2. Créer un __alias__ pour l'utilisation d'enigmail.
alias enigmail="sh $(pwd)/enigmail.sh"

# OU

# 2. Enregistrer comme commande intégrée (toujours dans le dossier d'enigmail)
sh install.sh
```
- la commande enigmail fonctionnera à la prochaine ouverture d'un terminal

_Note: Il faudra refaire cette manipulation si vous changez le répertoire de place._


#####Configurer
```bash
enigmail config
```

Entrer ses paramètres en remplaçant les valeurs déjà écrites et enregistrer le fichier.
Si vous obtenez une erreur, retournez à la première étape vous n'êtes pas dans le bon dossier.

__Paramètres__
- serveur smtp
- port smtp
- serveur imap
- port imap
- login smtp/imap
- adresse mail

_Note: le login smtp et imap est commun. Le protocole POP n'est pas pris en charge dans cette version. L'utilisation du service mail fonctionne pour gmail et n'est pas stable pour les autres clients mail._

###Utilisation

```bash
# Ecrire
enigmail write
enigmail w

# Modifier les paramètres
enigmail config
enigmail c

# Réinitialiser les paramètres
enigmail init
enigmail i

# Lire
enigmail read
enigmail r

# Effacer le contenu
enigmail empty
enigmail em

# Crypter
enigmail encode          # ouvre l'interface pour entrer la clé
enigmail encode 168      # cryptage avec clé numérique
enigmail encode 0x1f2e85 # cryptage avec clé hexadécimale

enigmail e
enigmail e 168
enigmail e 0x1f2e85

# Décrypter
enigmail decode          # ouvre l'interface pour entrer la clé
enigmail decode 168      # décryptage avec clé numérique
enigmail decode 0x1285   # décryptage avec clé hexadécimale

enigmail d
enigmail d 168
enigmail d 0x1285

# Envoyer par mail
enigmail send
enigmail ms  # MailSend

# Récupérer le contenu du dernier mail
enigmail receive
enigmail mr  # MailReceive

# Obtenir de l'aide
enigmail help
enigmail h
```



###A faire
1. Prise en compte: accents + utf-8 [FAIT]
2. Gestion: fichiers [FAIT]
3. Améliorer le cryptage car pour un même caractère n fois, on obtient un schéma répétitif [fait~50]
4. Gestion de serveur SMTP [FAIT~50]
5. Fichier de config [FAIT~80]
6. Appel en shell [FAIT]
