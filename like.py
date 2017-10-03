import datetime


class Like:
    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id
        self.time = datetime.datetime.now()
        self.like = False

    def like_post(self):
        self.post_id
        



    def like_comment(self):
        self.like = True
        self.time = datetime.datetime.now()
        return self.like, self.time

new_like = Like
print(new_like.set_like(Like(1, 2)))
