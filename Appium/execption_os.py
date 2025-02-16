import csv
import json
try:
    a = 5/0
    print(a)
except:
    print("cant divide by 0")
finally:
    print("done")

#R to just read
with open("test.txt", "r") as files:
    text = files.read()
    print(text)

#W for remove the old text and re-write new one
with open("test.txt", "w") as files:
    files.write("I like basketball")
    print("done")

#to not remove old stuff from the file

with open("test.txt", "a") as files:
    files.write("\nI love cookies")

#Reading and writing CSV
with open('test_csv.csv','w', newline='') as files:
    csv_content = csv.writer(files)
    csv_content.writerow(["Name", "age"])
    csv_content.writerow(["Adsad", "312"])
    csv_content.writerow(["ad", "1"])
    print(text)

with open('test_csv.csv','r') as files:
    csv_content = csv.reader(files)
    for con in csv_content:
        print(con)

#Reading and writing JSON
with open('test.json', 'w') as files:
    data={
        "Name": "Something",
        "age": 21
    }
    json.dump(data, files)

with open('test.json', 'r') as files:
    json_data = json.load(files)
    print(json_data)