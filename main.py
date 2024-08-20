from bs4 import BeautifulSoup
import requests

def calcular_filtro_ano(ano):
    # Calcula o valor do filtro com base na diferença entre o ano atual e 1950
    return max(0, ano - 1950)

def links_olx(base_link):
    while True:
        numero_paginas = input('Informe o número de paginas a serem raspadas: ')
        if numero_paginas.isdigit():
            numero_paginas = int(numero_paginas)
            break
        else:
            input('Digite apenas números ')
    
    # Altera entre as páginas para exibir mais anuncios.
    links = []
    for pagina in range(numero_paginas):
        link = base_link + '&o=' + str(pagina + 1)
        links.append(link)
    return links
        
def scrap_olx(links:list):
    for link in links:
        r = requests.get(link)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            print(soup.text)
            break

# Marca
while True:
    marca = input('Informe a marca do veículo: ')
    if marca.isalpha():
        marca = marca + '/'
        break
    else:
        print(f'Digite o nome de uma marca de veículos válida. ')

# Modelo
while True:    
    modelo = input('Informe o modelo do veículo: ')
    modelo = modelo + '/estado-sp?'
    break

# Preço mínimo
while True:    
    preco_minimo = input('Informe o preço mínimo: R$ ')
    if preco_minimo.isdigit():
        preco_minimo = '&ps=' + str(preco_minimo) #+ '&rs=58&motp=1&o='
        break
    else:
        print(f'Digite apenas números. ')

# Preço máximo
while True:         
    preco_maximo = input('Informe o preço máximo: R$ ')
    if preco_maximo.isdigit():
        preco_maximo = 'pe=' + str(preco_maximo)
        break
    else:
        print(f'Digite apenas números. ')

# Ano mínimo        
while True: 
    ano_minimo = input('Informe o ano mínimo: (1950 ou superior) ')
    if ano_minimo.isdigit() and int(ano_minimo) >= 1950:
        ano_minimo = calcular_filtro_ano(int(ano_minimo))
        ano_minimo = '&rs=' + str(ano_minimo)
        break
    else:
        print('Digite um ano válido (1950 ou posterior).')
  
# Ano máximo        
while True:         
    ano_maximo = input('Informe o ano máximo: ')
    if ano_maximo.isdigit() and int(ano_maximo) >= 1950:
        ano_maximo = calcular_filtro_ano(int(ano_maximo))
        ano_maximo = '&re=' + str(ano_maximo)
        break
    else:
        print('Digite um ano válido (1950 ou posterior).')
        
base_link  = 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/'

link = base_link + marca + modelo + preco_maximo + preco_minimo + ano_maximo + ano_minimo
print(link)

links = links_olx(link) # lista de links a serem raspados
scrap_olx(links)

