# metodos
def crear_archivo(path,archivo,texto):
	url = "%s/%s"%(path,archivo)
	f = open(url,'w')
	f.write(texto)
	f.close()

def add_texto_archivo(path,texto):
	f = open(path)
	contenido = ""
	try:
		for line in f:
			contenido += line.strip()+"\n"
		f.close()
	finally:
		f.close()
	contenido += texto
	f = open(path,"w")
	f.write(contenido)
	f.close()
