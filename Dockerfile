FROM python:3.10

ADD main.py .
ADD src/ src/
ADD requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt -v

CMD [ "python", "./main.py" ]