
# Python 2 y 3
# explorer.py
# LawlietJH
# v1.2.3

try:
	from Tkinter import Tk
	from Tkinter import filedialog
except:
	from tkinter import Tk
	from tkinter import filedialog

import os


root = Tk()
root.withdraw()


class Explorer():
	
	def use():
		print('''\n\n	Ejemplo de Uso:
		
		from explorer import Explorer as ex
		
		file_name = ex.getFileName()
		print(file_name)
		
		folder_path = ex.getFolderName()
		print(folder_path)
		
		file_name_save = ex.getFileNameSave()
		print(file_name_save)
		
		ex.use()''')
	
	def getFileName(title='Abrir', file_types=[ 
				['Archivos de Texto','.txt'], ['Todos los Archivos','.*']
			], init_dir=os.getcwd(), encima=True):
		
		if encima == True:
			root.wm_attributes('-topmost', True)
		else:
			root.wm_attributes('-topmost', False)
		
		f_name = filedialog.askopenfile(title = title,
										initialdir = init_dir,
										filetypes = file_types)
		if not f_name == None:
			return f_name.name
	
	
	def getFolderName(title='Abrir Carpeta', init_dir=os.getcwd(), encima=True):
		
		if encima == True:
			root.wm_attributes('-topmost', True)
		else:
			root.wm_attributes('-topmost', False)
		
		d_path = filedialog.askdirectory(title = title, initialdir = init_dir)
		
		if not d_path == '':
			return d_path
	
	
	def getFileNameSave(title='Guardar', file_types=[
					['Archivos de Texto','.txt'], ['Todos los Archivos','.*']
				], init_dir=os.getcwd(), encima=True):
		
		if encima == True:
			root.wm_attributes('-topmost', True)
		else:
			root.wm_attributes('-topmost', False)
		
		f_name = filedialog.asksaveasfilename(title = title,
											  initialdir = init_dir,
											  filetypes = file_types)
		if not f_name == '':
			return f_name


if __name__ == '__main__':
	
	Explorer.use()


