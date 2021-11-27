class Square:
    side: float

    def __init__(self, side: int) -> None:
        self.side = side

    def area(self) -> float:
        return self.side*self.side

    def perimeter(self, side: int) -> int:
        return 4*side

class Traingle:
    side: float
    height: float

    def __init__(self, side: int, height: int) -> None:
        self.side = side
        self.height = height

    def area(self) -> float:
        return (self.side * self.height) / 2

    def perimeter(self, side: int) -> float:
        return 3 * side


list1 = []
for x in range(11, 21):
    list1.append(Square(x))
print(list1)

for z in list1:
    print(z.area())

list2 = []
for x in range(6,11):
    for h in range(15,20):
        list2.append(Traingle(x,h))

for z in list2:
    print(z.area())