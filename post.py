import datetime
import csv




class Post:
    def __init__(self, title="", date_time="", content="":
        self.title = title
        self.date_time = date_time
        self.content = content

    def publish_post(self):

        post_file = open('post.csv', 'w', newline='').
        post_reader = csv.writerow([self.title, self.date_time, self.content])


        post_file.close()

    def delete_post(self):
        post_file = open('post.csv')
        post_reader = csv.reader(post_file)
        title_to_delete = input("Enter title of the post you want to delete: ")

        for row in post_reader:
            if title_to_delete in post == True

    def update_post(self):
        pass

    def show_all_posts(self):
        pass
