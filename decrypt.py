import os 
import pyaes

##abrindo o arquivo 
file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia 

key = b'novomundoalo1234'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data= aes.decrypt(file_data)

##removendo o arquivo criptografado 
os.remove(file_name)

##criando um novo arquivo descriptografado 
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()