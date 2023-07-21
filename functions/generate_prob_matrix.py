import pandas as pd

def generate_prob_matrix(df):
    """This function takes a dataframe with customer movements over time inside the store. It generates a probability matrix of size N x N. where N is the total number of locations in the store. The matrix contains the probabilities that a customer will go to the next location based on the current one within the time defined by the timestep in the dataframe. It is meant to be used further in a Markov chain Monte Carlo simulation.

    INPUT ARGUMENTS:
        -df -> pandas DataFrame with a timedate index, customer_ID and location at every timestep.

    OUTPUT:
        -prob_matrix -> matrix where each element is the probability to transition from one state to another in a Markov chain simulation. 
    """
    
    # create empty series that will be populated with the current and previous locations for each customer
    loc_now = pd.Series(dtype=object)
    loc_before = pd.Series(dtype=object)
    
    # iterate through all customer IDs
    for customer_id in df.day_id.unique():
        
        # find the current and previous locations for just the current customer
        loc_per_customer = df[df['day_id'] ==  customer_id]['location']
        loc_per_customer_before = loc_per_customer.shift(1)
        
        # shifting data will create NaN values for previous locations; they will be replaced with 'entrance'
        loc_per_customer_before.fillna('entrance',
                               inplace=True)
        
        # add the current and previous locations to the series
        loc_now = pd.concat([loc_now,
                            loc_per_customer])
        loc_before = pd.concat([loc_before,
                                loc_per_customer_before])    
    
    # generate transition probability matrix
    prob_matrix = pd.crosstab(loc_before, 
                            loc_now,
                            normalize='index')

    return prob_matrix