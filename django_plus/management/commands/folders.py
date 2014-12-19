from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand
import os
from django.conf import settings


vars_settings = \
"""
STATICFILES_DIR = 
(
	'static/',
)


TEMPLATE_DIRS =
(
	'plantillas/',
)

MEDIA_URL = '/media/'
MEDIR_ROOT = 
(
	'media/',
)
"""

BASE_DIR = settings.BASE_DIR
PROJECT_NAME = os.path.basename(BASE_DIR)

def crear_archivo(path,archivo,text):
	url = "%s/%s"%(path,archivo)
	f = open(url,'w')
	f.write(text)
	f.close()

def add_var_settings(path):
	url = "%s/%s/settings.py"%(path,PROJECT_NAME)
	f = open(url)
	contenido = ""
	try:
	for line in f:
		contenido += line.strip()+"\n"
		f.close()
	finally:
		f.close()
	contenido += vars_settings
	print contenido
	f = open(url,"w")
	f.write(contenido)
	f.close()



def plantilla_base():
	plantilla_django = """{% block title%}
{% endblock %}
{% block content%}
{% endblock %}
					"""
	return plantilla_django
	


class Command(TemplateCommand):
    help = ("Crea las carpetas para plantillas,aplicaciones,archivos estaticos y la carpeta de media ")

    def handle(self, msg=None, **options):
		print "este es el nombre del proyecto %s" % PROJECT_NAME
		carpetas = ["plantillas","apps","static","media"]
		#add_var_settings(BASE_DIR)
		for car in carpetas:
			os.mkdir(car)
			print "se ha creado la carpeta %s"% car
			if car == "plantillas":
				ruta_completa = "%s/%s"%(BASE_DIR,car)
				crear_archivo(ruta_completa,"base.html",plantilla_base())
			if car == "apps":
				ruta_completa = "%s/%s"%(BASE_DIR,car)
				crear_archivo(ruta_completa,"__init__.py","")
			if car == "static":
				lista = ["img","css","js"]
				for c in lista:
					ruta_completa = "%s/%s/%s/"%(BASE_DIR,car,c)
					os.mkdir(ruta_completa)



