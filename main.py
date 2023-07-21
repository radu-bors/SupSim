import pandas as pd
from load_data import *

if __name__=='__main__':
    print('*** S T A R T ***')
    load_dataframes()
    
    print('\n *** N E W   C O L U M N S ***')
    new_columns()
    
    print('\n *** A D D   N O   C H E C K O U T ***')
    customers_to_checkout = []
    for day in days_data:
        customers_to_checkout.append(get_non_checkout(day))
        
    filled_data = []
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    date = ['02', '03', '04', '05', '06']
    for i, day in enumerate(days_data):
        #print(i)
        #print(day)
        temporary = add_checkout(day, customers_to_checkout[i], date[i], weekdays[i])
        filled_data.append(temporary)
        
    total = pd.concat(filled_data)
    #per_minute(total)
    print(total)

    
    #print(total.head(35))
    #print(total.head(35))
    print(len(total))
    #total.reset_index()
    
    total.to_csv('./data/total.csv', sep=',')