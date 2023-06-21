from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
def index(response):
    doc_externo = open("./templates/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    document = plt.render(ctx)
    return HttpResponse(document)