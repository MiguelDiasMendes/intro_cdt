print('\nmodulo04 - Estrutura de Dados - dicionarios\n')
print('-' *40)

cardapio_semana = { 
"segunda-feira": "Arroz com feijão",
"terça-feira": "Strogonoff",
"quarta-feira": "Feijoada",
"quinta-feira": "Sopa",
"sexta-feira": "Pizza",
"sabado": "Churrasco",
"domigo": "Macarrão"
}

nome_usuario = input('Digite seu nome para começar: \n')
print(cardapio_semana)

selecione_opcao = input('Selecione o dia da semana: \n')

if selecione_opcao in cardapio_semana: 
    comida = cardapio_semana [selecione_opcao]
    print(f"No {selecione_opcao}, o dia é de comer {comida}!")

else:
    print("Desculpe, não temos esse dia em nosso cardapio")