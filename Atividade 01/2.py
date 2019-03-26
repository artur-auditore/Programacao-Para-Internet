import requests

'''2. Crie um programa em que permita baixar, via
HTTP e usando o método GET, um arquivo de
imagem (escolha um tipo apenas - jpg ou gif...):
• Passe como parâmetro o "endereço WEB" completo
até o arquivo;
• Salve o corpo da resposta como um arquivo
atentando para o tipo.'''


def main():
    img = requests.get(
        'https://cdn-cf-1.xda-developers.com/devdb/deviceForum/screenshots/6203/20170226T024155.jpg').content
    open('img_teste', 'wb').write(img)


if __name__ == "__main__":
    main()
