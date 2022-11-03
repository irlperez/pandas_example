import csv
from distutils.log import debug
from operator import concat # built in csv library
import os # operating system
import glob
from xml.etree.ElementPath import find # finding path names matching pattern=

# print('hello word')

### testing different os commands.
# print(os.listdir())
# print('test: ', os.getcwd())


''' I scrapped this function because it felt too busy. I broke up the task into seprate functions.
def process_data(file_list, drop_column_name):
    new_data_list = []
    file_count = 0
    
    for file_name in file_list:
        with open(file_name) as csv_file: # 'with' command manages opening and closing of file.
            csv_reader = csv.reader(csv_file, delimiter=',') # returns a reader object that will iterate over lines in a given csvfile.
            row_count = 0 # keeps track of the line number
            
            for row in csv_reader: # for loop, to iterate through each line
                if row_count == 0: # checks if line is 0 to print header.
                    drop_column_number = find_column_number(row, drop_column_name)
                    fname_col_num = find_column_number(row, 'first_name')
                    lname_col_num = find_column_number(row, 'last_name')
                    if file_count == 0:
                        row.append('last_first')
                        print (f'column names are {", ".join(row)}') # i know f-strings. i haven't used join much.
                        new_data_list.append(row)
                    row_count += 1 # increase running count
                else:
                    row.pop(drop_column_number) # drop the column
                    row.append(concat_first_and_last(row, fname_col_num, lname_col_num)) # add concatenated name
                    print(row)
                    new_data_list.append(row)
                    row_count +=1
            print(f'processed {row_count} lines.')
            file_count += 1
    # print(new_data_list)
    
    unique_set_of_ages = set()
    
    for row_number, new_row in enumerate(new_data_list):
        if row_number == 0:
            age_column_num = find_column_number(new_row, 'age')
        else:
            unique_set_of_ages.add(new_row[age_column_num])
    
    for age in unique_set_of_ages:
        current_path = os.getcwd()
        #print(current_path)
        current_path = os.path.join(current_path, str(age))
        #print(current_path)
'''
    



def partition_all_data(data, age_set):
    for age in age_set:
        path = os.getcwd()
        temp_partition = partition_data_by_age(data, age)
        path = os.path.join(path, f'age={str(age)}')
        
        try:
            os.mkdir(path)
        except FileExistsError as fee:
            pass

        os.chdir(path)
        with open(f'data', 'w') as f:
            write = csv.writer(f)
            write.writerows(temp_partition)
        os.chdir('..')

def partition_data_by_age(data, age):
    row_number = 0
    new_data_list = []
    for row in data:
        if row_number == 0:
            age_col_num = find_column_number(row, 'age')
            new_data_list.append(row)
            row_number += 1
        elif row_number > 0 and row[age_col_num] == age:
            new_data_list.append(row)
    # print(new_data_list)
    return new_data_list


def drop_column_from_data(data:list, column_name):
    row_count = 0
    new_data_list = []
    for row in data:
        if row_count == 0:
            drop_col_num = find_column_number(row, column_name)
            row_count += 1
            row.pop(drop_col_num)
            new_data_list.append(row)
        else:
            row.pop(drop_col_num)
            new_data_list.append(row)
    
    # print(new_data_list)
    return new_data_list



def get_data_from_files(file_list):
    file_count = 0 
    row_count = 0
    new_data_list = []
    age_set = set()
    for file_name in file_list:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if file_count == 0 and row_count == 0: # checks to make sure we are on the first file and first row.
                    age_col_num = find_column_number(row, 'age')
                    new_data_list.append(row) # this is our headers
                    row_count += 1
                else:
                    if file_count != 1:
                        age_set.add(row[age_col_num])
                    new_data_list.append(row)
                    row_count += 1
            file_count += 1
            
    # print(new_data_list)
    print(f'processed {row_count} lines.')
    # print('age set: ', age_set)
    return new_data_list, age_set

        

def concat_first_and_last(data):
    row_count = 0
    new_data_list = []
    fname_col_num = find_column_number(data[0], 'first_name')
    lname_col_num = find_column_number(data[0], 'last_name')

    for row in data:
        if row_count == 0:
            row.append('last, first')
            new_data_list.append(row)
            row_count += 1
        else:
            last_first = f'{row[lname_col_num]}, {row[fname_col_num]}'
            row.append(last_first)
            new_data_list.append(row)
    # print(new_data_list[0:3])
    return new_data_list


def get_drop_column_from_user(file_list):
    with open(file_list[0]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header_list = next(csv_reader)

        print(f'please choose a column to drop (number only)')
        for number, header_name in enumerate(header_list):
            print(number, ". ", header_name, sep='')
        
        drop_column_number = int(input(f'enter number [0-{number}]:'))
    # print(header_list[drop_column_number])
    return header_list[drop_column_number]


def find_column_number(row_list, column_name):
    column_number = 0
    for name in row_list:
        if name == column_name:
            return column_number
        column_number +=1

def get_file_names():
    file_list = glob.glob('*.csv') # gets all files matching a string pattern.
    # print(file_list)
    return file_list

def main():
    try:
        os.mkdir('partitioned_data')
    except FileExistsError as fee:
        print(fee)
    os.chdir('./data_sets') # CHanges DIRectory to csv folder.
    data_file_names = get_file_names()
    usr_sel_drop_column = get_drop_column_from_user(data_file_names)
    raw_data, age_set = get_data_from_files(data_file_names)
    raw_data = drop_column_from_data(raw_data, usr_sel_drop_column)
    raw_data = concat_first_and_last(raw_data)
    os.chdir('..')
    os.chdir('./partitioned_data')
    partition_all_data(raw_data, age_set)

    
    




if __name__=="__main__":
    main()

'''
for file in directory:
    row = 0
    for row in file:
        if row == 0:
            find_column_number(drop_number)
        else:
            drop column
            concat first and last
            write_record(row)


def write_record(row):
    age_var = parse_age(row, age_index) # index maybe if it was input from user
    with open(f'partitioned_data/age={age_var}/data', 'append_mode") as f:
        write row

# save memory and time.
# big data sets we will not be able to load data in memory
'''