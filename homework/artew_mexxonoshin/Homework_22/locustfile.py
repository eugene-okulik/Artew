from locust import task, HttpUser
import random


class JsonPlaceholderUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"

    @task(5)
    def get_posts(self):
        self.client.get("/posts")

    @task(4)
    def get_comments(self):
        post_id = random.randint(1, 100)
        self.client.get(f"/comments?postId={post_id}")

    @task(3)
    def get_albums(self):
        self.client.get("/albums")

    @task(2)
    def get_photos(self):
        album_id = random.randint(1, 100)
        self.client.get(f"/photos?albumId={album_id}")

    @task(1)
    def get_todos(self):
        user_id = random.randint(1, 10)
        self.client.get(f"/todos?userId={user_id}")

    @task(1)
    def get_users(self):
        self.client.get("/users")

    @task(1)
    def create_post(self):
        data = {
            "title": "Test Post",
            "body": "body_body_body",
            "userId": 1
        }
        self.client.post("/posts", json=data)