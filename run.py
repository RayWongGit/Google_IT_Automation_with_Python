
#! /usr/bin/env python3

import os
import requests

url = 'http://localhost/fruits/'
path = 'supplier-data/descriptions/'
files = os.listdir(path)

for file in files:
  file_name = os.path.splitext(file)[0]
  file_path = os.path.join(path, file)
  with open(file_path) as f:
    values = f.read().split('\n')
    weight = int(values[1].split(' ')[0])
    im_name = file_name + '.jpeg'
    fruit_dict = {'name':values[0], 'weight':weight, 'description':values[2], 'image_name':im_name}
    response = requests.post(url, json=fruit_dict)
    print(response.status_code)
