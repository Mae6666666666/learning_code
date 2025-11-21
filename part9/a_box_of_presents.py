from present import Present

class Box:

    def __str__(self):
        return self.total_weight()

    def add_present(self, present: Present):
        self.the_presents = []
        self.overall_weight = 0
        self.the_presents.append(present.name)
        self.overall_weight += present.weight

    def total_weight(self):
        return self.overall_weight




book = Present("ABC Book", 2)

box = Box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box.add_present(cd)
print(box.total_weight())

