FROM python:3.9
 
WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY . /code/app

RUN apt-get update && \
    apt-get install -y telnet && \
    apt-get clean

CMD ["python", "/code/app/realtime_data_client.py"]
