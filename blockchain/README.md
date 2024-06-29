# Instalação inicial

## Dependencias OpenZeppelin
 1 - pip install -r requirements.txt
 2 - ape init
 3 - ape plugins install . (o ponto servira para instalar todos os plugins presentes em ape-config.yaml)
  4 - ape plugins install aws (opcional em caso de usar AWS pode adicionar o plugin aws pois ele ira permitir transações ethereum EVM usando AWS KMS)
 5 - ape pm install gh:OpenZeppelin/openzeppelin-contracts --name openzeppelin --version "4.6.0"
 6 - ape compile --include-dependencies -> para compilar todas as dependencias do projeto
 
 ## Geração de contas
 1 - ape accounts generate <name_account>(gera conta para trabalhar com o console)
 2 - ape accounts export <name_account>(exporta a chave privada)