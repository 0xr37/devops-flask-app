FROM python:3-alpine

WORKDIR /app

RUN pip install flask redis

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "hello", "run", "--host=0.0.0.0"]

