class Dog():
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def pt(self):
        self.year = "10"
        print(self.year)
        return self.year


mydog = Dog("lol",10)
mydog.pt()
