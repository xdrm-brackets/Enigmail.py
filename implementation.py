import random

def encode(al, key, msg):
	tmp = '';
	hash = '';
	for i in range(0, len(msg)): # parcourt chaque caractere du message
		tmp = al[1].index( msg[i] );
		hash += al[len(al)-1][tmp];
		
	# decale le premier alphabet d'un cran, le deuxieme si le premier depasse
	for i in range(1, len(al)):
		print i;
	return hash;
	
alphabet = [];
alphabet.append( [] )
alphabet.append( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] )
alphabet.append( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] )
alphabet.append( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] )

for i in range(1, len(alphabet)):
	random.shuffle( alphabet[i] );
	alphabet[0].append( alphabet[i][0] );
	print alphabet[i]
print 

code = raw_input("Votre message: ")
# demande la saisie des cles (positions initiales)
key = [];
for i in range(0, len(alphabet)):
	key.append( raw_input('Cle n%d : ' % (i+1) ) )
print

print encode(alphabet, key, code);
