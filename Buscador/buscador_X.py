from operator import itemgetter

import requests
import requests_cache
from bs4 import BeautifulSoup
import re


def main():
    requests_cache.install_cache("testes")
    lista = buscar("facebook", 'http://facebook.com', 2)
    exibe(lista)


def buscar(key, url, profundidade=0, lista=None):
    if lista is None:
        lista = []
    limitador = 5
    response = requests.get(url)
    texto = response.text
    copia_texto = texto
    cont = 0
    lista_de_palavras = []
    while True:
        palavra = ''
        encontou = copia_texto.find(key)
        for j in range(10, 0, -1):
            palavra += texto[encontou - j]
        for i in range(len(key)):
            palavra += texto[encontou + i]
        for k in range(0, 11):
            palavra += texto[encontou + (len(key)) + k]
        copia_texto = copia_texto.replace(key, "*" * len(key), 1)
        if encontou == -1:
            break
        lista_de_palavras.append(palavra)
        cont += 1
    lista.append({'site': url, 'resultados': lista_de_palavras, 'quantidade': cont, 'profundidade': profundidade})
    print(" \n", cont, "Ocorrencias", "no link", url)
    print()
    if profundidade > 0:
        links_validos = []
        html = BeautifulSoup(response.text, "html.parser")
        for link in html.findAll('a', {'href': re.compile("http")}):
            links_validos.append(link.get('href'))
        if len(links_validos) >= limitador:
            qtd_buscas = limitador + 1
        else:
            qtd_buscas = len(links_validos)
        for t in range(1, qtd_buscas):
            link_buscar = links_validos[t]
            print("Buscando no link> ", link_buscar)
            buscar(key, link_buscar, profundidade - 1, lista)
    return lista


def exibe(lista):
    resultado_ord = sorted(lista, key=itemgetter('quantidade'), reverse=True)
    for resultado in resultado_ord:
        print("link do site > ", resultado['site'])
        print("Quantidade de ocorrências da key na procura: ", resultado['quantidade'])
        print("---- Trechos encontrados no link: ----")
        for i in range(len(resultado['resultados'])):
            print(i, '-', resultado['resultados'][i])


    # for h in lista:
    #     print(h['site'])
    #     print(h['quantidade'])
    #     for o in range(len(h['resultados'])):
    #         print(h['resultados'][o].s)




if __name__ == '__main__':
    main()
