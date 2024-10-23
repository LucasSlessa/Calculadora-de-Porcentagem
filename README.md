# Calculadora de Porcentagem

Este projeto é uma calculadora de porcentagem que lê um arquivo CSV e identifica os valores digitados na coluna "observação". Em seguida, soma esses valores e calcula a porcentagem com base na soma total.

## Funcionalidades

- Carregar dados de um arquivo CSV.
- Identificar e somar valores da coluna "observação".
- Calcular a porcentagem com base na soma total dos valores identificados.

## Tecnologias Utilizadas

- Python
- Pandas

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)
- Um editor de texto ou IDE (recomendado: Visual Studio Code, PyCharm, etc.)

### Instalação do Ambiente

1. Instalar Python
Acesse python.org e baixe a versão mais recente do Python.
Siga as instruções de instalação, certificando-se de marcar a opção "Add Python to PATH".

3. Verificar Instalação do Python
Abra o terminal ou o prompt de comando e execute o seguinte comando:

```
python --version
```

Isso deve retornar a versão do Python instalada.

### Criar um Diretório de Projeto

Crie um diretório para o seu projeto:

```
mkdir projeto_soma_porcentagem
cd projeto_soma_porcentagem
```
Criar um Ambiente Virtual (opcional, mas recomendado)

Execute o seguinte comando para criar um ambiente virtual:

```
python -m venv venv
```
## Ative o ambiente virtual:

Windows:

```
venv\Scripts\activate
```
Linux/Mac:

```
source venv/bin/activate
```
## Bibliotecas
Instale a biblioteca pandas, que é necessária para o seu script. Execute:

```
pip install pandas

```
# Uso do Sistema

- Preparar o Arquivo CSV

- Certifique-se de que o arquivo tabela.csv esteja localizado no mesmo diretório que o seu script soma.py. O arquivo deve estar formatado corretamente, conforme a estrutura de colunas que você mencionou anteriormente.

- Criar o Script Python

- Crie um arquivo chamado soma.py no diretório do projeto e cole o seguinte código:

```
import pandas as pd
```

# Carregar a tabela CSV
```
df = pd.read_csv('tabela.csv', encoding='ISO-8859-1', delimiter=';', on_bad_lines='skip')
```

# Exibir as colunas disponíveis para confirmar
```
print("Colunas disponíveis na tabela:", df.columns)
```

# Filtrar e limpar a coluna "Unnamed: 16"
```
df['Unnamed: 16'] = df['Unnamed: 16'].str.replace(',', '.', regex=False)  # Trocar vírgulas por pontos
df['Unnamed: 16'] = pd.to_numeric(df['Unnamed: 16'], errors='coerce')  # Converter para numérico, substituindo erros por NaN
```

# Somar apenas os valores numéricos, ignorando NaN
```
soma = df['Unnamed: 16'].sum(skipna=True)
```

# Exibir o resultado da soma
```
print("A soma dos valores da coluna 'Unnamed: 16' é:", soma)
```

# Solicitar ao usuário a porcentagem desejada
```
porcentagem_input = input("Digite a porcentagem que deseja calcular: ")
```

# Validar a entrada e calcular a porcentagem
```
try:
    porcentagem = float(porcentagem_input)
    valor_porcentagem = (porcentagem / 100) * soma
    print(f"A porcentagem de {porcentagem}% sobre a soma é: {valor_porcentagem}")
except ValueError:
    print("Por favor, insira um valor numérico válido para a porcentagem.")
```
### Executar o Script

No terminal ou prompt de comando, execute o seguinte comando:

bash
Copiar código
python soma.py
O programa irá calcular a soma dos valores na coluna Unnamed: 16 do arquivo tabela.csv e solicitar que você insira a porcentagem desejada.

Estrutura de Arquivos
A estrutura do seu projeto deve ser semelhante a esta:

```
projeto_soma_porcentagem/
│
├── venv/                # Ambiente virtual (se criado)
├── tabela.csv           # Arquivo CSV com os dados
└── soma.py              # Script Python

```
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto é licenciado sob a MIT License.
