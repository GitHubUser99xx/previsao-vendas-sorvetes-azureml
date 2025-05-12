from azureml.core import Workspace, Dataset
# Conectando ao workspace
ws = Workspace.from_config()
# Acessando o datastore padrão
datastore = ws.get_default_datastore()
# Carregando o dataset a partir de um arquivo CSV no datastore
dataset = Dataset.Tabular.from_delimited_files(path=(datastore, 'path_to_data.csv'))
# Convertendo dataset para DataFrame Pandas para manipulação local
data = dataset.to_pandas_dataframe()
print(data.head())
