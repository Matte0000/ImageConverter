import sys
import os
from PIL import Image

old_folder = sys.argv[1]
new_folder = sys.argv[2]
new_format = sys.argv[3]

if not os.path.exists(old_folder):
	raise FileNotFoundError('old folder not found')

if not os.path.exists(new_folder):
	try:
   		os.mkdir(new_folder)
	except OSError:
	    print (f"Creation of the directory failed {new_folder}")
	else:
	    print (f"Successfully created the directory {new_folder}")

for old_img in [name for name in os.listdir(old_folder) if os.path.isfile(os.path.join(old_folder, name))]:
	if not os.path.exists(f'./{new_folder}/{old_img}'):
		try:
			img = Image.open(f'./{old_folder}/{old_img}')
			clear_name = os.path.splitext(old_img)[0]
			img.save(f"./{new_folder}/{clear_name}.{new_format}")
		except ValueError:
			os.rmdir(new_folder)
			print('Error to convert images')
		except KeyError:
			os.rmdir(new_folder)
			print('format error')


