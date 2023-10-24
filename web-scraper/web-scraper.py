from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

class JobFinder:
    def __init__(self, skill):
        self.skill = skill

    def find_jobs(self, unfamiliar_skill):
        raise NotImplementedError

    def export_to_excel(self, job_list, file_name):
        df = pd.DataFrame(job_list)
        df.to_excel(file_name, index=False)


class NoJsJobFinder(JobFinder):
    def find_jobs(self, unfamiliar_skill):
        html_text = requests.get(
            f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
            '={self.skill}&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        job_list = []

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                job_info = {
                    'Company Name': company_name.strip(),
                    'Required Skills': skills.strip(),
                    'More Info': more_info
                }
                job_list.append(job_info)

        return job_list


class NoJavaJobFinder(JobFinder):
    def find_jobs(self, unfamiliar_skill):
        html_text = requests.get(
            f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
            '=java&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        job_list = []

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                job_info = {
                    'Company Name': company_name.strip(),
                    'Required Skills': skills.strip(),
                    'More Info': more_info
                }
                job_list.append(job_info)

        return job_list


class NoCJobFinder(JobFinder):
    def find_jobs(self, unfamiliar_skill):
        html_text = requests.get(
            f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
            '=c&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        job_list = []

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                job_info = {
                    'Company Name': company_name.strip(),
                    'Required Skills': skills.strip(),
                    'More Info': more_info
                }
                job_list.append(job_info)

        return job_list


class NoAngularJobFinder(JobFinder):
    def find_jobs(self, unfamiliar_skill):
        html_text = requests.get(
            f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords'
            '=angular&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        job_list = []

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                job_info = {
                    'Company Name': company_name.strip(),
                    'Required Skills': skills.strip(),
                    'More Info': more_info
                }
                job_list.append(job_info)

        return job_list


if __name__ == '__main__':
    unfamiliar_skill = 'js/java/c/angular'

    job_list = []

    no_js_finder = NoJsJobFinder('javascript')
    no_java_finder = NoJavaJobFinder('java')
    no_c_finder = NoCJobFinder('c')
    no_angular_finder = NoAngularJobFinder('angular')

    job_list.extend(no_js_finder.find_jobs(unfamiliar_skill))
    job_list.extend(no_java_finder.find_jobs(unfamiliar_skill))
    job_list.extend(no_c_finder.find_jobs(unfamiliar_skill))
    job_list.extend(no_angular_finder.find_jobs(unfamiliar_skill))

    time_wait = 10
    print(f'Searching for jobs...')
    time.sleep(time_wait * 60)

    no_js_finder.export_to_excel(job_list, 'jobs_list.xlsx')
    print('Jobs exported to jobs_list.xlsx')
