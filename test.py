from datetime import datetime
import time

with open('test1.txt','a') as file:
    time.sleep(100)
    file.write(f'This is file generated from jenkin, at {datetime.now()}  \n')
    
