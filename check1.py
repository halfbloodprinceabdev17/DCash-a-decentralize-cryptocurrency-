import json 
import pandas as pd
import os
import csv

def json_to_table(json_data):
    df = pd.json_normalize(json_data) 
    return df
def sql_to_csv():
    pass
def is_valid():
      with open('ChainData.csv','r') as f:
            r=csv.read(f)
            g=sql_to_csv()
            if(r==g):
                 return True
            else:
                 return False
            
#if(is_valid()):       -------> then only this will excecute else ,it will give an error
def chainData():
        i=0
        path = 'chaindata'
        with open('ChainData.txt', 'w'):
             pass
        for filename in os.listdir(path):
             
            if filename.endswith('.json'):
                file_path = os.path.join(path,filename)
                #print(file_path)
                with open(file_path) as file:
                    json_data = json.load(file)
                    table = json_to_table(json_data)
                    df= pd.DataFrame(table)
                    with open('ChainData.txt', 'a') as file: ############
                       if(i==0):
                            df_string = df.to_csv(index=False)
                            file.write(df_string)
                            i+=1
                       else:
                            df_string = df.to_csv(header=False,index=False)
                            file.write(df_string) 
        
        dataframe1 = pd.read_csv("ChainData.txt")
  
# storing this dataframe in a csv file
        
        dataframe1.to_csv('ChainData.csv', 
                  index = None,mode='w')
        #print("chain data\n")
        #print(dataframe1)
        #print("\n")
            #      table = json_to_table(json_data)
            #     file.write(table)
#with open('ChainData.txt', 'r') as file:
#               content = file.read()
#mod = content[:-2]
#with open('ChainData.txt', 'w') as file:
#               file.write(mod)  
  
# readinag given csv file
# and creating dataframe







#with open('ChainData.txt', 'r') as file:
#    json_data = json.load(file)

 


# Display the table
