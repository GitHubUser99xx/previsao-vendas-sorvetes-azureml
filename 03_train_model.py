from azureml.core import Workspace, Dataset
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Conectando ao workspace
ws = Workspace.from_config()

# Carregando dataset
datastore = ws.get_default_datastore()
dataset = Dataset.Tabular.from_delimited_files(path=(datastore, 'path_to_data.csv'))
data = dataset.to_pandas_dataframe()

# Preparando dados
X = data[['temperatura']]
y = data['quantidade_vendida']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Avaliando modelo
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print(f'MAE: {mae}, RMSE: {rmse}')
