FROM python:3.9-alpine

WORKDIR /code

ENV FLASK_APP inicio.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

RUN apk add build-base

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY . .

RUN chmod +x boot.sh

# CMD [ "flask", "run" ] ejecutaría el servidor de flask
# que no debemos utilizar en producción, pero nos podria servir
# en desarrollo y no haria falta gunicorn.
# tambien en vez de un punto de entrada podriamos utilizar
# CMD [ "gunicorn", "-b", ":5000", "inicio:app"]

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]