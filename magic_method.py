class User:

	name = ""
	phone = ""
	email = ""

	def __init__(self, name="", phone="", email=""):
		print ("User class is created...")
		self.name = name
		self.phone = phone
		self.email = email

	def __ne__(self, other):
		if (self.name != other.name) or (self.phone != other.phone) or (self.email != other.email):
			return True
		else:
			return False

	def __eq__(self, other):
		if (self.name == other.name) and (self.phone == other.phone) and (self.email == other.email):
			return True
		else:
			return False

	def __str__(self):
		return self.name + "," + self.email +"," +self.phone

user1 = User(name="kresna", phone="7501234", email="kresnagaluh@example.com")
user2 = User(name="kresna", phone="7501234", email="kresnagaluh@example.com")
user3 = User(name="toni", phone="7504357", email="toni@example.com")

print (user1)
print (user2)
print (user3)

print (user1 == user2)
print (user1 == user3)
print (user1 != user2)
print (user1 != user3)

