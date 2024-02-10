FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y gcc pkg-config python-dev-is-python3 default-libmysqlclient-dev libssl-dev

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "api.py" ]