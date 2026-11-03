import pandas as pd

def verify_retail_data():
    file_name = 'online_retail_II.xlsx'
    print(f"Attempting to load {file_name}...")
    
    try:
        # sheet_name=None loads all sheets into a dictionary of DataFrames
        sheets = pd.read_excel(file_name, sheet_name=None)
        df = pd.concat(sheets.values())
        
        print("\n--- Dataset Verification ---")
        print(f"Total number of rows: {len(df):,}")
        print(f"Total number of columns: {len(df.columns)}")
        
        print("\n--- Missing Values per Column ---")
        print(df.isna().sum())
        
    except FileNotFoundError:
        print(f"\n[!] Error: The file '{file_name}' was not found in this directory.")
        print("Please ensure you run this script from the 'online+retail+ii' directory.")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")

if __name__ == '__main__':
    verify_retail_data()
