from python:latest
copy requirements.txt .
workdir .
run pip install --upgrade pip
run pip3 install -r requirements.txt

