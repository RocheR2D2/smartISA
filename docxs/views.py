from django.shortcuts import render
from django.http import HttpResponse 
from .models import DocxFile
from docx import Document
from spacy.tokens import Span
import json
from django.http import JsonResponse



# Create your views here.
def getText(requst):
    

    doc = Document("static/Smart_ISA_01.docx")
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    text = '\n'.join(fullText)
    #return HttpResponse(json.dump(text), content_type='application/json')
    return JsonResponse({'text':text})

# Display basic entity info:
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')

# Get a dictonary filled of org ents from the word doc without duplicate value
def get_org_ents(doc):
    org_ents = {}
    i=0
    if doc.ents:
        for ent in doc.ents:
            if ent.label_ == 'ORG' and ent.text.replace("\n", "") not in str(org_ents.values()).replace("\n",""):
            #if ent.label_ == 'ORG' and not ent.text.isspace():
                org_ents[i] = ent
                i += 1
            #[e for e in doc.ents if not e.text.isspace()]
            #print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    return org_ents 

def addORGSpan(doc):
	ORG = doc.vocab.strings[u'ORG']  

	# Create a Span for the new entity
	new_ent = Span(doc, 0, 1, label=ORG)

	# Add the entity to the existing Doc object
	doc.ents = list(doc.ents) + [new_ent]