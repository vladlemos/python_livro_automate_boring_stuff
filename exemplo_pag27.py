passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print("Entre com uma senha")
senhaDigitada = input()
if senhaDigitada == secretPassword:
    print("Acesso concedido")
    if senhaDigitada =='12345':
        print('Este tipo de senha é muito fraca meu amigo')
else:
    print("Acesso negado")