import pandas as pd

try:
    df = pd.read_excel("Nations_Capitals_data.xlsx", engine="openpyxl")
    
    df['Country'] = df['Country'].astype(str).str.strip().str.lower()
    df['Capital City'] = df['Capital City'].astype(str).str.strip()
    
    df = df.dropna(subset=['Country', 'Capital City'])
    
    Nations_to_capitals = dict(zip(df['Country'], df['Capital City']))
    
    # Get user input
    user_input = input("Enter the name of Country: ").strip().lower()
    
    if user_input in Nations_to_capitals:
        print(f"The capital of {user_input.title()} is {Nations_to_capitals[user_input]}")
    else:
        print("Nation not found. Please check the spelling or try again.")
        
except FileNotFoundError:
    print("Error: Excel file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
