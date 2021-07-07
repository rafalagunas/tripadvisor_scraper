import sys
import csv
from selenium import webdriver
import time

# default path to file to store data
path_to_file = "reviews.csv"

# default number of scraped pages
num_page = 10

# default tripadvisor website of hotel or things to do (attraction/monument) 
url = "https://www.tripadvisor.com.mx/Hotel_Review-g616319-d1790979-Reviews-Las_Nubes_De_Holbox-Holbox_Island_Yucatan_Peninsula.html"
#url = "https://www.tripadvisor.com/Attraction_Review-g187791-d192285-Reviews-Colosseum-Rome_Lazio.html"

# if you pass the inputs in the command line
if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]

# import the webdriver
driver = webdriver.Safari()
driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

# change the value inside the range to save more or less reviews
for i in range(0, num_page):

    # expand the review 
    time.sleep(2)
    driver.find_element_by_xpath(".//div[contains(@data-test-target, 'expand-review')]").click()

    container = driver.find_elements_by_xpath("//div[@data-reviewid]")
    dates = driver.find_elements_by_xpath(".//div[@class='_2fxQ4TOx']")

    for j in range(len(container)):

        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        title = container[j].find_element_by_xpath(".//div[contains(@data-test-target, 'review-title')]").text
        review = container[j].find_element_by_xpath(".//q[@class='IRsGHoPm']").text.replace("\n", "  ")
        date = container[j].find_element_by_xpath(".//span[contains(@class,'_34Xs-BQm')]").text

    
        csvWriter.writerow([date, rating, title, review]) 
        
    # change the page            
    driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()

driver.quit()
