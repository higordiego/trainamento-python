import sys

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print("Digite seu sexo: ")

# dois modos de fazer stdin and stdout
sexo = sys.stdin.readline()
print("Nome:"+nome + "\n" + "Sexo: %s Idade: %s" %(sexo,idade))
