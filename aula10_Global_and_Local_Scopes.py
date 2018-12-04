# Essa aula basicamente trata de variaveis locais e globais, e de que é possivel declarar uma variável como 
# global mesmo estando em uma função colocando global antes do nome ou se ela for usada numa função dentro da função

spam = 42 #global variable

def eggs():
	spam = 42 # local variable

print (spam)
print (eggs())
