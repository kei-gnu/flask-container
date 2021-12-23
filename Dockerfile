FROM python:3.9-alpine

WORKDIR /app
COPY ./requirements.txt /app/
COPY ./app /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "app.py"]