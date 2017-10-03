import csv
import datetime


class Like:
    def __init__(self):
        pass


class Comment:
    def __init__(self, comment={}):
        self.comment = comment
        self.time = datetime.datetime.now()

    def add_comment(self, user_comment):
        self.user_id
        self.comment[self.user_id] = [user_comment]
        # for user_id in self.comment.keys():
        #     print(user_id)

    def show_all(self):
        print(self.comment)

    def remove(self, user_comment):

        if user_comment in self.comment.keys():
            del self.comment[user_comment]
            print("Comment delete ")

    def save(self):
        save_comment = open('comments.csv', 'a+')
        field_names = ["user_id", "comment", "time"]
        comments = csv.DictWriter()
        comments.writerow({"user_id": self.user_id, "comment": self.comment, "time":self.time})


class Share:
    def __init__(self):
        pass
