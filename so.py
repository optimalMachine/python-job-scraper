import requests
from bs4 import BeautifulSoup

URL = 'https://stackoverflow.com/jobs?q=python&sort=i'


def get_jobs():
    last_indeed_pages = extract_indeed_pages()
    indeed_jobs = extract_indeed_jobs(last_indeed_pages)
    return indeed_jobs