class Comments:
    def __init__(self, comment={}):

        self.comment = comment


    def add_comment(self):
        iduser = input("Enter your ID")
        yourcomment = input("Enter your Comment")
        youremail = input("Enter your Email")

        self.comment.setdefault(iduser,[]).append(yourcomment)
        self.comment[iduser].append(youremail)


        for iduser in self.comment.keys():
            print(iduser)

    def search(self,find):

        if find in self.comment.keys():
            look = self.comment[find]
            print ("yourcomment: " + look[0])

    def remove(self,rmve):

        if rmve in self.comment.keys():
            del self.comment[rmve]
            print ("Comment delete ")

new = Comments()

check = input("To add comment press 1, To search comment press 2, To delete comment press 3, To exit press 4:  " )


while check != "4":

    if check == "1":
        new.add_comment()

    elif check == "2":
        new.search(input("Enter iduser : "))

    elif check == "3":
        new.remove(input("Enter iduser: "))

    check = input("To add comment press 1, To search comment press 2, To delete comment press 3, To exit press 4:  ")





