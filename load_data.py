import pandas as pd
import datetime


def load_data():
    
    global days_data, monday, tuesday, wednesday, thursday, friday
    monday = pd.read_csv('./data/monday.csv', sep=';')
    tuesday = pd.read_csv('./data/tuesday.csv', sep=';')
    wednesday = pd.read_csv('./data/wednesday.csv', sep=';')
    thursday = pd.read_csv('./data/thursday.csv', sep=';')
    friday = pd.read_csv('./data/friday.csv', sep=';')
    days_data = [monday, tuesday, wednesday, thursday, friday]
    print('data was loaded.')
    #print(monday)
    return days_data, monday, tuesday, wednesday, thursday, friday
#load_data()


def new_columns():
    
    '''add new column day'''
    monday['day'] = 'monday'
    tuesday['day'] = 'tuesday'
    wednesday['day'] = 'wednesday'
    thursday['day'] = 'thursday'
    friday['day'] = 'friday'
    
    '''set datetime to index for every day'''
    for day in days_data:
        day.timestamp = pd.to_datetime(day.timestamp)
        day.set_index('timestamp', inplace=True)
        
        ''' add new column with day and customer_no'''
        list_of_IDs = []
        for unit in day['customer_no']:
            #print(unit)
            weekday = day['day'][0][:3]
            #print( unit, weekday)
            list_of_IDs.append(weekday +'-'+ str(unit))
        day['day_id'] = list_of_IDs     
    
    print('new columns were added.')
    #print(monday)
    return days_data, monday, tuesday, wednesday, thursday, friday
#new_columns()


def get_non_checkout(df):
    non_checkout_customers = df['customer_no'].max()
    checkout_customers = []
    for c_id in range(non_checkout_customers):
        if not 'checkout' in df[df['customer_no'] == c_id+1]['location'].values:
            checkout_customers.append(c_id+1)
    print('a list of non checkouts was built')
    return checkout_customers

def add_checkout(df, customer_nos, date, day):
    df_fill = pd.DataFrame()
    for p_id in customer_nos:
        #print(p_id)
        trial_id = df.iloc[p_id]['day_id']
        trial_day = df['day'][0][:3]
        #print(p_id, trial_id, trial_day)
        trial_together = trial_day + '-' + str(p_id)
        #print(trial_together)
        df_tmp = pd.DataFrame(data=[[p_id, 'checkout', day, trial_together]],
                              index=[pd.to_datetime(f'2019-09-{date} 21:59:00')],
                              columns=['customer_no', 'location', 'day', 'day_id'])
        df = pd.concat([df, df_tmp])
    print(f'the checkout was added to the data-frame/customers for {day}.')
    return df


if __name__=='__main__':
    print('*** S T A R T ***')
    load_data()
    
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
    print(total)
        #get_non_checkout()

    