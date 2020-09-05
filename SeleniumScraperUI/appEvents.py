class AppEvents():
    def __init__(self, MainWindow, TextService, ScrapeService):
        self.MainWindow = MainWindow
        self.textService = TextService
        self.scrapeService = ScrapeService

    def pullKeyWords(self):
        keywords = self.MainWindow.textEditKeyWords.toPlainText().upper()
        keyList = keywords.split(',')
        strippedList = []
        for key in keyList:
            key = key.strip()
            strippedList.append(key)
        #keywordsUpper = [x.upper() for x in keywords]
        print(strippedList)
        return strippedList

    def pullPhoneNumber(self):
        phonenumber = self.MainWindow.lineEditPhoneNumber.text()
        return phonenumber

    def scrapePage(self):
        jobs = self.scrapeService.FindJobs()
        return jobs

    def startButtonClick(self):
        print("the button has been clicked")
        keywords = self.pullKeyWords()
        phonenumber = self.pullPhoneNumber()
        jobs = self.scrapePage()
        matches = self.scrapeService.FindMatches(jobs, keywords)
        self.textService.sendSms(matches, phonenumber)
        print(matches)

    



