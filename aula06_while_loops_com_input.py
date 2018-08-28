#While com input básico
name =''
while name != 'your name':
    print ('Please type your name')
    name = input()
print ("Thanks")

#Loop infinito com clausula if e break para parar
while True:
    print ('Falae seu nome agora')
    name = input()
    if name == "Vlad":
        break
    
print ("Obrigado Mermo!")

# Legal. mostrou como pular usando o continue
spam = 0
while spam <5:
    spam = spam +1
    if spam == 3:
        continue
    print ("o Spam já está no número " + str(spam))

#Ensinou a parar o loop infinito no shel com ctrl + C
