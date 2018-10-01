from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
    
sql_dataframe   = pd.read_sql_table('my_table', engine, columns=['ColA', 'ColB'])
xls_dataframe   = pd.read_excel('my_dataset.xlsx', 'Sheet1', na_values=['NA', '?'])
json_dataframe  = pd.read_json('my_dataset.json', orient='columns')
csv_dataframe   = pd.read_csv('my_dataset.csv', sep=',')
table_dataframe = pd.read_html('http://page.com/with/table.html')[0]


my_dataframe.to_sql('table', engine)
my_dataframe.to_excel('dataset.xlsx')
my_dataframe.to_json('dataset.json')
my_dataframe.to_csv('dataset.csv')

my_dataframe.columns = ['new', 'column', 'header', 'labels']
df.head(5)
df.describe()
df.index
df.dtypes

