FROM python:3.7-slim
ADD app/ /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN apt-get update
CMD python api.py