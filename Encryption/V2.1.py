class Work:
    def __init__(self,key, mes, out,i):
        self.key = key
        self.mes = mes
        self.out = out
        self.i = i
    def length(self) :
        if bool(self.i==len(self.mes)):
            self.i=0
    def CODE(self):
        for x in self.mes:
            while self.i <= len(self.key): 
                num = ord(self.key[self.i])-32
                break
            letra = ord(x)-32 + num 
            if letra > 94:
                letra = letra%94 
            letra = letra + 32
            self.out = self.out + chr(letra)
            self.i += 1
            self.length()
    def DECODE(self) :
	
      for x in self.mes:

        while self.i <= len(self.key):
            num = ord(self.key[i]) -32
            break
        letra = ord(x)-32 - num 
        while(letra<0):
            letra = 94+(letra)
        letra = letra + 32
        self.out= self.out + chr(letra)
        self.i+= 1
        self.length()

print ("-----------------------------------ENCRYPTER (CAESAR STYLE)  V2.0----------------------------------------------")
print ("___________________________________ROCiO PERALES VALDES________________________________________________________")
print ("-FOR EXTRA SECURITY IT IS RECOMMENDED TO USE A KEYWORD AS LONG AS YOUR MESSAGE BUT THIS IS NOT AT ALL NECESSARY")
i=0
key = list(input("Set a keyword: "))
code=input ("Do you wish to encode or to decode, type 'e' to encode or 'd' o decode: ")

while (code != 'e' and code != 'd'):
	code=input ("Type 'e' to encode or 'd' o decode: ")
mes = input('Type in the message here: ')
out = ""
w = Work(key,mes,out, i)
if code == 'e':
	w.CODE()
elif code=='d':
	w.DECODE()
print(w.out)
