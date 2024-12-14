import random

class Human:
    def __init__(self, name="Human", job=None, car=None):
        self.name = name
        self.money = 100
        self.job = job
        self.car = car

    def work(self):
        self.money += self.job.salary
        print(f'{self.name} worked for 8 hours and get {self.job.salary}$')

    def feed(self, pet, food):
        if self.money >= food:
            pet.feed(food)
            self.money -= food
            print(f'{self.name} fed buddy with {food} units of food.')
        else:
            print(f'{self.name} does not have enough money to feed {pet.name}.')

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        print(f"Names of {self.brand} passengers: ")
        for passenger in self.passengers:
            print(passenger.name)

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]

class pet:
    def __init__(self, name, hunger=100):
        self.name = name
        self.hunger = hunger

    def feed(self, food):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print(f'{self.name} hunger level {self.hunger}')

sasha = Human('Sasha', Job(job_list))
print(sasha.money, 'before job')
sasha.work()
print(sasha.money, 'after job')

buddy = pet('Buddy')
sasha.feed(buddy, 30)
print(f"buddy hunger level after feed {buddy.hunger}")

