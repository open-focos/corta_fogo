"""
Obte daods de Municipíos que aderirm 
"""

from pathlib import Path

import requests
from paths import input_path


# URL
URL = 'https://smastr16.blob.core.windows.net/cortafogo/sites/10/2020/10/municipios_aderentes_2020_outubro.pdf'

# File
file = input_path / Path(URL).name


if __name__ == '__main__':
    # Request
    r = requests.get(URL, timeout=60)
    with open(file, 'wb') as f:
        f.write(r.content)
        
    print('Download Ok!')
