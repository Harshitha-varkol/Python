from abc import *
class ATM(ABC):
    @abstractmethod
    def sample(self):
        pass
class atm_user(ATM):
    def sample(self):
        print("SAMPLEEEEEE")
a=atm_user()
a.sample()