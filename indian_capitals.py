import pandas as pd

try:
    df = pd.read_excel("Capitals_data.xlsx",engine = "openpyxl")
    states_to_capitals = dict(zip(df['State'].str.lower(),df['Capital']))

    #taking input from user

    user_input=input("Enter the name of indian state :").strip().lower()

    if user_input in states_to_capitals:
        print(f"The capital of {user_input.title()} is {states_to_capitals[user_input]}")
    else:
        print("State not found. Please check the spelling or try again. ")


except FileNotFoundError:
    print("Error:Excel file not found ")
except Exception as e:
    print(f"An error occured :{e}")



#Store Ball wise runs for ten overs and draw the line graph with the runs Highlight with the green mark if there is sixer
#read data from student and marks from student table and show passing mark in bargrafh 