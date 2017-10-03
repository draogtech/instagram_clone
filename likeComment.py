class LikeComment():
    def __init__(self):
        self.like = False

    def like_is_ok(self):
        self.like = True
        return self.like

    def like_is_notok(self):
        self.like = False
        return self.like

if __name__ == "__main__":
    like_comment = LikeComment()

    print(like_comment.like_is_notok())
