# 04_register_model.py

from azureml.core import Workspace, Model, Dataset
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Conectando ao workspace
ws = Workspace.from_config()

# Carregando dataset
datastore = ws.get_default_datastore()
dataset = Dataset.Tabular.from_delimited_files(path=(datastore, 'path_to_data.csv'))
data = dataset.to_pandas_dataframe()

# Preparando dados
X = data[['temperatura']]
y = data['quantidade_vendida']

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Salvando modelo localmente
joblib.dump(model, 'modelo_vendas_sorvete.pkl')

# Registrando modelo no Azure ML
registered_model = Model.register(workspace=ws,
                                  model_path='modelo_vendas_sorvete.pkl',
                                  model_name='modelo_vendas_sorvete')

print("Modelo registrado com sucesso:", registered_model.name)
