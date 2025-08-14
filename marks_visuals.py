import pandas as pd
import matplotlib.pyplot as plt

#Loading the excel file 

try:
    df = pd.read_csv("marksheet.csv")
    #Taking onl starting 50 Students
    df=df.head(50)
    #Extracting names and maths marks 

    names = df['Name']
    Maths_marks=df['Maths']

    #creating bar graph using matplot lib

    plt.figure(figsize=(10,6))
    bars = plt.bar(names,Maths_marks,color='skyblue', edgecolor='black')

    #adding a dashed red line at 35 marks

    plt.axhline(y=35 ,color='red',linestyle='--',linewidth=2,label='Fail Threshold (35 marks)')

    #steps to add the labels and titles

    plt.xlabel("Student Name")
    plt.ylabel("Maths Marks (out of 100)")
    plt.title("Maths Marks of Students ")
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()


    #creating seperate pie chart for the categoriztaions

    fail_count = (df['Maths']<35).sum()
    distinction_count = (df['Maths']>80).sum()
    pass_count = ((df['Maths']>=35)&(df['Maths']<81)).sum()

    labels = ['Fail(<35)','Average Pass(35-80)','Distinction Pass(80+)']
    sizes =[fail_count,pass_count,distinction_count]
    colors=['red','lightgreen','Gold']
    explode=[0.1,0,0.1]

    plt.figure(figsize=(6,6))
    plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=140,explode=explode,shadow=True)
    plt.title("Performance of Students")
    plt.tight_layout()
    plt.show()


except FileNotFoundError:
    print("Error : CSV file not found. ")
except KeyError:
    print("Error: Make sure your CSV file has 'Name' and 'Maths' column.")
except Exception as e:
    print (f"Error{e}")