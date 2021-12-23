FROM python:3.9-alpine

#COPY ./requirements.txt /app/
ADD  . /app 
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# CMD ["python", "app.py"]
