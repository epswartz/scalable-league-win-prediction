# scalable-league-win-prediction

A scalable service for predicting wins in League of Legends using logistic regression. Built to demonstrate containerized scalability on GKE.

# Running Locally
1. `python3 main.py`
2. To test with `httpie`: `http POST localhost:8080/predict < test_payload.json`

# Deployment on GKE
1. Create a GKE cluster
2. `kubectl apply -f ./kube/deployment.yaml`
3. `kubectl apply -f ./kube/service.yaml`

# Load Testing
1. `pip install locust`
2. `make locust host=<HOST>`