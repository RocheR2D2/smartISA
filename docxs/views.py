from django.shortcuts import render
from django.http import HttpResponse 
from .models import DocxFile
from docx import Document
import spacy
from spacy.tokens import Span
import json
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import logging

nlp = spacy.load('en_core_web_sm')

# Create your views here.
def _get_text(filepath):
    doc = Document(filepath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    doc = '\n'.join(fullText)
    doc= nlp(doc)
    return doc

# Display basic entity info:
def _show_ents(doc):
    fullText = {}
    i=0
    if doc.ents:
        for ent in doc.ents:
            fullText[i] = ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_))
            i += 1
    return fullText

# Get a dictonary filled of org ents from the word doc without duplicate value
def _get_org_ents(doc):
    org_ents = {}
    i=0
    if doc.ents:
        for ent in doc.ents:
            if ent.label_ == 'ORG' and ent.text.replace("\n", "") not in str(org_ents.values()).replace("\n",""):
            #if ent.label_ == 'ORG' and not ent.text.isspace():
                # org_ents[i] = ent !!!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  NON SÉRIALISABLE PAR JSONRESPONSE
                org_ents[i] = ent.text
                i += 1
            #[e for e in doc.ents if not e.text.isspace()]
            #print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    #return org_ents 
    return org_ents

def addORGSpan(doc):
	ORG = doc.vocab.strings[u'ORG']  

	# Create a Span for the new entity
	new_ent = Span(doc, 0, 1, label=ORG)

	# Add the entity to the existing Doc object
	doc.ents = list(doc.ents) + [new_ent]

@csrf_exempt
def upload(request):
    if request.method == 'POST' or request.method == 'OPTIONS':
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filepath= fs.path(filename)
        logging.info(f"Saved {filepath}")
    else:
        #default value for test
        filepath="static/Smart_ISA_01.docx"
        logging.info(f"Use default file {filepath}")
    nlp_text = _get_text(filepath)
    #ents = _show_ents(nlp_text)
    org_ents = _get_org_ents(nlp_text)
    return JsonResponse({'text': [token.text for token in  nlp_text], "org_ents": org_ents})
