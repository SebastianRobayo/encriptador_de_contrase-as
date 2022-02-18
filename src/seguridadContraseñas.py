from cryptography.fernet import Fernet
import pymysql

global idUsuario
global contrasena

db = pymysql.connect(
    host="localhost",
    user="sebastian",
    passwd="sebas1033802619",
    database="encriptacioncontrasenas"
)

cursor = db.cursor()

cursor.execute("SELECT id, contrasena FROM `contrasenas`")
capturaDato = cursor.fetchall()
for row in capturaDato:
    idUsuario = row[0]
    contrasena = row[1]


for idUsuario != 1:



texto = "sebas1033802619"

# Genera una clave en formato de secuencia de bytes
key = Fernet.generate_key()
objetoCifrado = Fernet(key)
textoEncriptado = objetoCifrado.encrypt(str.encode(texto))
encriptado = textoEncriptado.decode()
print(encriptado)

textoDesencriptado = objetoCifrado.decrypt(textoEncriptado)
desencriptado = textoDesencriptado.decode()
print(desencriptado)