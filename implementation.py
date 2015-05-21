import random

def encode(al, key, msg):
	tmp = '';
	hash = '';
	for i in range(0, len(msg)): # parcourt chaque caractere du message
		tmp = msg[i]
		for j in range(1, len(al)): # parcourt les alphabets du premier au dernier
			tmp = al[j][ al[j-1].index(tmp) ];
		hash += tmp
	return hash;
	
alphabet = [];
alphabet.append( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] )
alphabet.append( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] )
alphabet.append( ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] )

for i in range(0, len(alphabet)):
	random.shuffle( alphabet[i] );
	print alphabet[i]
print 

code = raw_input("Votre message: ")
# demande la saisie des cles (positions initiales)
key = [0,0,0,0];
for i in range(0, len(key)):
	key[i] = raw_input('Cle n%d : ' % (i+1) )
	

print encode(alphabet, key, code);
