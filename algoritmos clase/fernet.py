# Ejercicio de cifrado SIMETRICO AES usando Algortimo de Fernet

# Importamos la libreria
from cryptography.fernet import Fernet

# Generar la llave de cifrado
key = Fernet.generate_key()
print("Llave: ", key)

# Mensaje a cifrar
message = "Mensaje Secreto".encode("utf-8")
print("Mensaje Original: ", message)

# Cifrar el mensaje
f = Fernet(key)
mensaje_cifrado = f.encrypt(message)
print("Mensaje Cifrado: ", mensaje_cifrado)

# Descifrar el mensaje
mensaje_descifrado = f.decrypt(mensaje_cifrado)
print("Mensaje Descifrado: ", mensaje_descifrado)