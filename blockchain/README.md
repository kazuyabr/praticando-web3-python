# Instalação inicial

## Dependencias OpenZeppelin
 1 - pip install -r requirements.txt
 2 - ape init
 3 - ape plugins install solidity infura polygon template tokens ens (em caso de usar AWS pode adicionar o plugin aws pois ele ira permitir transações ethereum EVM usando AWS KMS)
 4 - ape plugins install etherscan (opcional caso ja queira fazer deploy e pegar o scan da rede)
 5 - ape plugins install foundry (opcional blockchain de desenvolvimento para nao ter que usar NPM)
 6 - ape plugins install notebook (opcional quando aprender a usar Jupyter Notebook do python podera vir a ser util este plugin)
 7 - ape pm install gh:OpenZeppelin/openzeppelin-contracts --name openzeppelin --version "4.6.0"
 8 - ape compile --include-dependencies -> para compilar todas as dependencias do projeto
 9 - 