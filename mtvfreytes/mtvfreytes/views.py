from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context, loader

def familiares(self):

    miHtml = open("C:/Users/Casita/entregable/mtvfreytes/plantilla/template.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    plantilla = loader.get_template('template.html')
    return HttpResponse(documento)