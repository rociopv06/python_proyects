def CODE() :
	global cifrado
	global i
	global lista
	for x in texto:
		
		while i <= len(lista):
			num = ord(lista[i])
			num = num -32
			break
		letra = ord(x)-32 + num 
		if letra > 94:
			letra = letra%94	
		letra = letra+32
		cifrado = cifrado + chr(letra)

		i += 1
		length()

	print(cifrado)
def DECODE() :
	global final
	global i
	global cifrado
	global lista
	for x in texto:
		
		while i <= len(lista):
			num = ord(lista[i])
			num = num -32
			break
		letra = ord(x)-32 - num 
		while(letra<0):
			letra = 94+(letra)
		letra = letra + 32
		final= final + chr(letra)
		
		i+= 1
		length()

	print(final)
def length() :
	global lista
	global i
	if bool(i==len(lista)):
		i=0

print ("-----------------------------------ENCRYPTER (CAESAR STYLE)  V2.0----------------------------------------------")
print ("___________________________________ROCiO PERALES VALDES________________________________________________________")
print ("-FOR EXTRA SECURITY IT IS RECOMMENDED TO USE A KEYWORD AS LONG AS YOUR MESSAGE BUT THIS IS NOT AT ALL NECESSARY")
i=0
lista = input("Set a keyword: ")
lista = list(lista)
cifrado= ""
final = ""
code=input ("Do you wish to encode or to decode, type 'e' to encode or 'd' o decode: ")
while (code != 'e' and code != 'd'):
	code=input ("Type 'e' to encode or 'd' o decode: ")
texto = input('Type in the message here: ')

if code == 'e':
	CODE()
elif code=='d':
	DECODE()
