
# Windows
# steny.py
# LawlietJH
# v1.0.0

from explorer import Explorer as ex
import binascii
import base64
import bz2
import re

encode = lambda data: base64.urlsafe_b64encode(data.encode()).decode()
decode = lambda data: base64.urlsafe_b64decode(data.encode()).decode()

header_INIT = encode('ZióN')
# ~ header_EOF  = encode('ZioN')
# ~ print('Compressed ZióN:', len(header_INIT), '-', header_INIT)
# ~ print('Compressed ZioN:', len(header_EOF),  '-', header_EOF)

class Steny:
	
	#-----------------------------------------------------------------------
	
	def prueba():
		print('\n---------------------------------------------------------------')
		original_data = 'Texto de Prueba'
		compressed = bz2.compress(original_data)
		decompressed = bz2.decompress(compressed)
		fl1 = len(original_data)
		fl2 = len(compressed)
		fl3 = len(decompressed)
		print('Original     :', fl1, '-', original_data)
		print('Compressed   :', fl2, '-', binascii.hexlify(compressed))
		print('Decompressed :', fl3, '-', decompressed.decode())
		print('Porcent Compression:', str(100-(round(fl2/fl3, 4))*100)+'%')
		print('\n---------------------------------------------------------------')
	
	#-----------------------------------------------------------------------
	
	def isValidExtension(s):
		r = re.compile('.+\.[a-zA-Z0-9]{1,}$')
		m = r.match(s)
		if m: return True
		else: return False
	
	#-----------------------------------------------------------------------
	
	def insertData():
		
		finput  = ex.getFileName(title='Abrir Archivo Principal', file_types=[['Todos los Archivos','.*']])
		fadd    = ex.getFileName(title='Abrir Archivo a Ocultar', file_types=[['Todos los Archivos','.*']])
		foutput = ex.getFileNameSave(title='Archivo de Salida', file_types=[['Todos los Archivos','.*']])
		
		if not (finput and fadd and foutput):
			print('\n---------------------------------------------------------------')
			print('\n Debes Indicar todos los Archivo.')
			print('\n---------------------------------------------------------------')
			return
		
		print('\n---------------------------------------------------------------')
		print('\n Leyendo los Archivos:')
		print(' Entrada:', finput)
		print(' Por Añadir:', fadd)
		print(' Salida:', foutput)
		
		ext = '.'+finput.split('.')[-1]
		
		try: f1 = open(finput, 'rb')
		except:
			print('\n No Existe el Archivo de Entrada:', finput)
			print('\n---------------------------------------------------------------')
			return
		try: f2 = open(fadd, 'rb')
		except:
			print('\n No Existe el Archivo a Agregar:', fadd)
			print('\n---------------------------------------------------------------')
			return
		
		print('\n Extrayendo los Binarios.')
		orig = f1.read()
		add = f2.read()
		
		print(' Comprimiendo los Datos.')
		data = bz2.compress(add)
		
		print(' Creando Archivo de Salida.')
		
		if not Steny.isValidExtension(foutput): foutput += ext
		
		fo = open(foutput, 'wb')
		fo.write(orig)
		fo.write(header_INIT.encode())
		fo.write(data)
		# ~ fo.write(header_EOF.encode())
		f1.close()
		f2.close()
		fo.close()
		print('\n---------------------------------------------------------------')
	
	#-----------------------------------------------------------------------
	
	def extractData():
		
		finput = ex.getFileName(title='Abrir Archivo para Observar', file_types=[['Todos los Archivos','.*']])
		if not finput:
			print('\n---------------------------------------------------------------')
			print('\n Debes Abrir un Archivo.')
			print('\n---------------------------------------------------------------')
			return
		
		print('\n---------------------------------------------------------------')
		print('\n Leyendo el Archivo.')
		print(' Archivo:', finput)
		
		try: f = open(finput, 'rb')
		except:
			print('\n No Existe el Archivo:', finput)
			print('\n---------------------------------------------------------------')
			return
		
		datas = f.read()
		datas = datas.split(header_INIT.encode())
		datas.pop(0)
		ldata = len(datas)
		
		if ldata == 0: print('\n No hay Datos Almacenados.')
		else:
			print('\n '+str(ldata)+' Archivos Almacenados.')
			print('\n Descomprimiendo los Datos.')
			print('\n---------------------------------------------------------------')
			for i, data in enumerate(datas):
				data = bz2.decompress(data).decode()
				print('\n > Contenido #'+str(i+1).zfill(2))
				print('   ---- INI ----')
				print(data)
				print('   ---- EOF ----')
		f.close()
		print('\n---------------------------------------------------------------')
	
	#-----------------------------------------------------------------------
	
	def deleteData():
		
		finput = ex.getFileName(title='Abrir Archivo para Eliminar los Datos Guardados', file_types=[['Todos los Archivos','.*']])
		if not finput:
			print('\n---------------------------------------------------------------')
			print('\n Debes Abrir un Archivo.')
			print('\n---------------------------------------------------------------')
			return
		
		print('\n---------------------------------------------------------------')
		print('\n Leyendo el Archivo.')
		print(' Archivo:', finput)
		
		try: f = open(finput, 'rb')
		except:
			print('\n No Existe el Archivo:', finput)
			print('\n---------------------------------------------------------------')
			return
		
		datas = f.read()
		datas = datas.split(header_INIT.encode())
		ldata = len(datas)
		
		if ldata == 1:
			print('\n No hay Datos por Eliminar.')
			print('\n---------------------------------------------------------------')
			return
		
		print('\n '+str(ldata-1)+' Archivos A Eliminar.')
		print('\n Eliminando los Datos del Archivo.')
		
		data  = datas.pop(0)
		
		fo = open(finput, 'wb')
		fo.write(data)
		fo.close()
		print('\n---------------------------------------------------------------')



if __name__ == '__main__':
	
	Steny.insertData()
	Steny.extractData()
	Steny.deleteData()
	
