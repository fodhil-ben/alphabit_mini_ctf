FROM node:14

WORKDIR /app

COPY ./challenge/package.json .

RUN npm install

COPY ./challenge .

EXPOSE 1333

CMD ["npm", "start"]

