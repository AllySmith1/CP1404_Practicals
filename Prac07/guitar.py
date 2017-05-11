class Guitar:
    def __init__(self, ):
        self.name = ""
        self.year = 0
        self.cost = 0

    def __str__(self):
        return '{} ({}) : ${}'.format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2016 - self.year
        return age

    def is_vintage(self):
        age = get_age(self)
        if age >= 50:
            return True
        else:
            return False


