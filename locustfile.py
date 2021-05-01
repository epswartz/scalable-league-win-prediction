from locust import HttpUser, task
import json

with open('test_payload.json', 'r') as f:
    payload = json.load(f)

class APIUser(HttpUser):
    """
    Simulated API user for load testing.

    Only has one action, which is calling the single endpoint.
    """

    #wait_time = between(1.5, 2.5)

    @task
    def predict(self):
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        self.client.post(
            "/predict",
            data=json.dumps(payload),
            headers=headers,
            name = "Predict Win Probability"
        )
