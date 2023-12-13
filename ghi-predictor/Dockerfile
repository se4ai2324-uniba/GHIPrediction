# Usa un'immagine di Node.js come base
FROM node:14-alpine

# Imposta la directory di lavoro su /
WORKDIR /ghi-predictor

# Copia i file package.json e package-lock.json (se esistono)
COPY package*.json ./

# Installa le dipendenze
RUN npm install

# Copia il resto dell'applicazione
COPY . .

# Costruisci l'applicazione React per la produzione
RUN npm run build

# Espone la porta 80 per rendere l'applicazione accessibile al di fuori del container
EXPOSE 3000

# Comando per eseguire l'applicazione quando il container viene avviato
CMD npm start
