import random
#from bs4 import BeautifulSoup

randomNumber = random.randint(0, 100)

with open('calculator-display.html', 'w') as file:

    # Write the HTML code to display the random number
    file.write(f"<html><body><h1>Your love score is: {randomNumber}</h1></body></html>")


#with open('calculator-display.html') as file:
   # html = file.read()

#soup = BeautifulSoup(html, 'lxml')

#span = soup.find('span', id = 'love-score')
#span.string = str(randomNumber)

#with open('calculator-display.html', 'w') as file:
   # file.write(str(soup))

