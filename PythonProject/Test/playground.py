def add(*args):
    # answer = 0
    # for n in args:
    #     answer += n
    # return answer
    return sum(args)

print(add(1, 2, 3, 4, 5))




def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.price = kwargs.get("price")

my_car = Car(make="Mercedes", model="AMG G60")
print(f"{my_car.make} /// {my_car.model}")


# tuple
t = (1, 2, 3)
print(t)