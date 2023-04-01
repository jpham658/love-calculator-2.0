import random
from bs4 import BeautifulSoup

random_number = random.randint(0, 100)

with open('calculator-display.html', 'r') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

span = soup.find("span", id='love-score')
span.string = f"Your random number is: {random_number}"

# Print the contents of the span before and after the modification
print(f"Before modification: {span}")
print(f"After modification: {span}")

with open('calculator-display.html', 'w') as file:
    file.write(soup.prettify())
