from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

def main():
    url_list = get_Url()
    driver = webdriver.Chrome('D:\Thesis\PatentSearch\chromedriver_win32\chromedriver.exe')
    get_Patents(driver,url_list)

    # with open('BlockChain.csv','w') as resultsFile:
    #     fieldnames = ['Year','BlockChainTransaction']
    #     writer = csv.DictWriter(resultsFile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for year,url in url_list.items():
    #         driver.get(url)
    #         time.sleep(10)
    #         scripts = driver.find_element_by_tag_name('search-app')
    #         x =scripts.text
    #         for _ in x.split('\n'):
    #             if 'About' in _ and 'Download (CSV)' in _:
    #                 results = _.strip('About')
    #                 results = results.strip('Download (CSV)')
    #                 writer.writerow({'Year': year, 'BlockChainTransaction': results.strip('results')})
    #                 print(results)
    #                 break
    driver.quit()

def get_Patents(driver,url_list):

    for year, url in url_list.items():
        driver.get(url)
        time.sleep(30)
        links = driver.find_elements_by_xpath("//a[@href]")
        patents_links = []
        download_folder = 'D:\\Thesis\\PatentSearch\\Patents_Files\\Bitcoin'
        for elem in links:
            print(elem.get_attribute("href"))
            if elem.get_attribute('href').__contains__("patentimages"):
                patents_links.append(elem.get_attribute('href'))
        options = webdriver.ChromeOptions()
        profile = {"plugins.plugins_list": [{"enabled": False,
                                             "name": "Chrome PDF Viewer"}],
                   "download.default_directory": download_folder,
                   "download.extensions_to_open": ""}
        options.add_experimental_option("prefs", profile)
        #Downloading the pdfs
        for patent in patents_links:
            driver1 = webdriver.Chrome(executable_path='D:\Thesis\PatentSearch\chromedriver_win32\chromedriver.exe',chrome_options=options)
            # Load a page
            driver1.get(patent)
            time.sleep(5)
            #patent_page = driver.find_element_by_id("plugin").click()
            print("Here")
            # close the tab
            driver1.close()

def get_Url():
    url_list = {}
    terms = ['smart card reader','authentication']
    terms = ['smart card reader']
    terms = ['LED Television']
    terms = ['LED','Display']
    terms = ['Deep Neural Networks','Backpropagation']
    terms = ['Backpropagation','Optimization']
    terms = ['Machine Learning','Deep Neural Networks']
    terms = ['RFID']
    terms = ['Farming','Computer','Map','Position']
    terms = ['Precision Farming','position data']
    terms = ['Position Data','Farming','Mapping']
    terms=['Lithium','Mobile phones']
    terms= ['Lithium Batteries','Mobile Phones']
    terms = ['Lithium Batteries','Non-Aqueous','Non-metallic','cobalt']
    # Three sets for bitcoin blockchain
    #terms = ['BlockChain','Transaction']
    #terms = ['BlockChain', 'Bitcoin']
    terms = ['Bitcoin']
    basicurl = 'https://patents.google.com/?'
    for i in terms:
        if basicurl.endswith('?'):
            basicurl = basicurl + 'q=' +i
        else:
            basicurl = basicurl + '&q=' + i
    prev = 0
    # Getting the patents
    for i in range(2010,2018,1):
        year = i
        if prev == 0:
            prev = year
            url = basicurl + '&before=priority:' + str(year)
        else:
            url = basicurl + '&before=priority:'+str(year)+'0101&after=priority:'+str(prev)+'0101'

            prev = i
        url_list[year]=url
    # Below loop is for getting the numbers of patents
    # for year in range(2010,2017,1):
    #     url = basicurl + '&before=priority:' + str(year)
    #     url_list[year] = url
    return url_list

def get_Technologies(fileName):
    pass



main()




# import selenium
# #from ghost import Ghost
# from ghost import Ghost
# import bs4 as bs
# from PyQt4.QtWebKit import QWebPage
# from PyQt4.QtGui import QApplication
# from PyQt4.QtCore import QUrl
# import sys
# import urllib3.request
#
# # g = Ghost()
# # with g.start() as session:
# #     page, resources = session.open('https://patents.google.com/?q=genomics')
# #     if(page.http_status == 200):
# #         print('True')
# #     try:
# #         result, resources = page.evaluate(
# #              "document.getElementById('resultsContainer').getAttribute('value');")
# #         print ('Here')
# #     except(BaseException):
# #         print(BaseException.message)
# #     # print (session.content)
# #     # page, extra_resources = session.open("http://jeanphi.fr")
# #     # assert page.http_status == 200 and 'jeanphix' in session.content
#
# class Client(QWebPage):
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebPage.__init__(self)
#         self.loadFinished.connect(self.on_page_load)
#         self.mainFrame().load(QUrl(url))
#         self.app.exec_()
#
#     def on_page_load(self):
#         self.app.quit()
#
# #url = 'https://pythonprogramming.net/parsememcparseface/'
# url = 'https://patents.google.com/?q=genomics'
# client_response = Client(url)
# source = client_response.mainFrame().toHtml()
# soup1 = bs.BeautifulSoup(str(source), "lxml")
# print(soup1.text)
# js_test = soup1.find('body')
# print("Shalaka")
# print(js_test.text)



# import urllib3
# from urllib3 import request as req
# from urllib3 import response as respos
# import simplejson
#
# http = urllib3.PoolManager()
# r = http.request(method='GET',url='https://ajax.googleapis.com/ajax/services/search/patent?v=1.0&q=thumb%20wrestling%20apparatus&callback=processResults')
# url = ('https://ajax.googleapis.com/ajax/services/search/patent?' +
#        'thumb%20wrestling%20apparatus')
# #r = req.RequestMethods.request(url=url)
# #response = urllib3.urlopen(request)
# #response = req(method='',url='https://ajax.googleapis.com/ajax/services/search/patent?v=1.0&q=thumb%20wrestling%20apparatus&callback=processResults')
# # Process the JSON string.
# results1 = http.urlopen(method='GET',url='https://patents.google.com/?q=genomics')
# print(results1.data)
# results = simplejson.load(results1)
# # now have some fun with the results...
# print(results)










