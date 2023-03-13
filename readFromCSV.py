import csv

def readCSVAndMap():
  A = list()
  B = list()
  with open('input.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
      A.append(row[0])
      B.append(row[1])

  output = list()

  for i in range(len(A)):
    for j in range(len(B)):
      output.append(A[i] + B[j])

  print(output)

readCSVAndMap()
