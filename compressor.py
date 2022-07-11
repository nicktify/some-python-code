from PIL import Image # python3 -m pip install Pillow

import os
import sys

dir_path = os.getcwd()

for filename in sys.argv[1:]:
    file_path = os.path.join(dir_path, filename)
    name, extension = os.path.splitext(dir_path + '/' + filename)

    if extension in [".jpg", ".jpeg", ".png"]:
        picture = Image.open(file_path)
        path_to_save = os.path.join(dir_path, "compressed_" + filename)
        picture.save(path_to_save, optimize=True, quality=60)
