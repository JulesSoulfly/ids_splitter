import os

def concat_path(lst):
	return os.path.join(*lst)

my_folder = os.path.abspath(os.path.dirname(__file__))
settings_file = concat_path([my_folder, '_settings.txt'])

settings = {'result_file_name': '_result.csv',
			'script_folder_name': 'autorus, emex, exist',
			'thread_count': 5}

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
	settings['script_folder_name'] = list(settings['script_folder_name'].replace(' ', '').split(','))
#	settings['result_file_name'] = concat_path([my_folder, settings['result_file_name']])


if __name__ == '__main__':
	load_settings()
	print(settings)

	for folder in settings['script_folder_name']:
		full_result_path = concat_path([my_folder, folder + ])
		with open('')
		with open(full_path)
		with safe_open_w(full_path) as file:
			file.write('\n'.join(ids_chunk))


	fn = concat_path([my_folder, settings['ids_file_name']])
	if os.path.isfile(fn):
		num_lines = sum(1 for line in open(fn, 'r'))
		if ids_pointer < num_lines:
			end_index = ids_pointer + settings['ids_limit']
			end_index = min(end_index, num_lines)
			with open(fn, 'r') as file:
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
					full_path = concat_path([my_folder, os.path.join(folder + str(i), settings['ids_file_name'])])
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

