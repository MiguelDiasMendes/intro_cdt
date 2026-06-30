'''
Módulo 04 - Estruturas de dados - Listas

Módulo 04 - Estruturas de dados - Tuplas

'''

dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta","sabado", "domingo")
print(dias_da_semana[1])#segunda, terça, quarta, quinta, sexta, sabado ou domigo
print('-' *40)

dia_favorito = input('Qual o seu dia favorio da semana?')
print(f'\n O dia escolhido foi!!: {dia_favorito}')

if dia_favorito == "domingo" :
    print ('Opa, Domingão é dia de macarronada')