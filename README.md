# previsao-vendas-sorvetes-azureml

# Previsão de Vendas de Sorvetes com Base na Temperatura - Azure Machine Learning

Este projeto tem como objetivo criar um modelo de machine learning para prever a quantidade de sorvetes vendidos com base na temperatura utilizando o Azure Machine Learning.

## Estrutura do Projeto

- `01_connect_workspace.py` - Código para conectar ao workspace do Azure ML.
- `02_load_data.py` - Código para carregar dados do Azure Blob Storage e transformar em DataFrame.
- `03_train_model.py` - Código para treinar e avaliar um modelo de regressão linear.
- `04_register_model.py` - Código para salvar e registrar o modelo treinado no Azure ML.

## Requisitos

- Python 3.7+
- azureml-sdk
- scikit-learn
