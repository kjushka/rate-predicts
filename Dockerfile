FROM python:3.9
COPY . /rate-predicts
WORKDIR /rate-predicts
RUN pip3 install -r requirements.txt
CMD [ "python3", "main.py"]