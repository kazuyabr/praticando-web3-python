# Instalação inicial

## Dependencias OpenZeppelin
 1 - pip install -r requirements.txt
 2 - ape init
 3 - ape plugins install solidity infura polygon template tokens ens etherscan
  4 - ape plugins install aws (em caso de usar AWS pode adicionar o plugin aws pois ele ira permitir transações ethereum EVM usando AWS KMS)
 5 - ape pm install gh:OpenZeppelin/openzeppelin-contracts --name openzeppelin --version "4.6.0"
 6 - ape compile --include-dependencies -> para compilar todas as dependencias do projeto
 