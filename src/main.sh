#!/bin/bash

# THIS CODE IS PASSED THROUGH THE BASH TERMINAL to create a csv with the data of the whole directory in the main root.

# Main directory
main_root="/workspaces/exercise-terminal-challenge-pilarzarco"

# Create CSV file headers
echo "File, Size, Date" > archivos.csv

# Traverses directory and subdirectories
find "$main_root" -type f | while read -r file; do
    # Gets the name of the file
    file_name=$(basename "$file")

    # Gets file size in bytes
    file_size=$(stat -c %s "$file")

    # Gets the modification date formatted in a readable format
    file_date=$(date -d "@$(stat -c %Y "$file")" "+%d/%m/%Y %H:%M:%S")

    # Add the information to the CSV file
    echo "$file_name,$file_size,$file_date" >> archivos.csv
done

# Completed
echo "CSV exported to .csv files"

