from datetime import datetime


class User:
    def __init__(self,name,email,password):
        self.name = name
        self._email = email
        self.password = password
    def cleanEmail(self):
        return self._email.lower().strip()
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    def set_email(self,new_email):
        print(f"Email updated at {datetime.now()}")
        self._email = new_email

user1 = User("Nithish","  TESt1@email.com ",1234)
user2 = User("Dhivyasri","test2@gmail.com",4234)
print("Before",user1.get_email())
user1.set_email("nithish@gmail.com")
print("After",user1.get_email())

