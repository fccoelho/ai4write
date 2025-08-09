FROM python:3.13

WORKDIR /code
ADD ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ADD . /code

CMD ["python", "app.py"]
