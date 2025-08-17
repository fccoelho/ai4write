FROM python:3.13

WORKDIR /code
# Install dependencies
ADD ./requirements.txt /code/requirements.txt
RUN pip install --upgrade -r requirements.txt

ADD . /code

CMD ["python", "app.py"]
