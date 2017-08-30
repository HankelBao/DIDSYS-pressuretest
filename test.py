from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(10)
    def index(self):
        self.client.get("/")

    @task(10)
    def get_index_data(self):
        self.client.get("/ajax/get-index")

    @task(2)
    def login_success(self):
        self.client.post("/ajax/get-scorerboard", {
            "username": "hankelbao",
            "password": "arche139286489"
        })

    @task(50)
    def login_username_error(self):
        self.client.post("/ajax/get-scorerboard", {
            "username": "asd",
            "password": "passs"
        })


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
