class Car:
  #attributes
  wheels = 4
  doors = 4
  engine = True

  def __init__(self, model, year, make="Subaru"):
    self.make = make
    self.model = model
    self.year = year

  def stop(self):
    print('The car has stopped')

  def go(self, speed):
    print(f'The car is going {speed}')

car_one = Car('WRX', 2011)
car_one.go('fast')
