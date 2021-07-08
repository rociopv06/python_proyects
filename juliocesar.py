def CODE() :
	global cifrado
	global i
	global lista
	for x in texto:
		
		if(x==" "):
			cifrado = cifrado + " "
			continue
		else:
			while i <= len(lista):
				num = ord(lista[i])
				break
			cifrado = cifrado + chr(((ord(x)-97 + num-96)%26)+97)
		
		i += 1
		length()

	print(cifrado)
def DECODE() :
	global final
	global i
	global cifrado
	global lista
	for x in texto:
		
		if(x==" "):
			final = final + " "
			continue
		else:
			while i <= len(lista):
				num = ord(lista[i])
				break
			final= final + chr(((ord(x) - num-1)%26)+97)
		i+= 1
		length()

	print(final)
def length() :
	global lista
	global i
	if bool(i==len(lista)):
		i=0

print ("-----------------------------------ENCRYPTER (CAESAR STYLE)  V1.0----------------------------------------------")
print ("___________________________________ROCíO PERALES VALDES________________________________________________________")
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

