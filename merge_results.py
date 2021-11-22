import os
from sys import argv

script_number = None
settings_file = None
my_folder = os.path.abspath(os.path.dirname(__file__))

settings = {'script_folder_name': 'autorus, emex, exist'}

def concat_path(lst):
	return os.path.join(*lst)

def form_settings_path(fname):
	global settings_file
	temp = '_' + script_number + fname if script_number else fname
	settings_file = concat_path([my_folder, temp])

if len(argv) > 1:
	temp_argv = argv[1:]
	try:
		script_number = int(temp_argv[0])
		temp_argv.pop(0)
	except: pass
	if len(temp_argv) > 0:
		if '.' in temp_argv[0]:
			form_settings_path(temp_argv[0])
		else:
			settings['script_folder_name'] = temp_argv[0]
			temp_argv.pop(0)
		if len(temp_argv) > 0:
			if '.' in temp_argv[0]:
				form_settings_path(temp_argv[0])
			else:
				settings['script_folder_name'] = temp_argv[0]

def load_settings():
	if settings_file and os.path.isfile(settings_file):
		with open(settings_file, 'r') as file:
			lines = [x.split(' = ') for x in file.read().split('\n')]
			st = {x[0]: x[1] for x in lines}
			for k, v in settings.items():
				temp = st.get(k, None)
				if temp:
					try: temp = int(temp)
					except: pass
					settings[k] = temp
	settings['script_folder_name'] = list( settings['script_folder_name'].replace(' ', '').split(',') )

def safe_open_w(path):
	''' Open "path" for writing, creating any parent directories as needed.'''
	os.makedirs(os.path.dirname(path), exist_ok = True)
	return open(path, 'w')

if __name__ == '__main__':
	load_settings()
	print('__settings: ', settings)
	subfolders = [f.name for f in os.scandir(my_folder) if f.is_dir()]
	print('__all_subfolders: ', subfolders)
	for site in settings['script_folder_name']:
		folders = [x for x in subfolders if site in x]
		print('__site_folders: ', folders)
		with open(concat_path([my_folder, site + '.csv']), 'w') as result_file:
			pass
		with open(concat_path([my_folder, site + '.csv']), 'a', encoding = 'utf-16') as result_file:
			for folder in folders:
				with open(concat_path([my_folder, folder, site + '.csv']), 'r', encoding = 'utf-16') as read_file:
					for line in read_file:
						result_file.write(line)


	print('----------> FINISH')
