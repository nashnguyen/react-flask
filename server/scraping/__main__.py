import os
import sys

import pandas
import requests
from bs4 import BeautifulSoup

# Append root path for absolute import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from models import engine

html = requests.get('https://hoopshype.com/salaries/players/')
soup = BeautifulSoup(html.text, 'html.parser')

final_df = pandas.DataFrame()

url_list = soup.find(class_='team-list-ul')
url_list_item = url_list.find_all('a', href=True)

for url_item in url_list_item:
    html = requests.get(url_item['href'])
    soup = BeautifulSoup(html.text, 'html.parser')

    array = []
    table = soup.find('table')
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td]
        array.append(row)

        temp_df = pandas.DataFrame(array)
        temp_df.columns = temp_df.iloc[0].str.lower()
        temp_df = temp_df[1:]
        temp_df.head()
        temp_df.drop(list(temp_df.filter(regex='^$|(\*)')), axis=1, inplace=True)
        temp_df = temp_df.melt(id_vars='player', var_name='season', value_name='salary')

    final_df = pandas.concat([final_df, temp_df])
    final_df = final_df.replace({'salary': {'\$': '', ',': ''}}, regex=True).astype(
        {'player': 'string', 'season': 'string', 'salary': 'int32'}
    )

final_df.to_sql(
    'salary',
    con=engine,
    if_exists='replace',
    index=True,
    index_label="id",
    method='multi',
)
