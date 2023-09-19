from bs4 import BeautifulSoup

with open('cart.html','r') as html_file:
    content=html_file.read()
    soup=BeautifulSoup(content,'lxml')
    heading=soup.find_all('h4')

    for i in heading:
        print(f'heading for the div is {i.text}')
