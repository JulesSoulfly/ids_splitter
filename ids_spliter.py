import os
from sys import argv

script_number = None
if len(argv) > 1:
	script_number = argv[1]

def concat_path(lst):
	return os.path.join(*lst)

my_folder = os.path.abspath(os.path.dirname(__file__))
temp = '_' + script_number + '_settings.txt' if script_number else '_settings.txt'
settings_file = concat_path([my_folder, temp])
temp = '_' + script_number + '_ids_pointer.txt' if script_number else '_ids_pointer.txt'
ids_pointer_file = concat_path([my_folder, temp])

settings = {'ids_file_name': 'ids.txt',
			'ids_file_name_for_save': 'ids.txt',
			'finish_file_name': 'start',
			'script_folder_name': 'autorus, emex, exist',
			'thread_count': 5,
			'ids_limit_per_thread': 10,
			'ids_limit': 0}

ids_pointer = 0

all_is_ok = False

def load_settings():
	if os.path.isfile(settings_file):
		with open(settings_file, 'r') as file:
			lines = [x.split(' = ') for x in file.read().split('\n')]
			st = {x[0]: x[1] for x in lines}
			for k, v in settings.items():
				temp = st.get(k, None)
				if temp:
					try: temp = int(temp)
					except: pass
					settings[k] = temp
	settings['ids_limit'] = settings['thread_count'] * settings['ids_limit_per_thread']
	settings['script_folder_name'] = list(settings['script_folder_name'].replace(' ', '').split(','))
	settings['finish_file_name'] = concat_path([my_folder, settings['finish_file_name']])
	global ids_pointer
	if os.path.isfile(ids_pointer_file):
		with open(ids_pointer_file, 'r') as file:
			ids_pointer = int(file.read().strip())


def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed.'''
    os.makedirs(os.path.dirname(path), exist_ok = True)
    return open(path, 'w')

if __name__ == '__main__':
	load_settings()
	print(settings)
	url_ids = []
	finish_line = ids_pointer
	fn = concat_path([my_folder, settings['ids_file_name']])
	if os.path.isfile(fn):
		num_lines = sum(1 for line in open(fn, 'r', encoding = 'utf-8'))
		if ids_pointer < num_lines:
			end_index = ids_pointer + settings['ids_limit']
			end_index = min(end_index, num_lines)
			with open(fn, 'r', encoding = 'utf-8') as file:
				for i in range(ids_pointer):
					next(file)
				for index, line in enumerate(file, start = ids_pointer):
					if end_index == index: break
					print(index, line.strip('\n'))
					url_id = line.strip('\n')
					url_ids.append(url_id)
					finish_line = index
			print('len(url_ids): ', len(url_ids))

			ids_limit_per_thread = settings['ids_limit_per_thread']

			for i, ids_chunk in enumerate([url_ids[i * ids_limit_per_thread: i * ids_limit_per_thread + ids_limit_per_thread] \
				   for i in range(settings['thread_count'])]):
				print(ids_chunk)
				for folder in settings['script_folder_name']:
					full_path = concat_path([my_folder, os.path.join(folder + str(i), settings['ids_file_name_for_save'])])
					with safe_open_w(full_path) as file:
						file.write('\n'.join(ids_chunk))

			if len(url_ids) > 0:
				all_is_ok = True

	if all_is_ok:
		with open(ids_pointer_file, 'w') as file:
			file.write(str(finish_line + 1))

		with open(settings['finish_file_name'], 'w') as file:
			file.write(':3')

	print('----------> FINISH')

