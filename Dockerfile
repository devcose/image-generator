FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
# ENTRYPOINT ["python", "main.py"]
