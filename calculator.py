import random
from bs4 import BeautifulSoup

randomNumber = random.randint(0, 100)

with open('calculator-display.html') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')

span = soup.find('span', id = 'love-score')
span.string = str(randomNumber)

with open('calculator-display.html', 'w') as file:
    file.write(str(soup))

