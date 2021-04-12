from bs4 import BeautifulSoup 
import pandas as pd 
from tabulate import tabulate
import json 
import os 
import time 

#read_file = open('html/1.html', "r", encoding='utf-8')
#soup = BeautifulSoup(read_file, 'html.parser')

'''   
def write_json(data, filename='data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
'''
print("Pandas Power \n")

one_page = pd.DataFrame()
temp = []

'''
for filename in os.listdir('html_test'):
    print(filename)
'''
filename = 'test'
df_table = pd.read_html(r'html_test\1.html', encoding='utf-8')
time.sleep(5)
print(f"Total tables: {len(df_table)}")
for i in range(1, len(df_table)):
    #one_page['Table'] = i
    print('Starting Table: ' + str(i))
    df1 = df_table[i]
    df1['table'] = i
    #print(tabulate(df1.head()))
    print(df1.shape)
    #df1.to_json('data.json', orient='records')
    #print(df1.columns)
    print('-----x-----')

    one_page = one_page.append(df1)
    temp.append(df1.to_dict())

    ## Converting JSON with append method
    with open('{}.json'.format(filename), 'w') as f:
        #json.dump(temp, f)
        f.write(json.dumps(temp, indent=2))
#print('{} is done'.format(filename))


'''
## Using Dataframe to covert JSON 
print(one_page.columns)
print(one_page.shape)
result = one_page.to_json('sample.json', orient='records')
'''




