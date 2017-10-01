import datetime
import csv
import randint
from random


class Post:
    def __init__(self, title="", date_time="", content="", user_id=""):
        self.title = title
        self.date_time = date_time
        self.content = content
        self.user_id = user_id

    def publish_post(self):
        self.title = input("Please enter the title of your post: ")
        self.date_time = datetime.datetime.now()
        self.content = input("Please type your post: ")
        self.user_id = randint(1000000, 9999999 + 1)


        post_file_writer =open('post.csv', 'w', newline='').writerow([self.title, self.date_time, self.content, self.user_id])

    def delete_post(self):
        pass

    def update_post(self):
        pass

    def show_all_posts(self):
        pass
