import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from scrapy import Spider 
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
import scrapy_crawler.settings as my_settings

logging.getLogger().setLevel(logging.INFO)

def crawl_research(research):
    """use Selenium to interact with autocomplete search of investmentpolicy.

    research:
        Name of affair to search can be partial due to autocomplete on website side

    Returns:
        List of url to crawl, empty list if nothing found
    """
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

    browser.get("https://investmentpolicy.unctad.org/investment-dispute-settlement/")
    search_bar = browser.find_element_by_id("searchByCaseName")
    search_bar.click() 
    search_bar.send_keys(research)
    # need some time for autocomplete to finish
    time.sleep(2)
    autocomplete_list = browser.find_element_by_id("ui-id-1")
    items = autocomplete_list.find_elements_by_tag_name("li")
    logging.info(f"Found {len(items)} matching proprositions for {research}")
    list_url_to_crawl = []
    for item in items:
        logging.info(f"loading info for {item.text} case")
        # Got exception "Element is not currently visible and may not be manipulated" using item.click so we need to bypas and send javascript request directly
        browser.execute_script("arguments[0].click();", item);
        # need some time to load result
        time.sleep(3)
        correct_link = browser.find_element(By.XPATH,"/html/body/main/section[1]/div/div/div[2]/div/div/div[2]/div[3]/div[1]/div/table/tbody/tr/td[2]/a")
        logging.info(correct_link.text)
        list_url_to_crawl.append(str(correct_link.get_attribute('href')))
    browser.quit()
    display.stop()
    logging.info(list_url_to_crawl)
    return list_url_to_crawl

def crawling_site(research):
    list_result = crawl_research(research)
    task_status = "Failed"
    if list_result:
        try:
            crawler_settings = Settings()
            crawler_settings.setmodule(my_settings)
            process = CrawlerProcess(settings=crawler_settings)
            #process = CrawlerProcess(get_project_settings())
            process.crawl('quotes', domain="investmentpolicy.unctad.org", start_urls=list_result)
            process.start()
            task_status="Done"
        except Exception as e:
            logging.exception(e)
    else:
        logging.debug(f"Nothing to crawl for {research}")
    return task_status

if __name__ == '__main__':
    crawling_site("bulgaria")
