'''
Write a Python class named Student with two attributes student_name, marks. 
Modify the attribute values of the said class and print the original 
and modified values of the said attributes.
'''


class Student:
	def __init__(self, student_name: str, mark: int):
		self.name = student_name
		self.mark = mark

	def print_attributes(self):
		print("\nName : {0}".format(self.name))
		print("Mark : {0}".format(self.mark))


if __name__ == '__main__':
	s1 = Student("Rachel", 6)
	s1.print_attributes()
	s1.name = "Michael"
	s1.mark = 7
	s1.print_attributes()
