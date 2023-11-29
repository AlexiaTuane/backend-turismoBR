# Use a imagem base do Python
FROM python:3.8

# Configuração do diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt


# Instale o pacote mysqlclient
RUN pip install mysqlclient

# Copie o código-fonte da aplicação para o contêiner
COPY . /app

# Comandos a serem executados quando o contêiner for iniciado
CMD ["python", "manage.py", "runserver"]
