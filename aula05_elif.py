# Essa aula é interessante porque ele apresenta o else if, neste caso elif
# e tem uma questão interessante, mesmo sendo verdade a ultima linha não chega a ser executada
# porque o parâmetro anterior era maior

name = "bob"
idade = 5000
if name == "Alice":
	print("Olá Alice!")
elif idade <12:
	print("Você não é a Alice, criança!")
elif idade >200:
	print("...diferente de você a Alice não é um vampiro imortal!")
elif idade >100:
	print("Você não é a alice vovó!")

