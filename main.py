import bs4
import numpy
import pandas
import requests
import matplotlib

# get data
html = requests.get('https://www.worldometers.info/coronavirus/')
print(html.content)

# parse html and find the table
html_parse = bs4.BeautifulSoup(html.content)
table = html_parse.find('table', attrs={'id': 'main_table_countries_today'})
print(table)

# get the rows
rows = table.find_all('tr')
print('First row:', rows[0])
print('\nFirst row:', rows[0].text.strip())
print('\nFirst row:', rows[0].text.strip().split('\n'))
print('\nFirst country:', rows[9].text.strip().split('\n'))

# convert list into DataFrame
data = []

for x in rows:
  data.append(x.text.strip().split('\n')[1:5])

df = pandas.DataFrame(data)
print(df.head())

df = pandas.DataFrame(data[9:],columns=data[0])
print(df.head())

df.to_csv('covid19.csv')

df_plot = df[['Country,Other','TotalCases']]
df_plot = df_plot[:10]
print(df_plot.head())