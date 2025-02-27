import Crypto.Random
import Crypto.Util.number
import hashlib

# Vamos a usar 2^16 + 1 = 65537, el numero 4 de Fermat por eficienia
e = 65537

# Calculamos las llaves publicas de Bob de 1024 bits
pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

# Calculamos nB = pB * qB
nB = pB * qB

# Calculamos phiB, que se usa para calcular la llave privada
phiB = (pB - 1) * (qB - 1)

# Calculamos la clave privada dB (de Bob)
dB = Crypto.Util.number.inverse(e, phiB)

# Mensaje a cifrar: Lyrics Island in the Sun (1050 caracteres)
m = "Hip-hip Hip-hip Hip-hip Hip-hip When you re on a holiday You can t find the words to say All the things that come to you And I wanna feel it too On an island in the sun We ll be playing and having fun And it makes me feel so fine I can t control my brain Hip-hip Hip-hip When you re on a golden sea You don t need no memory Just a place to call your own As we drift into the zone On an island in the sun We ll be playing and having fun And it makes me feel so fine I can t control my brain We ll run away together We ll spend some time forever We ll never feel bad anymore Hip-hip Hip-hip Hip-hip On an island in the sun We ll be playing and having fun And it makes me feel so fine I can t control my brain We ll run away together We ll spend some time forever We ll never feel bad anymore Hip-hip (Hip-hip) we ll never feel bad anymore Hip-hip No, no (hip-hip) (Hip-hip) we ll never feel bad anymore (Hip-hip) No, no (hip-hip) No, no (hip-hip) Hip-hip No, no (hip-hip) (Hip-hip) we ll never feel bad anymore (Hip-hip) No, no hip-hip No, no (hip-hip)"
print("\nMensaje original enviado:\n", m)

# Dividir el mensaje en bloques de 128 caracteres
block = [m[i:i+128] for i in range(0, len(m), 128)]

# Convertimos cada bloque a int
for i, piece in enumerate(block):
    block[i] = int.from_bytes(piece.encode(), byteorder='big')

# Alice Cifra el Mensaje con la llave publica de Bob segun RSA
messages = []
for piece in block:
    mC = pow(piece, e, nB)  # Cifrar con la clave pública (e, nB)
    messages.append(mC)

# Bob recibe los mensaje y los Descifra
messagesD = []
for piece in messages:
    mD = pow(piece, dB, nB)
    messagesUn = mD.to_bytes((mD.bit_length() + 7) // 8, byteorder='big').decode()
    messagesD.append(messagesUn)

# Reconstruir el mensaje completo
m1 = ''.join(messagesD)

# Generar hash del mensaje original (hM) y el recibido (hM1)
hM = hashlib.sha256(m.encode('utf-8')).hexdigest()
hM1 = hashlib.sha256(m1.encode('utf-8')).hexdigest()

print('\n hM: ', hM)
print('\n hM1: ', hM1)

print("\nMensaje recibido después de descifrar:\n", m1)

# Se verifica la seguridad
if hM == hM1:
    print("\n Se recibio el mensaje con exito sin ninguna alteracion :)")
else:
    print("\n NO se recibio el mismo mensaje :(")
