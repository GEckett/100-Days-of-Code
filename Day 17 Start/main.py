class User:
    def __init__(self, user_id, username,):
        print("New User Added")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        user.following += 1


user_1 = User("001", "Grant")
user_2 = User("002", "Bob")
print(user_1.id)
print(user_1.username)
print(user_1.followers)


