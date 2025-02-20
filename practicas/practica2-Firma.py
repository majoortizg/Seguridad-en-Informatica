# Firma Digital usando RSA

# Importamos las librerias
from Crypto.Util import number
from Crypto.Random import get_random_bytes
import hashlib

# Para "e" vamos a usar el Numero 4 de Fermat
e = 65537

# Calculamos las llave Publica de Alice
pA = number.getPrime(1024, randfunc=get_random_bytes)
qA = number.getPrime(1024, randfunc=get_random_bytes)

nA = pA * qA
print("/n RSA nAlice: ", nA)

# Calculamos las llave Publica de Bob
pB = number.getPrime(1024, randfunc=get_random_bytes)
qB = number.getPrime(1024, randfunc=get_random_bytes)

nB = pB * qB
print("\n RSA nBob: ", nB)

# Calculas la llave Privada de Alice
phiA = (pA - 1) * (qA - 1)
dA = number.inverse(e, phiA)

print('\n RSA Llave Privada Alice dA', dA)

# Calculas la llave Privada de Bob
phiB = (pB - 1) * (qB - 1)
dB = number.inverse(e, phiB)

print('\n RSA Llave Privada Bob dB', dB)

# Firmamos el Mensaje
mensaje = "Quiero ir de Shopping a Zara"
print('\n Mensaje: ', mensaje)

# Generamos el HASH del mensaje
hM = int.from_bytes(hashlib.sha256(mensaje.encode('utf-8')).digest(), byteorder='big')
print('\n HASH de hM: ', hex(hM))

# Firmamos el HASH usando la llave PRIVADA de Alice y se lo enviamos a Bob
sA = pow(hM, dA, nA)
print("\n Firma: ", sA)

# Bob verifica la firma de Alice usando la llave PUBLICA de Alice
hM1 = pow(sA, e, nA)
print('\n HASH de hM: ', hex(hM))

# Verificamos
print('\n Firma Valida: ', hM == hM1, '\n')
