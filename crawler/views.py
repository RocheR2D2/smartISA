from django.shortcuts import render
from django.http import JsonResponse
from crawler import crawl
import logging
from scrapyd_api import ScrapydAPI

logging.getLogger().setLevel(logging.INFO)
scrapyd = ScrapydAPI('http://scrapyd:6800')

def crawling(request, research):
    list_result = crawl.crawl_research(research)
    task_status = "Failed"
    if list_result:
        try:
            task = scrapyd.schedule('default', 'quotes', start_urls=list_result, domain="investmentpolicy.unctad.org")
            logging.info(task)
            task_status="started"
        except Exception as e:
            logging.exception(e)
    else:
        logging.debug(f"Nothing to crawl for {research}")
    return {"task_status": task_status, "status_code":200}
