#!/usr/bin/env python3

from PIL import Image
import os

path = 'supplier-data/images/'
files =  os.listdir(path)

for file in files:
  if file.endswith('.tiff'):
    file_path = os.path.join(path, file)
    im = Image.open(file_path)
    new_im =  im.convert("RGB").resize((600, 400))
    new_name = os.path.splitext(file)[0] + '.jpeg'
    new_path = os.path.join(path, new_name)
    new_im.save(new_path)
