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

file_dir = glob('html_test/*.html')

finalist = []
page = {}
for f in file_dir:
    name = os.path.basename(f).replace(".html", "_page")
    print(name)
    df_table = pd.read_html(f, encoding='utf-8')
    print(f"Total tables: {len(df_table)}")

    data = []
    table = {}
    for i in range(1, len(df_table)):
        #table.append(i)
        print('Starting Table: ' + str(i))
        table['Table_{}'.format(i)] = df_table[i].to_dict(orient='records')
        #df1['table'] = i
        #print(tabulate(df1.head()))
        #print(df1.shape)
        #print(df1.columns)
        print('-----x-----')
        data.append(table['Table_{}'.format(i)])

    #print(data)
    '''
    print('------Table 1 ----')
    print(table['Table_1'])
    print('*****-*****')
    print('------Table 2 ----')
    print(table['Table_2'])
    '''

    ## adding dataframe into data list 
    page['T1'] = data[0]
    page['T2'] = data[1]

    

#print('DF Length : {}'.format(len(data)))
print('..........****..........')
print(page['T1'])
print('..........****..........')
#print('{} is done'.format(name))
#print('-----x-----')


    #table['Data'] = data 


## Converting JSON with append method
#finalist.append(page)

#print(finalist)

'''
with open('export.json', 'w') as f:
    #json.dump(temp, f)
    f.write(json.dumps(finalist, indent=2))
'''
    


'''
## Using Dataframe to covert JSON 
print(one_page.columns)
print(one_page.shape)
result = one_page.to_json('sample.json', orient='records')
'''

'''
JSON: {
    Page1:
        {
            Table1: {

            },

            Table2: {

            }
        },

    Page2:
        {
            Table1: {

            },
            Table2: {

            }
        }, 

}
'''

