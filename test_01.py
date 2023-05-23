file = open("administradores.txt", "r+")
login_pass = ""
# tamanho = len(file.readlines())


dicionario = {
    # "gpg2@cesar.school": "123",
    # "avs@cesar.school": "321"
}
# print("qwe" in dicionario)

# print(dicionario.items())
# for email, senha in dicionario.items():
#     login_pass = f'{email} {senha}'
#     login_pass += "\n"
#     file.write(login_pass)

# for valor in range(len(file.readlines())):
#     # lista = file.readline()
#     print(file.readline())

# print(dicionario["gpg2@cesar.school"])

for x in file.readlines():
    lista = x.split(" ")
    print(lista)
    lista[1] = lista[1][:len(lista[1])-1]
    print(lista[1])
    print(lista)
    dicionario.update({lista[0]: lista[1]})


# print(str(dicionario))
# print(dicionario.keys())
# print(dicionario.values())
# print(len(file.readlines()))
# print(file.readline())
print(dicionario)
file.close()
