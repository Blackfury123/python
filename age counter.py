def hotel_cost(nights):
  return 150*nights

def plane_cost(city):
  if city=="bali":
    return 100

  elif city=="dubai":
    return 200

  elif city=="india":
    return 230

  elif city=="north korea":
    return 10

def car_rental(day):
  if day>=10:
    return 3500*day-250
  elif day>=5:
    return 3500*day-120

  elif day>=2:
    return 3500*day-50

  else:
    return 3500*day

vacation=int(input("enter the nights you want to stay : "))
plane=input("enter the place you want to go : ")
car=int(input("enter the amount of days you will rent the car : "))
total=hotel_cost(vacation)+plane_cost(plane)+car_rental(car)
print(total)v.,|[
]p
]