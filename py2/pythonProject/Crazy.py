import zipfile
with zipfile.ZipFile('cjysb.zip','a') as zipboj:
  zipboj.write('matplotlib.py')