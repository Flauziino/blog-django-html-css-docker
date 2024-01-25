FROM python:3.11.3-alpine3.18
LABEL mantainer="https://github.com/Flauziino"

# Configurações do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copia o conteúdo do diretório atual para /djangoapp dentro do contêiner
COPY . /djangoapp
COPY djangoapp/requirements.txt /djangoapp/requirements.txt
COPY djangoapp /djangoapp
COPY djangoapp/manage.py /djangoapp/



# Copia o diretório scripts para /scripts dentro do contêiner
COPY scripts /scripts

# Define o diretório de trabalho dentro do contêiner
WORKDIR /djangoapp/


# Porta exposta
EXPOSE 8000

# Configuração do ambiente e dependências
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media && \
    chmod -R +x /scripts

RUN /venv/bin/pip install -r /djangoapp/requirements.txt
# Adiciona a pasta scripts e venv/bin no $PATH do container
ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["sh", "/scripts/commands.sh"]
