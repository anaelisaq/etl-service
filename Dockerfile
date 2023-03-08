FROM python:3.9

ENV PYTHONUNBUFFRERED 1

WORKDIR /app

COPY requirements.txt /app/

COPY main.py /app/

COPY base_teste.txt /app

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "main.py"]