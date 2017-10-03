import datetime
import csv
import random


class Post:
    def __init__(self, title, content):
        self.title = title

        self.date_time = datetime.datetime.now()
        self.content = content
        self.post_id = random.randint(1000000, 9999999)

    def save_post(self):
        post_file = open('post.csv', 'a+')
        fieldnames = ['title', 'date and time', 'content', 'post id']
        writer = csv.DictWriter(post_file, fieldnames=fieldnames)

        writer.writerow(
            {'title': self.title, 'date and time': self.date_time, 'content': self.content, 'post id': self.post_id})

        post_file.close()

    '''def delete_post(self):
        post_file = open('post.csv')
        post_reader = csv.DictReader(post_file)
        title_to_delete = input("Enter title of the post you want to delete: ")

        for row in post_reader:
            if title_to_delete in post_reader == row['title']:'''

    def show_all_posts(self):
        post_file = open('post.csv')
        post_reader = csv.reader(post_file)
        post_data = list(post_reader)

        for i in post_data:
            print('******************************************************')
            for j in range(len(i) - 1):
                return i[j]

        post_file.close()

    def find_in_post(self, value):
        post_file = open('post.csv')
        post_reader = csv.reader(post_file)
        post_data = list(post_reader)

        for i in post_data:
            if value in i:
                print(value)
            else:
                print('No such post')


g = Post("hello", "wow!")

g.save_post()

g.show_all_posts()

g.find_in_post("hello")