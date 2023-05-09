dictionary = {'gato':'fettuchini','tortuga':'bummy','perro':'chirris','perro':'chacalito'} 
#error no puede haer clave duplicada
print(len(dictionary)) #salida 4
words = ['gato','perro','caballo']

for word in words:
    if word in dictionary:
        print(word,"->",dictionary[word])
    else:
        print(word,"no esta en el diccionario ")


for word in dictionary:
    print (word)
    if word == 'perro':
        print(word," ",dictionary[word])
