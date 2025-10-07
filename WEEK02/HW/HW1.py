import csv
import json

#1
def read_lines(file):
    with open('HW1.log', 'r') as f:
        print(f.readlines())
    return f
print(read_lines('HW1.log'))

#2
def extraction():
    with open('HW1.log', 'r') as f:
        for line in f:
            try:
                parts = line.split()
                
                if parts[5] == "[notice]":
                
                    timestamp = f"{parts[0]},{parts[1]},{parts[2]},{parts[3]},{parts[4]}".replace("[", "").replace("]", "")
                    level = f"{parts[5]}".replace("[", "").replace("]", "")
                    message = " ".join(parts[6:])
                    print(f"[{timestamp}] [{level}] {message}")
                
            except:
                continue

extraction()

#3
def errors_extractor():
    c = 0
    with open('HW1.log', 'r') as f:
        for line in f:
            parts = line.split()
            try:
                if parts[5] == "[error]":
                    with open("errors.log", "a") as file:
                        file.writelines(f"{parts} \n")
                        c += 1
            except:
                break

errors_extractor()

#4

def organizer():
    with open('HW1.log', 'r') as f:
        with open("critical_errors.csv", "w", newline = "", encoding = "utf-8") as file:
            timestamp = ("Timestamp")
            message = ("Message")
            rows = (timestamp, message)
            writer = csv.writer(file)
            writer.writerow(rows)

        for line in f:
            try:
                parts = line.split()
                if parts[5] == "[error]":
                    timestamp = " ".join(parts[0:5])
                    message = " ".join(parts[6:])
                    with open("critical_errors.csv", "a", newline = "", encoding = "utf-8") as file:
                            writer1 = csv.writer(file)
                            writer1.writerow((timestamp, message))
            except:
                continue 

organizer()


#5
def logs():
    with open('HW1.log', 'r') as f:
        n = 0
        e = 0
        w = 0
        for line in f:
            parts = line.split()
            try:
                if parts[5] == "[notice]":
                    n += 1
                elif parts[5] == "[error]":
                    e += 1
                elif parts[5] != "[notice]" and parts[5] != "[error]":
                    w += 1
            except IndexError:
                w += 1
    info = {"INFO" : n, "WARNING" : w, "ERROR" : e}
    with open("summary.json", "w") as file:
        json.dump(info, file, indent = 0)
    
logs()

#6
try:
    with open('HW1.log', 'r') as f:
        f.readline()
        extraction()
        errors_extractor()
        organizer()
        logs()
except FileNotFoundError:
    print("Sorry! We can not find your file.")
            












  



   