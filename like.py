import datetime


class Like:
    def __init__(self, post_id, user_id, time):
        self.post_id = post_id
        self.user_id = user_id
        self.time = datetime.datetime.now()
        self.like = False

    def like_is_ok(self):
        self.like = True
        return self.like

    def like_is_notok(self):
        self.like = False
        return self.like

if __name__ == "__main__":
    like = Like()


