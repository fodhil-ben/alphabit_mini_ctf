FROM python:3.8-alpine

WORKDIR /app
COPY ./challenge .

RUN pip3 install -r requirements.txt

EXPOSE 1332
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=1332"]