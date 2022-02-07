

# a = input('name: ')
# print('age:')
# b = int(input())
# c={i:i for i in a and b}

# def ras():
#     for ag in c:
#         if ag<=17:
#             print(' ')
#         else:
#             print(f'здраствуйте {name}у нас сейчас   действует акция на алкоголь ') 




# -------------------------------
import schedule
import time
import csv

def write_csv():
    name = input('name: ')
    age = input('age: ')
    with open('usr.csv ', 'a') as csv_file:
        wr = csv.writer(csv_file, delimiter='/')
        wr.writerow(
            (name,age)
            )
    answ = input('continue y or n')
    if answ =='y':
        write_csv()
    else:
        print('Stop!!')


def mailing():
    with open('user.csv', 'r') as csv_file:
        data = csv_file.readlines()
        name = [i.replace('\n','') for i in data]
        for i in name:
            name = i.split('/')
            if int(name[-1] >= 10):
                print(f'скидки {name[0]}')

schedule.every(3).seconds.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)

