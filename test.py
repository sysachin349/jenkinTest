from datetime import datetime


with open('test.txt','a') as file:
    file.write(f'This is file generated from jenkin, at {datetime.now()}  \n')
    