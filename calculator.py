import random
from bs4 import BeautifulSoup

random_number = random.randint(0, 100)

soup = BeautifulSoup(open("calculator-display.html"), "html.parser")
div = soup.select_one("#love-score")
scoretags = div.find_all("p")
print(div)

for scoretag in scoretags:
    scoretag.extract()

score = "<p>Score: "+str(random_number)+"</p>"
div.append(BeautifulSoup(score, "html.parser"))

with open('calculator-display.html', 'w') as file:
    file.write(str(soup))
