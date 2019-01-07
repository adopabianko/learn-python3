class Car:

	# attribute yang dimulai dengan underscore merupaka attribute private
	_wheeldrive = 4
	_type = "Sport Car"
	_merk = "Yamada"
	_owner = ""

	# attribute tanpa underscore bersifat public
	color = "green"
	def start_engine(self):
		print ("Starting the car ...")
		print ("owner: %s" % self._owner)
		print ("color: %s" % self.color)
		print ("merk: %s" % self._merk)
		print ("type: %s" % self._type)
		print ("wheeldrive: %s" % self._wheeldrive)

# Proses instansiasi object
car = Car()

# Pemanggilan method
car.start_engine()
