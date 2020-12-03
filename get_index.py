import os, shutil
import pandas as pd
from pathlib import Path
from irsx.settings import INDEX_DIRECTORY

os.system("irsx_index")

if os.path.isdir('indices'):
    shutil.rmtree('indices')

os.system('mkdir indices')

paths = Path(INDEX_DIRECTORY).rglob('*.csv')
paths_list = [x for x in paths]

for p in paths_list:
    df = pd.read_csv(p, usecols = ['TAXPAYER_NAME', 'OBJECT_ID'], error_bad_lines = False)
    df.to_csv('indices/' + p.name, index = False)

shutil.rmtree(INDEX_DIRECTORY)
