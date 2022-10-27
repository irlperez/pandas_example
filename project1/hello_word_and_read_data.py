import csv # built in csv library
import os

print('hello word')

### testing different os commands.
# print(os.listdir())
# print('test: ', os.getcwd())

def process_data(file_name):

    with open(file_name) as csv_file: # 'with' command manages opening and closing of file.
        csv_reader = csv.reader(csv_file, delimiter=',') # returns a reader object that will iterate over lines in a given csvfile.
        line_count = 0 # keeps track of the line number
        
        drop_column = 0
        
        for row in csv_reader: # for loop, to iterate through each line
            if line_count == 0: # checks if line is 0 to print header.
                drop_column = find_column_number(row, 'salary')
                print (f'column names are {", ".join(row)}') # i know f-strings. i haven't used join much.
                line_count += 1 # increase running count
            else:
                row.pop(drop_column)
                print(row)
                line_count +=1
        print(f'processed {line_count} lines.')

def find_column_number(row_list, column_name):
    column_number = 0
    for name in row_list:
        if name == column_name:
            return column_number
        column_number +=1
    


def main():
    fname1 = './data_sets/random-people.csv'
    fname2 = './data_sets/random-people2.csv'

    process_data(fname1)
    process_data(fname2)

if __name__=="__main__":
    main()