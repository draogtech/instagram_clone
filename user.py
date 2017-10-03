import re
import bcrypt
import random
import csv


class User(object):

    def __init__(self, username, email, password):
        self.user_id = random.randint(10000000, 9999999999999)
        self.username = username
        self.email = email
        self.password = password
        self.bio =''
        self.location=''
        self.following = []
        self.followers = []

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def email(self):
        return self._email

    @username.setter
    def username(self, name):
        if self.findall(name) != True:
            self._username = name
        else:
            return 'username already in use'

    @email.setter
    def email(self, emailstring):
        try:
            if re.match(r"^[\w\.+\-]+\@[\w]+\.[a-z]{2,3}$", emailstring):
                if self.findall(emailstring) != True:
                    self._email = emailstring
                else:
                    return "Email already in use"
            else:
                raise ValueError('Not a valid email')
        except ValueError as e:
            print ("Please enter a valid Email")

    @password.setter
    def password(self, value):
        if len(value) >= 8:
            if re.match(r'[A-Za-z0-9@#$%^&+=]', value):
                self._password = bcrypt.hashpw(value, bcrypt.gensalt())
            else:
                raise ValueError(
                    'Password can only contain the alphanumeric characters')
        else:
            raise ValueError('Password must be 8 or more characters')

    def check_password(self, password):
        if bcrypt.checkpw(password, self._password):
            return True
        return False

    def findall(self, value):
        user = open('users.csv' , 'r')
        userfile = csv.reader(user)
        for vals in userfile:
            if value in vals:
                return True
            return False

    def send_email(self, email):
        pass

    def validate_email(self, value):
        pass

    def add_bio(self, value):
        return self.bio = value


    def is_following(self, other):
        for val in self.following:
            if other in  

    def followers(self):
        pass
    def save_user(self):
        users = open('users.csv', 'a+')
        fieldnames = ['User_Id', 'Username',
                      'Email', 'Password', 'Bio', 'Location']
        writer = csv.DictWriter(users, fieldnames=fieldnames)
        writer.writerow({'User_Id': self.user_id,\
         'Username': self.username, 'Email': self.email, 'Password': self.password, 'Bio': self.bio, 'Location':self.location})
        users.close()

