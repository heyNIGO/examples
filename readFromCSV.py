import csv

# A python class representing a plant.
class Plant:
    def __init__(self, plant_id, employee_count, avg_salary, and_so_on):
        self.plant_id = plant_id
        self.employee_count = int(employee_count)
        self.avg_salary = int(avg_salary)
        self.and_so_on = and_so_on

    def plant_compensation(self):
        return self.avg_salary * self.employee_count

def loadPlantsFromCsv():
  plants = []
  with open('input.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
      # Make a new plant for each row in the CSV.
      plants.append(Plant(row[0], row[1], row[2], "extra"))

  return plants

plants = loadPlantsFromCsv()

for plant in plants:
  print("plant {} has total cost: {}".format(plant.plant_id, plant.plant_compensation()))

