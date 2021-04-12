from bs4 import BeautifulSoup 
import pandas as pd 
from tabulate import tabulate
import json 
from glob import glob 
import os 
import time 

#read_file = open('html/1.html', "r", encoding='utf-8')
#soup = BeautifulSoup(read_file, 'html.parser')


print("Pandas Power \n")

one_page = pd.DataFrame()
need_format = {}

table = []

file_dir = glob('html/*.html')

finalist = []
for f in file_dir:
    name = os.path.basename(f).replace(".html", "_page")
    
    print(name)
    df_table = pd.read_html(f, encoding='utf-8')
    print(f"Total tables: {len(df_table)}")

    temp = []
    for i in range(1, len(df_table)):
        #table.append(i)
        print('Starting Table: ' + str(i))
        df1 = df_table[i]
        #df1['table'] = i
        #print(tabulate(df1.head()))
        print(df1.shape)
        #print(df1.columns)
        print('-----x-----')

        one_page = one_page.append(df1)
        temp.append(df1.to_dict())

    need_format['Data'] = temp 

    print('{} is done'.format(name))
## Converting JSON with append method
    finalist.append(need_format)


with open('export.json', 'w') as f:
    #json.dump(temp, f)
    f.write(json.dumps(finalist, indent=2))

    


'''
## Using Dataframe to covert JSON 
print(one_page.columns)
print(one_page.shape)
result = one_page.to_json('sample.json', orient='records')
'''




