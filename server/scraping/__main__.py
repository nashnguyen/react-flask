import pandas as pd
import requests
from bs4 import BeautifulSoup

html = requests.get('https://hoopshype.com/salaries/players/')
soup = BeautifulSoup(html.text, 'html.parser')

final_df = pd.DataFrame()

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

        temp_df = pd.DataFrame(array)
        temp_df.columns = temp_df.iloc[0].str.lower()
        temp_df = temp_df[1:]
        temp_df.head()
        temp_df.drop(list(temp_df.filter(regex='^$|(\*)')), axis=1, inplace=True)
        temp_df = temp_df.melt(id_vars='player', var_name='season', value_name='salary')

    final_df = pd.concat([final_df, temp_df])

final_df.to_csv('data.csv', index=False)
