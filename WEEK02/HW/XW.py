import csv

with open("test.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Ali", 25])
    writer.writerow(["Sara", 30])
