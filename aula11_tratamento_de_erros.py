# Problema de erro inicial
# Primeiro exemplo
def div42by(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print("vc tentou dividir por zero")

print(div42by(1))
print(div42by(2))
print(div42by(0)) # erro de divisão por zero
print(div42by(3))

# segundo exemplo

print ("quantos gatos vc tem?")
numCats = input()
try:
	if int(numCats) >=4:
		print ("Mestre dos gatos nivel hard, hein?")
	else:
		print ("ah tá")
except ValueError:
	print("entre com um numero, seu animal")
