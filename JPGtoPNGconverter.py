import sys
import os
from PIL import Image

old_folder = sys.argv[1]
new_folder = sys.argv[2]

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
			img.save(f"./{new_folder}/{old_img.replace('.jpg', '')}.png")
		except:
			print('Error to convert images')

