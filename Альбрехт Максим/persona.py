class Person:
	def __init__(self, name):
		self.name = name

	def say_name(self):
		print(f'Hello, I am {self.name}')


class Student(Person):
	def __init__(self, name, age):
		Person.__init__(self, name)
		self.age = age


		def get_years(self):
			print(f'{self.name} is {self.age} years old')

p = Person("Max")
p.say_name()
s = Student('Alex', 27)
s.say_name()
s.get_years()