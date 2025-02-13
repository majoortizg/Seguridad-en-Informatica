# Practica de Algoritmo de intercambio de Claves
# Diffie - Helman

import hashlib
import random

# Numero primo de RFC3526 de 1536 bits - MODP Group
p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)
g = 2

# Inicio
print("**********")
print("\n", "Variables Publicas Compartidas")
print("\n", "Numero primo compartido publicamente RFC3625")
print("\n", "Numero Base Comaprtido Publicamente")

sAlice = random.getrandbits(256)
sBob = random.getrandbits(256)
sEve = random.getrandbits(256)

print("\n", "Numero Alice", sAlice)
print("\n", "Numero Bob", sBob)
print("\n", "Numero Eve", sEve)

#Alice manda mensaje a Bob
# A = g^a mod p
A = pow(g, sAlice, p)
print("\n", "Mensaje Alice", A)

#Bob manda mensaje a Alice
# B = g^b mod p
B= pow(g, sBob, p)
print("\n", "Mensaje Bob", B)

#Ataque de Eve "Man In The Middle"
AEve= pow(g, sEve, p) # Genera A de Eve
BEve= pow(g, sEve, p) # B de Eve

print("\n", "-----------------------------", "\n")

# Alice calcula la llave secreta interceptada por Eve - > s = BEve^a mod p
s1 = pow(BEve,sAlice,p)
print("\n", "Llave Secreta compartida (interceptada por BEve)", s1)

# Bob calcula la llave secreta compartida interceptada por Eve - > s = AEve^b mod p
s2 = pow(AEve,sBob,p)
print("\n", "Llave Secreta compartida (interceptada por AEve)", s2)

# Eve calcula las llaves secretas compartidas entre Alica y Bob
s1Eve = pow(B,sAlice,p)
s2Eve = pow(A,sBob,p)

# Comparamos las llaves secretas
h1 = hashlib.sha512(int.to_bytes(s1, length=1024, byteorder='big')).hexdigest()
h2 = hashlib.sha512(int.to_bytes(s2, length=1024, byteorder='big')).hexdigest()

h1Eve = hashlib.sha512(int.to_bytes(s1Eve, length=1024, byteorder='big')).hexdigest()
h2Eve = hashlib.sha512(int.to_bytes(s2Eve, length=1024, byteorder='big')).hexdigest()

if (h1==h2):
    print("¡Completado! El mensaje se ha enviado con exito, sin riesgo de inflitracion.")
else:
    print("¡Cuidado! El mensaje ha sido un hackeado.")

if (h1Eve==h2Eve):
    print("¡HACKEADO!")
else:
    print("¡BOOOO!")


print("\n", "h1:", h1)







