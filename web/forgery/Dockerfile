FROM node:14


RUN mkdir -p /app/challenge/main /app/challenge/internal

WORKDIR /app/challenge/main
COPY ./challenge/main/package.json .
RUN npm install
COPY ./challenge/main .


WORKDIR /app/challenge/internal
COPY ./challenge/internal/package.json .
RUN npm install
COPY ./challenge/internal .

WORKDIR /app
RUN mv challenge/internal/.env .

COPY entrypoint.sh .

EXPOSE 1335

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]

