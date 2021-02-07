class TopTen:

    def __init__(self):
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 2

            return val
        
        else:
            raise StopIteration


values = TopTen()

print(next(values))
print(next(values))

for i in values:
    print(i)