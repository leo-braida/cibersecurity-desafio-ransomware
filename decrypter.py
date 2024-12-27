import os
import pyaes
import sys

if len(sys.argv)<= 2:
    print("Por favor, insira o nome do arquivo a ser descriptografado e sua chave. Exemplo: python3 encrypter.py nome-do-arquivo chave-de-16-24-ou-32-bytes")
    sys.exit()


file_name = sys.argv[1]
key = sys.argv[2].encode('utf-8')

file = open(file_name, "rb")
file_data = file.read()
file.close()


aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)


os.remove(file_name)

if file_name.endswith(".ransomware"):
    new_file = file_name[: -len(".ransomware")].rstrip()
else:
    new_file = file_name
    
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
