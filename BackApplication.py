import sync
import time
import check1
import csvformater
import sqltocsv
import csv
import checknodes
import pandas as pd
import LocalDatabaseCheck as LDC
i=10

def loading():
        for i in range(14):
            print("Starting Security Check" + "." * i, end="\r")
            time.sleep(0.5)
def main1():

    loading()
   
    check1.chainData()
   
    csvformater.csv_for()

    try : 
        sqltocsv.sql_load()
    except Exception:
        pass       
def check_column_similarity(file1, file2, column_name):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.DictReader(f1)
        reader2 = csv.DictReader(f2)

        # Get the column values from each file
        column_values1 = [row[column_name] for row in reader1]
        column_values2 = [row[column_name] for row in reader2]

        # Check if the column values are the same
        if column_values1 == column_values2:
             
            return True
        else:
            
            return False
 
def check():
    file1 = 'output.csv'
    file2 = 'data.csv'
    column_name = 'data'

    return check_column_similarity(file1, file2, column_name)



while(i>=0):
    main1()
    sync.sync(save=True)
    time.sleep(8)
    #print(check())
    #loading()
    if(check() and checknodes.check()):
        print("Check : ",check())
        print("node :",checknodes.check())
        print("No malicious behavior was detected.")
       
    else:
        #print("*&^%"*50)
        #print("\n")
        print("Check : ",check())
        print("node :",checknodes.check())
        print("Malicious behavior was detected. Data has been compromised \n Perform measurements immedietly")
        LDC.main()
        #print("\n")
        #print("*&^%"*50)
       
        break
    i-=1