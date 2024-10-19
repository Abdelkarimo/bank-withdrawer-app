from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    """ An abstract bank class
    """
    def basicinfo():
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw():
        pass


# Class Swiss
class Swiss(Bank):
    """ A specific type of bank than derives from class Bank

    """
    def __init__(self):
        self.bal=1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: {}".format(self.bal)
    
    def withdraw(self, amount):
        if amount > self.bal :
            print ("Insufficient funds")
        else :
            print ("Withdrawn amount: {}".format(amount))
            self.bal -= amount
            print ("New Balance: {}".format(self.bal))
        return self.bal


# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()