from django.shortcuts import render
from django.http import HttpResponse 
from .models import DocxFile
from docx import Document
import spacy
from spacy.tokens import Span
import json
from django.http import JsonResponse

nlp = spacy.load('en_core_web_sm')

# Create your views here.
def getText(request):
    

    doc = Document("static/Smart_ISA_01.docx")
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    doc = '\n'.join(fullText)
    #return HttpResponse(json.dump(text), content_type='application/json')
    #return JsonResponse({'text':doc})
    return doc

# Display basic entity info:
def show_ents(request):
    
    doc = nlp(getText(request))
    fullText = {}
    i=0
    if doc.ents:
        for ent in doc.ents:
            fullText[i] = ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_))
            i += 1
    return JsonResponse({'fulltext':fullText})

# Get a dictonary filled of org ents from the word doc without duplicate value
def get_org_ents(request):
    doc = nlp(getText(request))
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
    return JsonResponse({'org_ents':org_ents})

def addORGSpan(doc):
	ORG = doc.vocab.strings[u'ORG']  

	# Create a Span for the new entity
	new_ent = Span(doc, 0, 1, label=ORG)

	# Add the entity to the existing Doc object
	doc.ents = list(doc.ents) + [new_ent]