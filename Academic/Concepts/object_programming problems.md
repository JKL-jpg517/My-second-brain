[Q1](https://cs61a.org/lab/lab06/#:~:text=%27red%27.-,Q1%3A%20Bank%20Account,-Extend%20the%20BankAccount)
```python
class Transaction:

    def __init__(self, id: int, before: int, after: int):

        self.id = id

        self.before = before

        self.after = after

    def changed(self) -> bool:

        return self.before!=self.after

    def report(self) -> str:

        msg: str = 'no change'

        if self.changed():

            "*** YOUR CODE HERE ***"

            if self.before<self.after:

                msg='increased ' + str(self.before)+ '->'+ str(self.after)

            else:

                msg='decreased '+ str(self.before)+ '->' + str(self.after)

  

        else:

            msg='no change'

        return str(self.id) + ': ' + msg

  

class BankAccount:  

    def __init__(self, account_holder: str):

        self.balance: int = 0

        self.holder = account_holder

        self.transactions=[]

  

    def deposit(self, amount: int) -> int:

        self.balance = self.balance + amount

        self.transactions.append(Transaction(len(self.transactions),self.balance-amount,self.balance))  # a class instance an be the 元素 of lists!!

        return self.balance

  

    def withdraw(self, amount: int) -> int | str:

        if amount > self.balance:

            self.transactions.append(Transaction(len(self.transactions),self.balance,self.balance))

            return 'Insufficient funds'

        self.balance = self.balance - amount

        self.transactions.append(Transaction(len(self.transactions),self.balance+amount,self.balance))

        return self.balance
```


[Q2](### Q2: Email)
```python
class Email:
    def __init__(self, msg: str, sender, recipient_name: str):

        self.msg = msg

        self.sender = sender

        self.recipient_name = recipient_name

  

class Server:

    def __init__(self):

        self.clients = {}

    def send(self, email: Email):


        self.clients[email.recipient_name].inbox.append(email)

  

    def register_client(self, client):

        self.clients[client.name] = client
class Client:

    def __init__(self, server: Server, name: str):

        self.inbox: list = []

        self.server = server

        self.name = name

        server.register_client(self)

  

    def compose(self, message: str, recipient_name: str):

        email = Email(message, self, recipient_name)

        self.server.send(email)
```

[Q3](https://cs61a.org/lab/lab06/#:~:text=c.cents%0A5-,Q3%3A%20Mint,-A%20mint%20is)
```python
class Mint:
    present_year = 2025

    def __init__(self):

        self.update()

    def create(self, coin):


        return coin(self.year)

  

    def update(self) -> None:

        "*** YOUR CODE HERE ***"

        self.year=self.present_year    # 这里定义的是另一个关于year 的attribute; 但是instance attribute 而非intance attribute

class Coin:

    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year: int):

        self.year = year

  

    def worth(self) -> int:

        "*** YOUR CODE HERE ***"
        return self.cents+Mint.present_year-self.year-50 if Mint.present_year-self.year>50 else self.cents

class Nickel(Coin):

    cents = 5

class Dime(Coin):

    cents = 10
```