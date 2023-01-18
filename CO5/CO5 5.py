import csv
cars=[{'no':1,'company':'ferrari','model':'34er'},{'no':2,'company':'Hyundai','model':'i10'},{'no':3,'company':'suzuki','model':'Alto'}]
csvfile=open('names.csv','w')
field_names=list(cars[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_names)
writer.writeheader()
writer.writerows(cars)
csvfile.close()

csv_file=open('names.csv','r')
csv_reader=csv.reader(csv_file)
for line in csv_file:
    print(line,end="")