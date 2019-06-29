import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://www.example.com/'


def chrome_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })
    logging.info('Prepared chrome options..')

    browser = webdriver.Chrome(chrome_options=chrome_options)
    logging.info('Initialized chrome browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


def firefox_example(url, research):
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir', os.getcwd())
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

    logging.info('Prepared firefox profile..')

    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    logging.info('Initialized firefox browser..')

    browser.get(url)
    search_bar = browser.find_element_by_id("searchByCaseName")
    search_bar.click() 
    search_bar.send_keys(research)
    time.sleep(5)
    autocomplete_list = browser.find_element_by_id("ui-id-1")
    logging.info(autocomplete_list)
    items = autocomplete_list.find_elements_by_tag_name("li")
    for item in items:
        text = item.text
        logging.info(text)
        item.click
        logging.info(text)
        time.sleep(5)
        correct_link = browser.find_element(By.XPATH,"/html/body/main/section[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]/div/table/tbody/tr/td[2]/a")
        logging.info(correct_link.get_attribute('href'))

    browser.quit()
    display.stop()

if __name__ == '__main__':
    #chrome_example()
    firefox_example("https://investmentpolicy.unctad.org/investment-dispute-settlement/","bulgaria")
