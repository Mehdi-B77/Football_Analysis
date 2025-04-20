FROM python:3.9-slim 

WORKDIR /app

COPY . /app/


RUN ls /app



RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8080 

CMD ["python", "data_football.py"]

