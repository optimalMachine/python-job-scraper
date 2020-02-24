import requests
from bs4 import BeautifulSoup 

indeed_url = 'https://www.indeed.com/jobs?q=python&l=plano&radius=15&limit=50'
indeed_result = requests.get(indeed_url)
print (indeed_result.text)

#beautifulsoup parses html data.
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

# extracting html code.
pargination = indeed_soup.find("div",{"class":"pagination"})
# extract more detail information (pages)
links = pargination.find_all('a')

#Ending pages number extration.
#Remove the last one, Next link from pages list.
pages = []
for element in links[:-1]:
  pages.append(int(element.string))

#Find the largest number in the pages list, and save it into 'max_pages'.
max_pages = max(pages)
print (max_pages)