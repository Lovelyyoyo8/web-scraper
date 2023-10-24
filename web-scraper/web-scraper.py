from bs4 import BeautifulSoup
import requests
import time

def find_jobs_no_js(unfamiliar_skill):
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
        '=javascript&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            with open(f'posts/js_{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'Required Skills: {skills.strip()} \n')
                f.write(f'More Info: {more_info} \n')
                f.write(' ')
            print(f'File saved: js_{index}')

def find_jobs_no_java(unfamiliar_skill):
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
        '=java&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            with open(f'posts/java_{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'Required Skills: {skills.strip()} \n')
                f.write(f'More Info: {more_info} \n')
                f.write(' ')
            print(f'File saved: java_{index}')

def find_jobs_no_c(unfamiliar_skill):
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
        '=c&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            with open(f'posts/c_{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'Required Skills: {skills.strip()} \n')
                f.write(f'More Info: {more_info} \n')
                f.write(' ')
            print(f'File saved: c_{index}')

def find_jobs_no_angular(unfamiliar_skill):
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
        '=angular&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.strip()
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            with open(f'posts/angular_{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name.strip()} \n')
                f.write(f'Required Skills: {skills.strip()} \n')
                f.write(f'More Info: {more_info} \n')
                f.write(' ')
            print(f'File saved: angular_{index}')


if __name__ == '__main__':
    print('Put some skill that you are not familiar with: ')
    unfamiliar_skill = input('> ')
    print(f'Filtering out {unfamiliar_skill}')

    while True:
        find_jobs_no_js(unfamiliar_skill)
        find_jobs_no_java(unfamiliar_skill)
        find_jobs_no_c(unfamiliar_skill)
        find_jobs_no_angular(unfamiliar_skill)
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
