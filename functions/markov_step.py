import classes.customer as customer
import classes.supermarket as supermarket
import classes.tile as tile
import numpy as np

def markov_step(cust, store):
    """_summary_

    Args:
        cust (_type_): _description_
        store (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    current_location = cust.get_location()
    
    prob_matrix = cust.prob_matrix
    
    # first checkout, then dairy, drinks, fruit, spices (order of values inside)
    location_list = ['checkout', 'dairy', 'drinks', 'fruit', 'spices']
    state_vector = [0, 0, 0, 0, 0]
    
    if current_location in location_list:
        # get index of location
        loc_index = location_list.index(current_location)
        
        # mark the location with 1 in the state vector
        state_vector[loc_index] = 1

    # calculate probability that each location is the next one        
    prob = np.dot(np.transpose(prob_matrix), state_vector)

    # find the new location
    new_location = np.random.choice(location_list, p = prob)
    
    # find coordinates of new location
    for i in range(store.grid.shape[0]):
        for j in range(store.grid.shape[1]):
            if store.grid[i, j].location == new_location:
                location_coord = [i,j]
    
    return location_coord