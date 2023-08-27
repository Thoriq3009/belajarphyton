class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age
     self.jalan = jalan

    def say_hello(self):
        print("helo, my name is {} and iam {} years old".format(self.name, self.age))

    def berjalan(self):
        print(f"Nama : {self.name} ")

oPerson = Person ("Budi",19)
oPerson2.say_hello()
oPerson.berjalan()