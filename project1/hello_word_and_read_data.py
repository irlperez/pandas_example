import csv # built in csv library
import os

print('hello word')
print(os.listdir())
print('test: ', os.getcwd())

with open('./data_sets/random-people.csv') as csv_file: # 'with' command manages opening and closing of file.
    csv_reader = csv.reader(csv_file, delimiter=',') # returns a reader object that will iterate over lines in a given csvfile.
    line_count = 0 # keeps track of the line number
    for row in csv_reader: # for loop, to iterate through each line
        if line_count == 0: # checks if line is 0 to print header.
            print (f'column names are {", ".join(row)}') # i know f-strings. i haven't used join much.
            line_count += 1 # increase running count
        else:
            print(row)
            line_count +=1
    print(f'processed {line_count} lines.')

# there's probably a better way to loop through files within my directory.
with open('./data_sets/random-people2.csv') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print (f'column names are {", ".join(row)}')
            line_count += 1
        else:
            print(row)
            line_count +=1
    print(f'processed {line_count} lines.')