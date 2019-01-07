class Foo:
	def __init__(self):
		print ("Foo class is created...")

	@staticmethod
	def get_foo_info():
		print ("Getting foo information...")

	def get_foo_detail(self):
		print ("Getting foo detail information...")

	def __del__(self):
		print ("Foo class is deleted...")

# Pemanggilan static method, tanpa instansiasi object
Foo.get_foo_info()
# Foo.get_foo_detail()

# Cara biasa dengan instansiasi
foo = Foo()
foo.get_foo_detail()
foo.get_foo_info()
