class Whatsapp:
    def status(self):
        print("Sending status")
class User(Whatsapp):
    def status(self):
        print("Sent Text,Photos")
w=User()
w.status()