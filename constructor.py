class Car:
	_wheel = 4
	_type = ""
	_merk = ""
	_owner = ""
	color = ""

	def __init__(self, owner="unknown", color="green", merk="unknown", types="Sport Car", wheeldrive=4):
		self._owner = owner
		self.color = color
		self._merk = merk
		self._type = types
		self._wheeldrive = wheeldrive

	def get_owner(self):
		return self._owner

	def start_engine(self):
		print ("Starting the car... ")
		print ("owner: %s" % self._owner)
		print ("color: %s" % self.color)
		print ("merk: %s" % self._merk)
		print ("type: %s" % self._type)
		print ("wheeldrive: %s" % self._wheeldrive)

car = Car(wheeldrive=8)
car2 = Car(owner="kresnagaluh", color="red", merk="Isuju", types="City Car")

car.start_engine()
car2.start_engine()

owner = car.get_owner()
owner = car2.get_owner()

print(car.color)
print(car2.color)
