import re
import bcrypt


class User(object):

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self. password = password
        self.bio
        self.location
        self.following = []
        self.followers = []

    @property
    def username(self):
        return self._name

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
        if re.match(r"^[\w\.+\-]+\@[\w]+\.[a-z]{2,3}$", emailstring):
            if self.findall(emailstring) != True:
                self.send_email(emailstring)
                print ("An authentication code has been sent to your email enter it  to continue")
            else:
                return "Email already in use"
        else:
            return 'Invalid email'
        if self.validate_email(emailstring):
            self._email = emailstring
        else:
            return "Enter code to vaildate email"

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
        user = 
        for i in user:
            if value in i:
                return True
            return False

    def send_email(self, email):
        pass
    def validate_email(self, value):
        pass
    def is_following(self):
        pass
    def followers(self):
        pass
    
