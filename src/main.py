# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV

import os
import pandas as pd
from datetime import datetime

# Stores the path to the home directory
main_root = "/workspaces/exercise-terminal-challenge-pilarzarco"

# Recursively traverse the main_root
def list_files(main_root):
    files = [] 
    for current_folder, subfolder, files_folder in os.walk(main_root):
        for file in files_folder:
            files.append(os.path.join(current_folder, file))
    return files

# Get file size in bytes
def file_size(files):
    sizes = []
    for file in files:
        size = os.path.getsize(file)
        sizes.append(size)
    return sizes

# Obtain modification dates
def get_dates(files):
    file_date = []
    for file in files:
        date_amendment = os.path.getmtime(file)
        file_date.append(datetime.utcfromtimestamp(date_amendment).strftime('%d/%m/%Y %H:%M:%S'))
    return file_date

# Call the functions to collect the information from the files in the file.
all_files = list_files(main_root)
file_weight = file_size(all_files)
file_date = get_dates(all_files)

# Create DataFrame
files_pd = pd.DataFrame({'File': [os.path.basename(file) for file in all_files], 'Size': file_weight, 'Date': file_date})
print(files_pd.head(20))
