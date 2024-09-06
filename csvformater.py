import csv
import pandas as pd
input_filename = 'ChainData.csv'
output_filename = 'output.csv'

 

 
 


def delete_csv_contents(file_path):
    empty_df = pd.DataFrame()
    empty_df.to_csv(file_path, index=False)



def list_of_dict_to_csv(list_of_dicts, output_file):
    fieldnames = list_of_dicts[0].keys()

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        #print(list_of_dicts)
        writer.writerows(list_of_dicts)
            

    #print("List of dictionaries converted to CSV successfully!")

list_dict=[]
def csv_to_dictionary(input_file, key_mapping):
    result_dict = {}
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        list_dict=[]
        for row in reader:
            modified_row = {key_mapping.get(key, key): value for key, value in row.items()}
           # print(modified_row)
            list_dict.append(modified_row)
            #result_dict.update(modified_row)
            
    return list_dict
def remove_symbol_from_list_of_dicts(list_of_dicts, symbol):
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if isinstance(value, str):
                dictionary[key] = value.replace(symbol, '')
    return list_of_dicts

# Example usage:
def csv_for(): 
   
    key_mapping = {'index': 'name'}
    output_list = csv_to_dictionary(input_filename, key_mapping)
    #print(output_list)
    output = remove_symbol_from_list_of_dicts(output_list,symbol=";")
    #print(output)
    list_of_dict_to_csv(output,output_filename)
    #print_csv(output_filename)
    df = pd.read_csv(output_filename)
    #print_csv('output.csv')
    df = df.drop(df[df.data == 'Checking'].index)
    df = df.drop(df[df.data == 'First block data'].index)
    df.pop("timestamp")
#df.pop("name")
    
   
    df.to_csv('output.csv', index=False,mode='w')
    #delete_csv_contents('output.csv')
     