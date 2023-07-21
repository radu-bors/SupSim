import classes.customer as customer
import classes.supermarket as supermarket
import classes.tile as tile
import random

def start_simulation(prob_matrix):
    """This function starts a markov chain monte carlo simulation of customer behavior in a supermarket
    """
    
    # get supermarket dimensions from user
    supermarket_size = input("What size is the supermarket? (give input as m,n)")
    supermarket_size = supermarket_size.split(',')
    supermarket_size = [int(s.strip()) for s in supermarket_size]

    # get simulation time from user
    simulation_time = input("How long do you want to run the simulation? (in minutes)")
    simulation_time = int(simulation_time.strip())
    
    # get coordinates of blocked tiles
    blocked_list = input("Which tiles are blocked? Give input as a list of coordinates [[i_1, j_1], [i_2, j_2]...]")
    blocked_list = eval(blocked_list)
    
    # get coordinates of entrance
    entrace_location = input("Where is the entrance? (give input as coordinates m,n)")
    entrace_location = entrace_location.split(',')
    entrace_location = [int(s.strip()) for s in entrace_location]
    
    # get coordinates of checkout
    checkout_location = input("Where is the checkout? (give input as coordinates m,n)")
    checkout_location = checkout_location.split(',')
    checkout_location = [int(s.strip()) for s in checkout_location]
    
    # get coordinates of dairy
    dairy_location = input("Where is the dairy section? (give input as coordinates m,n)")
    dairy_location = dairy_location.split(',')
    dairy_location = [int(s.strip()) for s in dairy_location]
    
    # get coordinates of spices
    spices_location = input("Where is the spices section? (give input as coordinates m,n)")
    spices_location = spices_location.split(',')
    spices_location = [int(s.strip()) for s in spices_location]
    
    # get coordinates of drinks
    drinks_location = input("Where is the drinks section? (give input as coordinates m,n)")
    drinks_location = drinks_location.split(',')
    drinks_location = [int(s.strip()) for s in drinks_location]
    
    # get coordinates of fruit
    fruit_location = input("Where is the fruits section? (give input as coordinates m,n)")
    fruit_location = fruit_location.split(',')
    fruit_location = [int(s.strip()) for s in fruit_location]
    
    # make dictionary of locations
    locations = {'entrance': entrace_location,
                 'checkout': checkout_location,
                 'dairy': dairy_location,
                 'spices': spices_location,
                 'drinks': drinks_location,
                 'fruit': fruit_location}
    
    
    # create the supermarket
    store = supermarket.Supermarket(supermarket_size,
                                    blocked_list,
                                    locations)
    
    # initialize some variables needed
    timestep = 0            # which minute is simulated
    simulation_states = []  # list of how the supermarket looks like at every minute
    customer_list = []      # list of customers in the store
    
    while timestep < simulation_time:
        
        # customers appear randomly with 0.1 probability at every timestep
        customer_comes = True if random.random() < 0.1 else False
        if customer_comes:
            #create a customer and append it to the list of customers
            customer_list.append(customer.Customer(prob_matrix, 'entrance', entrace_location))
            # put the customer in the store at the tile that corresponds to 'entrance' location
            store.grid[entrace_location].customer = True
        
        # move all existing customers one by one
        for cust in customer_list.copy():
            
            # GET NEW COORDINATES
            new_coordinates = markov_step(cust, store)
            
            # delete the customer from the old tile
            store.grid[cust.coordinates].customer = False
            
            # delete the customer if they are already at checkout from previous step
            if cust.location == 'checkout':
                customer_list.remove(cust)
            else:
                # add customer to new tile
                store.grid[new_coordinates].customer = True
            
                # update the coordinates of the customer object
                cust.move(new_coordinates)
            
        # add the store to the list of simulated steps
        simulation_states.append(store)
        
        # advance simulation to the next timestep
        timestep += 1

    return simulation_states