# coding: utf-8

import zipfile

try:
    zipped_file = zipfile.ZipFile('exit.zip')
except IOError as ioe:
    print('Algum problema ao ler o arquivo {}'.format(ioe.filename))
else:
    zipped_file.extractall(path = 'banco')