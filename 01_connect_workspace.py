from azureml.core import Workspace
# Conectando ao seu workspace no Azure
ws = Workspace.from_config()  # Certifique-se de que o arquivo config.json está no diretório atual
print("Conectado ao workspace:", ws.name)
