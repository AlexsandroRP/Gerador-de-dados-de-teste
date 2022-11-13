import random
import os
# Criar uma lista com os dados
# Definir as opções de escolhas
# função para usuario escolher as opções e salvar em arquivo txt
# continuar o código até o usuário digitar 'parar'

# Listas para sorteio
nomes = ['Alex', 'Richard', 'Elisabeth']
emails = ['alex@gmail.com', 'richard@gmail.com', 'elisabeth@gmail.com']
numeros = ['21996547854', '51998745784', '11965547821']
cidades = ['Tokyo', 'New York', 'Dallas']
estados = ['Shinjuku', 'New York', 'Texas']

# Listas vazias para adicionar items iteráveis
decisao = []
resultado_final = []

# Definição das funções
def gerar_nome():
    nome = random.choice(nomes)
    resultado_final.append(nome)

def gerar_email():
    email = random.choice(emails)
    resultado_final.append(email)

def gerar_telefone():
    telefone = random.choice(numeros)
    resultado_final.append(telefone)

def gerar_cidade():
    cidade = random.choice(cidades)
    resultado_final.append(cidade)

def gerar_estado():
    estado = random.choice(estados)
    resultado_final.append(estado)

def gerar_arquivo():
    with open('dados.txt', 'a', newline='') as arquivo:
        for x in resultado_final:
            arquivo.write(x + os.linesep)
    print("Exportação concluída com sucesso")    

def exibir_dados():
    for dado in resultado_final:
        print(f'{dado}')    

# App Principal

while decisao != 'parar':
    print("-" * 60)
    print('Bem-vindo ao gerador de dados de Testes - Para finalizar o programa, digite "parar"')
    print('-'*60)
    print('Escolha uma ou mais opções abaixo a serem geradas aleatóriamente: ')
    print('[1] - Nome')
    print('[2] - E-mail')
    print('[3] - Tefone')
    print('[4] - Cidade')
    print('[5] - Estado')
    decisao = input("Digite uma(as) opções: ").lower()

    for item in decisao:
        if item == '1':
            gerar_nome()
            
        if item == '2':
            gerar_email()
            
        if item == '3':
            gerar_telefone()
        
        if item == '4':
            gerar_cidade()
            
        if item == '5':
            gerar_estado()
                        
    if decisao == 'parar':
        print("O sistema foi encerrado")
        break
        

    print("-" * 30)    
    exibir_dados()

# Salvar arquivos em txt e exportar
    print("-" * 30) 
    gerar = input("Deseja gerar um arquivo txt com os dados impressos? s/n ").lower()    
        
    if gerar == 's':
       gerar_arquivo()
    else:
        ("Resultados não foram exportados")    
    os.system('cls')  
    





