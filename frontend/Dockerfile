FROM node:16

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar arquivos do frontend para o contêiner
COPY . .

# Instalar dependências
RUN npm install -g http-server

# Expor a porta para o servidor
EXPOSE 3000

# Comando para iniciar o servidor
CMD ["http-server", "-p", "80"]
