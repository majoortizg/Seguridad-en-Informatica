# Ejemplo de cifrado usando RSA

import Crypto.Random
import Crypto.Util.number

# Vamos a usar 2^16 + 1 = 65537, el numero 4 de Fermat por eficienia
# Debemos tomar en cuenta que "e" sera parte de la llave publica por eso
# no hay problema de usar el numero de Fermat
e = 65537
print("\n", "Numero de Fermat 2^16+1 e: ",e)


# Calculamos las llaves publicas de Alice
pA = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print("\n", "RSA - Primo de Alice pA: ", pA)
qA = Crypto.Util.number.getPrime(1024, randfunc = Crypto.Random.get_random_bytes)
print("\n", "RSA - Primo de Alice qA: ", qA)

# Calculamos nA = pA * qA
nA = pA * qA
print("\n", "RSA - nA: ", nA)

# Calculamos phiA
phiA = (pA - 1) * (qA - 1)
print ("\n", "RSA - phiA: ", phiA)

# Calculamos la Llave Privada de Alice
dA = Crypto.Util.number.inverse(e,phiA)
print("\n", "RSA Llave Privada - dA: ", dA)

# El mensaje a cifrar sera un numero 450
m = 450
print("\n RSA - Mensaje - :", m)

# Bob cifra el mensaje con la clave publica de Alice
mc = pow(m, e, nA)
print("\n RSA Mensaje Cifrado - : ", mc)

#Alice descifra el mensaje con su llave privada
mA = pow(mc, dA, nA)
print("\n RSA Mensaje Descifrado - : ", mA)
