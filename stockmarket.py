import os

import requests
from bs4 import BeautifulSoup

# Function to add space around the text in certain tags
def add_space_around_tags(soup, tags):
    for tag in tags:
        for match in soup.find_all(tag):
            match.insert_before(" ")
            match.insert_after(" ")

# Web URL
url = "https://www.valueline.com/markets/stock-market-today/daily-update"

# Get URL Content
r = requests.get(url)

# Parse HTML Code
soup = BeautifulSoup(r.content, 'html.parser')

# Add spaces around the text in bold tags
add_space_around_tags(soup, ['b', 'strong'])

# Find the specific div
heading = soup.find('div', class_='col-md-8 article-overview-featured')

# Check if the heading exists
if heading:
    # Remove excess whitespace
    modified_text = ' '.join(heading.text.split())
else:
    modified_text = "Heading not found"

# Write to a text file
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(modified_text)

print("Output written to output.txt")
#os.system("lpr -P Brother_HL_L2350DW_series ./output.txt")

