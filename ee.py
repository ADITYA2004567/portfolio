import pandas as pd

excel_file = r"C:\Users\Sharm\OneDrive\Desktop\sprint\entryValues.xlsx"
xls = pd.ExcelFile(excel_file)
print(xls.sheet_names)  # See available sheets
