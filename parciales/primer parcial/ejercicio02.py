import os
import hashlib
from Crypto.Util import number
from Crypto.Random import get_random_bytes

e = 65537

# Generar claves de Alice
pA = number.getPrime(1024, randfunc=get_random_bytes)
qA = number.getPrime(1024, randfunc=get_random_bytes)
nA = pA * qA
phiA = (pA - 1) * (qA - 1)
dA = number.inverse(e, phiA)

# Generar claves de la AC
pAC = number.getPrime(1024, randfunc=get_random_bytes)
qAC = number.getPrime(1024, randfunc=get_random_bytes)
nAC = pAC * qAC
phiAC = (pAC - 1) * (qAC - 1)
dAC = number.inverse(e, phiAC)

# Ruta absoluta del archivo
filename = os.path.join(os.getcwd(), "parciales", "primer parcial", "NDA.pdf")

# Funcion para calcular el hash del archivo
def hF(filename):
    with open(filename, "rb") as file:
        data = file.read()
    return int.from_bytes(hashlib.sha256(data).digest(), byteorder='big')

# Funcion para firmar el documento
def docFirmado(filename, private_key, n):
    hM = hF(filename)
    return pow(hM, private_key, n)

# Funcion para verificar firma
def firmaReal(filename, signature, public_key, n):
    hM = hF(filename)
    hM1 = pow(signature, public_key, n)
    return hM == hM1

# Alice firma el documento
fAlice = docFirmado(filename, dA, nA)
print("\n Firma de Alice:", fAlice)

# Se verifica firma de Alice
vAlice = firmaReal(filename, fAlice, e, nA)
print("Firma de Alice valida:", vAlice, "\n\n")

# AC firma el documento
fAC = docFirmado(filename, dAC, nAC)
print("Firma de la AC:", fAC)

# Bob verifica la firma de la AC
vAC = firmaReal(filename, fAC, e, nAC)
print("Firma de la AC valica:", vAC, "\n")
