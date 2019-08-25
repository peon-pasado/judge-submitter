from python:latest
copy requirements.txt .
workdir ./root
run pip install --upgrade pip
run pip3 install -r requirements.txt

