from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:9000"
    wait_time = between(5.0, 9.0)

    @task
    def endpoint_index(self):
        self.client.get("/")

    @task(3)
    def endpoint_world_stats(self):
        self.client.get("/world-stats")
