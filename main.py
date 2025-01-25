class IterableGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):

        return (x for x in range(self.start, self.end + 1))

iterable_object = IterableGenerator(1, 5)

for value in iterable_object:
    print(value)



