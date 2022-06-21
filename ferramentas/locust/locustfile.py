from locust import HttpUser, LoadTestShape, task, between

class TestLocust(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_delay_1(self):
        self.client.get("/delay/1")

class StagesShape(LoadTestShape):

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
