import csv

with open("ex1.csv", "r") as f:
    info = csv.reader(f)
    print(list(info))

with open("ex1.csv","a") as f:
    m = "'15/12/2025 8:17:50', 'mango', '3'"
    f.writelines("\n")
    f.writelines(m)