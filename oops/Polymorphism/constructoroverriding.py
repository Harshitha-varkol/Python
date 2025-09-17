class Instagram:
    def __init__(self,username,id):
        self.username=username
        self.id=id
        print(self.username)
        print(self.id)
class User(Instagram):
    def __init__(self,following,no_of_followers):
        self.following=following
        self.no_of_followers=no_of_followers
        print(self.following)
        print(self.no_of_followers)
u=User(200,"1M")
