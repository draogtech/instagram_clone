import datetime
import csv
import random


class Post:
    def __init__(self, title, content):
        self.title = title

        self.date_time = datetime.datetime.now()
        self.content = content
        self.user_id = random.randint(1000000, 9999999)

    def save_post(self):
        post_file = open('post.csv', 'a+')
        fieldnames = ['title', 'date and time', 'content', 'user']
        writer = csv.DictWriter(post_file, fieldnames=fieldnames)

        writer.writerow(
            {'title': self.title, 'date and time': self.date_time, 'content': self.content, 'user': self.user_id, })

        post_file.close()


def delete_post(self):
    post_file = open('post.csv')
    post_reader = csv.DictReader(post_file)
    title_to_delete = input("Enter title of the post you want to delete: ")

    for row in post_reader:
        if title_to_delete in post == row['title']:
                

'''
    def update_post(self):
        pass

    def show_all_posts(self):
        pass'''

g = Post("gghh", "wow!")

g.save_post()
