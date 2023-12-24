FROM node:14

WORKDIR /app

COPY ./challenge/package.json .

RUN npm install

COPY ./challenge .

EXPOSE 1337

CMD ["npm", "start"]

