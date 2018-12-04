# Essa aula basicamente trata de variaveis locais e globais, e de que é possivel declarar uma variável como 
# global mesmo estando em uma função colocando global antes do nome ou se ela for usada numa função dentro da função
# ele usa bastante esse site para demonstrar o fluxo http://pythontutor.com/

spam = 420 #global variable

def egg():
	global eggs # aqui sobrescreve a global
	eggs = 'olha o ovo aqui'
	print (eggs)

eggs = 42
def ovoloco():
	print(eggs) # usou a global da primeira função?


print (spam)
print (eggs)
print (egg(), " What?")
print(ovoloco())


# Exemplo da página 101 melhor:

def spam():
	eggs = 'variavel local'
	print(eggs) # exibe variavel local

def bacon():
	eggs = 'bacon local'
	print (eggs) # exibe bacon local
	spam() # exibe variavel local
	print (eggs) # exibe bacon local

eggs = 'global'
bacon()
print (eggs) # exibe global