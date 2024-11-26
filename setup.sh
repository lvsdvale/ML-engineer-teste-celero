#!/bin/bash

ENV_NAME="ml-engineering-test"

REQUIREMENTS_FILE="requirements.txt"


echo "Criando o ambiente Conda '$ENV_NAME'..."
conda create -n $ENV_NAME --yes python=3.12

# Ativando o ambiente
echo "Ativando o ambiente Conda '$ENV_NAME'..."
source activate $ENV_NAME

# Instalando pacotes a partir do arquivo de requisitos
echo "Instalando pacotes a partir do arquivo de requisitos..."
pip install -r $REQUIREMENTS_FILE

echo "Configuração do ambiente '$ENV_NAME' concluída."