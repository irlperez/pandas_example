import os
import csv
import glob
from pathlib import Path
def write_row(row, age_index, header):
    if os.path.exists(f'./partitioned_data/age={row[age_index]}'):
        os.chdir(f'./partitioned_data/age={row[age_index]}')
        with open('data.csv', 'a') as write_file:
            csv.writer(write_file).writerow(row)
        os.chdir('../..')
    else:
        Path(f'./partitioned_data/age={row[age_index]}').mkdir(parents=True, exist_ok=True)
        os.chdir(f'./partitioned_data/age={row[age_index]}')
        with open('data.csv', 'a') as write_file:
            csv.writer(write_file).writerow(header)
        os.chdir('../..')


def process_data(file_list):
    print('start process')
    print('curren working directory: ', os.getcwd())
    for file_name in file_list:
        with open(file_name) as csv_file:
            row_count = 0 
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if row_count == 0:
                    drop_column_index = row.index('phone') # hard coded value to drop column
                    fname_index = row.index('first_name')
                    lname_index = row.index('last_name')
                    age_index = row.index('age')
                    row.pop(drop_column_index)
                    row.append('last, first')

                    header = row

                    row_count += 1
                else:
                    row.pop(drop_column_index)
                    full_name = f'{row[lname_index], row[fname_index]}'
                    row.append(full_name)
                    write_row(row, age_index, header)
                    row_count += 1

            print(f'processed {row_count} rows.')

                
            
def main():
    os.chdir('./data_sets')
    #os.mkdir('./partitioned_data')
    file_names = glob.glob('*.csv')
    #os.chdir('..')
    process_data(file_names)

if __name__ == '__main__':
    main()


''' pseudocode
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