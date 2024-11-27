FROM node:16-slim

WORKDIR /app

COPY . .

RUN npm install -g http-server

CMD ["http-server", "-p", "80"]
