import requests
from bs4 import BeautifulSoup
# Send GET request to the URL
url = "https://www.example.com"
response = requests.get(url)
# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# Extract and print all the <h2> tags
h2_tags = soup.find_all('h2')
for h2 in h2_tags:
 print(h2.text)
# Find and print the href attributes of all the links
links = soup.find_all('a')
for link in links:
 print(link.get('href'))
# Extract and print the content of the first paragraph
first_paragraph = soup.find('p').text
print("First paragraph:", first_paragraph)
