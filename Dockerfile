# Dockerfile, Image, Container
FROM python:3.9


COPY requirements.txt requirements.txt
RUN pip install --requirement requirements.txt

COPY . .
CMD [ "python", ".lib/main.py" ]