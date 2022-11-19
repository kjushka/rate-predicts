FROM python:3.9
COPY . /rate-predicts
WORKDIR /rate-predicts
RUN pip install -r requirements.txt
CMD [ "python3", "main.py"]