import csv
csv_file=open('student.csv','r')
csv_reader=csv.reader(csv_file)
for line in csv_reader:
    print(line)