from bs4 import BeautifulSoup
import requests #uso para enviar a requisição
import pandas



#1 - Coletando vagas em Python

response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=')
# print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
# print(jobs[:3]) #coletando as 3 primeiras vagas

#Criando listas para preenchimento com dados do site
companies = [] 
skills = []
published_date = []

#2 - Estruturando informações para coleta
for job in jobs:
    name_company = job.find('h3', class_='joblist-comp-name').text.strip().replace(' ',"")
    # print(name_company)
    skill = job.find('span', class_="srp-skills").text.strip().replace(' ',"")
    # print(skill)

    pub_date = job.find('span', class_ = 'sim-posted').span.text
    # print(pub_date[7:])

#3 - Exportando informações para CSV
    companies.append(name_company)
    skills.append(skill)
    published_date.append(pub_date[7:])

python_jobs = pandas.DataFrame()
python_jobs['Companies'] = companies
python_jobs[' Skills'] = skills
python_jobs['Published Date'] = published_date
print(python_jobs)
python_jobs.to_csv('python_jobs.csv')
