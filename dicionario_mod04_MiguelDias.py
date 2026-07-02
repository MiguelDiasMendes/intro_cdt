print('\nmodulo04 - Estrutura de Dados - dicionarios\n')
print('-' *40)

cardapio_semana = { 
"segunda-feira": "Arroz com feijão",

"terça-feira": "Strogonoff",

"quarta-feira": "Feijoada",

"quinta-feira": "Sopa",

"sexta-feira": "Pizza",

"sabado": "Churrasco",

"domingo": "Macarrão"

}

nome_usuario = input('Digite seu nome para começar: \n')
print(f'\nOlá, {nome_usuario}! Seja bem-vindo ao nosso cardápio da semana!\n')
print('-' *40)
print("Aqui você pode consultar o prato do dia de acordo com o dia da semana que você escolher.\n")   
print(f'\n{cardapio_semana}\n')

selecione_opcao = input('Selecione o dia da semana: \n').lower().strip()

if selecione_opcao in cardapio_semana: 
    comida = cardapio_semana [selecione_opcao]
    print(f'\n{selecione_opcao}, o dia é de comer {comida}!\n')

else:
    print("Desculpe, não temos esse dia em nosso cardapio, tente colocar o hífen (ex: segunda-feira).")

deseja_prosseguir = input("Deseja prosseguir com seu pedido?:  ")
print('\nVá para a aba de pagamentos\n')
