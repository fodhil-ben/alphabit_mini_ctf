FROM node:18

WORKDIR /app

COPY challenge/package.json .

RUN npm install

COPY . .

EXPOSE 1330

WORKDIR /app/challenge

CMD ["npm", "start"]
