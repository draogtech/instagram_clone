import datetime


class likeComment():
    def __init__(self):
        self.like = False
        self.time = ''

    # def like_is_ok(self):
    #     self.like = True
    #     return self.like
    #
    # def like_is_notok(self):
    #     self.like = False
    #     return self.like

    def condition_is_ok_or_nok(self):
        self.time = datetime.datetime.now()

        if self.like == True:
            self.like = False
        else:
            self.like = True
            print(self.time)

        return self.like


    # def my_time(self):
    #
    #     self.time = datetime.datetime.now()
    #     return self.time




if __name__ == "__main__":
    like_comment = likeComment()
    print(like_comment.condition_is_ok_or_nok())
    # print(like_comment.my_time())


