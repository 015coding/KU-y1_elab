class Coin:
  def __init__(self, value = 1):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Coin'

class BankNote:
  def __init__(self, value = 20):
    self.value = value

  def __str__(self):
    return f'{self.value} Baht Banknote'

 #-------------------------TEST----------------------#

# coin = Coin()
# banknote = BankNote()
total = int(input("Input amount : "))


balance = total
if total >= 1000:
    x = total // 1000
    balance = total - (x * 1000)
    print(f"You get {x} of {BankNote(1000)}")
if balance >= 500:
    x = balance // 500
    balance = balance - (x * 500)
    print(f"You get {x} of {BankNote(500)}")
if balance >= 100:
    x = balance // 100
    balance = balance - (x * 100)
    print(f"You get {x} of {BankNote(100)}")
if balance >= 50:
    x = balance // 50
    balance = balance - (x * 50)
    print(f"You get {x} of {BankNote(50)}")
if balance >= 20:
    x = balance // 20
    balance = balance - (x * 20)
    print(f"You get {x} of {BankNote()}")
if balance >= 10:
    x = balance // 10
    balance = balance - (x * 10)
    print(f"You get {x} of {Coin(10)}")
if balance >= 5:
    x = balance // 5
    balance = balance - (x * 5)
    print(f"You get {x} of {Coin(5)}")
if balance >= 2:
    x = balance // 2
    balance = balance - (x * 2)
    print(f"You get {x} of {Coin(2)}")
if balance >= 1:
    x = balance // 1
    balance = balance - (x * 1)
    print(f"You get {x} of {Coin(1)}")