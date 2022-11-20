FROM python:3.9
COPY . /rate-predicts
WORKDIR /rate-predicts
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN PYTHONPATH=/usr/bin/python pip install -r requirements.txt
CMD [ "python3", "main.py"]
