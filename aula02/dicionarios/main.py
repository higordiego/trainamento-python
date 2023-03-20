# Motivação

telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788'] # lista de telefone

contato = ('Yan', '1234-5678') # contatos tuples

contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')] # lista com dicionarios dentro

print(contatos_lista[3][1]) # acessando o numero da marina

# dicionarios
contatos = {'Yan': '1234-5678'}
print(type(contatos))


# reformulando
contatos_lista = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'Marina': '8877-7788'}

print(contatos['Marina'])
