class Account(object):
	def __init__(self, holder, number, balance, credit_line=500):
		self.Holder = holder
		self.Number = number
		self.Balance = balance
		self.CreditLine = credit_line

	def deposit(self, amount):
		self.Balance = amount
	def withdraw(self, amount):
		if self.Balance - amount <= self.CreditLine:
			return False
		else:
			self.Balance -= amount
			return True
	def balance(self):
		return self.Balance
	def transfer(self, target, amount):
		if self.Balance - amount <= self.CreditLine:
			return False
		else:
			self.Balance -= amount
			target.Balance += amount
			return True


class Greeting:
	def __init__(self, name):
		self.name = name

	def __del__(self):
		print("Destructor started")
	def SayHello(self):
		print("Hello, " + self.name)
