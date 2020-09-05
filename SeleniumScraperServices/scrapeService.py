from selenium import webdriver
import time
import smtplib
import sys
#define the path for the chrome webdriver

class ScrapeService:
    def __init__(self):
        #define the path for the chrome webdriver
        #self.chrome_path = "/Users/frankie/Desktop/SeleniumScraper/SeleniumScraperServices/mac/chromedriver"
        #create a instance of the webdriver
        #self.driver = webdriver.Chrome(self.chrome_path)
        pass

    def FindJobs(self):
        #define the path for the chrome webdriver
        self.chrome_path = "REMITTED FOR GITHUB"
        #create a instance of the webdriver
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.get("https://recruit.hirebridge.com/v3/CareerCenter/v2/?cid=7724")
        time.sleep(7)
        jobs = self.driver.find_elements_by_class_name("col-md-8.jobtitle")
        #.upper() job titles, since keywords are upper too
        jobs = [title.text.upper() for title in jobs]
        print(jobs)
        self.driver.quit()
        return jobs

    def FindMatches(self, jobs, keywords):
        #iterate through each list to find matches. 
        matches = []
        for keyword in keywords:
            for job in jobs:
                if job.find(keyword) != -1:
                    matches.append(job)
        print("----------------------")
        print("matches:")
        return matches



#comments about comments
