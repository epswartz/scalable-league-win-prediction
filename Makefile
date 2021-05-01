locust: # Use with make locust host=<host>
	locust --host $(host) --locustfile locustfile.py

build:
	docker build -t league-win-prediction .

install:
	pip install --upgrade pip
	pip install -r requirements.txt
