import requests
from bs4 import BeautifulSoup 

LIMIT =50
INDEED_URL ="https://www.indeed.com/jobs?q=python&l=plano&radius=15&limit={}".format(LIMIT)

def extract_indeed_pages():

    indeed_result = requests.get(INDEED_URL)
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
    
    return max_pages


def extract_job (html):

    title = html.find('div',{'class':'title'}).find('a')['title']
    company = html.find('span',{'class':'company'})
    company_anchor = company.find('a')
    if company:
        if company_anchor is not None:
            company = str(company_anchor.string.encode('ascii','ignore'))
        else:
            company = str(company.string.encode('ascii','ignore'))
        company = company.strip()
    else:
        company = None

    location = html.find('div',{'class':'recJobLoc'})['data-rc-loc']
    job_id = html['data-jk']
    return {
        'title':title,
        'company':company,
        'location':location,
        'link':'https://indeed.com/viewjob?jk={}'.format(job_id)
        }


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print ('Scrapping page {}'.format(page+1))
        result = requests.get('{}&start={}'.format(INDEED_URL,page*LIMIT))
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all('div',{'class':'jobsearch-SerpJobCard'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_indeed_pages = extract_indeed_pages()
    indeed_jobs = extract_indeed_jobs(last_indeed_pages)
    return indeed_jobs




