import pandas as pd
import numpy as np

import functions.load_data as load_data
import functions.generate_prob_matrix as gen_matrix
import functions.start_simulation as start_simulation

import classes.customer as customer
import classes.supermarket as supermarket
import classes.tile as tile

# read data from file and do preprocessing
total = load_data.ETL_data()

# generate probability matrix
prob_matrix = gen_matrix.generate_prob_matrix(total)

# start simulation
simulated_states = start_simulation.start_simulation(prob_matrix)

# maked images from simulated states

# make animation from all images

