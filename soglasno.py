import os
import glob
import openpyxl

directory = r"C:\Users\admin.LAPTOP-M704372G.000\Desktop\gau_gmt_bot\newAge"

# Find all Excel files in the directory and its subfolders
excel_files = glob.glob(os.path.join(directory, "**/*.xlsx"), recursive=True)

# Loop through each Excel file and search for the string
for file in excel_files:
    wb = openpyxl.load_workbook(file)
    for sheet in wb.worksheets:
        for row in sheet.iter_rows(values_only=True):
            for cell in row:
                if cell is not None and isinstance(cell, str) and cell.startswith("Согласно"):
                    with open(r"C:\Users\admin.LAPTOP-M704372G.000\Desktop\gau_gmt_bot\newAge\file.txt", "a") as f:
                        f.write(f" {cell}\t;\n")
