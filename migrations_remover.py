#!/usr/bin/env python

import os
import re

path = os.walk('.')
pattern = re.compile(r'^[0-9]\d+\w*(.py)')

os.remove('db.sqlite3')

for root, directories, files in path:
    for file in files:
        for migration_file in pattern.findall(file):
            path_to_file = os.path.join(root, migration_file)
            os.remove(path_to_file)

os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
