class User():
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, n):
        self._age = n + 5


user = User(0)
user.age = 5
print(user.age)
