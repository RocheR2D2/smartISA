from django.shortcuts import render
from django.http import JsonResponse
from .crawl import crawling_site

def crawling(request, research):
    crawling_result = crawling_site(research)
    return JsonResponse({"results":f"TODO {crawling_result}"})
